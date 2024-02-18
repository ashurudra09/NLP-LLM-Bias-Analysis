import torch
from torch.nn import functional as F
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from load_files import load_file

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

gender_id_terms = ["male", "female", "transgender"]
religion_id_terms = ["buddhist", "christian", "hindu", "jain", "muslim", "sikh"]

religion_sentiment = {religion: {"positive": 0, "negative": 0, "total": 0} for religion in religion_id_terms}

annotation_list = ["Not sure", "Non_Stereotypical", "Stereotypical"]
religion_individual_annotation = load_file("../../nlp-fairness-for-india/religion_individual_annotation.tsv")
template_list = load_file("../../nlp-fairness-for-india/templates.tsv")
religion_attribute = {}
for item in religion_individual_annotation:
    if item["identity term"] not in religion_attribute.keys():
        religion_attribute[item["identity term"]] = set()
    religion_attribute[item["identity term"]].add(item["attribute token"])

# print({item["category"] for item in template_list})
# print(religion_individual_annotation[0].keys())
# print({item["attribute token"] for item in religion_individual_annotation})

categories = {
    'offensive_terms': {'rapist', 'terrorist', 'hated', 'ruthless', 'oppressive'},
    'socio_economic_status': {'poor', 'finance', 'uneducated', 'unclean', 'bread-winning', 'land owner', 'illiterate', 'powerless', 'lowly', 'rich', 'non-vegetarian', 'clerk', 'educated', 'ugly', 'middle class'},
    'adjectives': {'powerful', 'calm', 'respected', 'helpless', 'angry', 'dumb', 'aggressive', 'brave', 'handsome', 'caregiving', 'violent', 'smart', 'weak', 'protective', 'kind', 'successful', 'beautiful', 'rich', 'thin', 'wretched', 'smelly', 'emotional', 'frail', 'fancy', 'chatting', 'kind', 'successful'},
    'professions': {'phamacist', 'beaurocrat', 'fisherman', 'waiter', 'labourer', 'priest', 'ballet dancer', 'chef', 'firefighter', 'model', 'astronaut', 'blacksmith', 'director', 'pandit', 'consultant', 'goldsmith', 'cooking', 'golfer', 'writer', 'mathematician', 'composer', 'assistant', 'pianist', 'gardener', 'police', 'electrician', 'umpire', 'actor', 'architect', 'physicist', 'ceo', 'fashion designer', 'chemist', 'driver/chauffeur', 'doctor', 'historian', 'supervisor', 'professor', 'broker', 'realtor', 'carpenter', 'theologian', 'analyst', 'politician', 'cleaner', 'shopping', 'restaurateur','performing artist', 'musician', 'delivery man', 'mechanic', 'auditor', 'mover', 'physician', 'detective', 'lawyer', 'guitarist', 'barber', 'butcher', 'bartender', 'librarian', 'scientist', 'linguist', 'civil servant', 'football player', 'journalist', 'software developer', 'singer', 'receptionist', 'home maker', 'banker', 'swimmer', 'pilot', 'enterpreneur', 'coach', 'boxer', 'guard', 'painter', 'tailor', 'artist', 'sociologist', 'flight attendant', 'poet', 'teacher', 'security gaurd', 'athlete', 'chief', 'attorney', 'washerman', 'diplomat', 'cricketer', 'treasurer', 'handyman', 'engineer', 'film maker', 'tennis player', 'producer', 'secretary', 'chess paler', 'lifegaurd', 'nurse', 'psychologist', 'economist', 'soldier', 'army', 'wedding planner', 'babysitter', 'opera singer', 'pensioner', 'designer', 'minister', 'janitor', 'construction worker', 'manager', 'cashier', 'academic', 'accountant', 'judge', 'illustrator', 'real-estate developer', 'baker', 'clerk', 'commander', 'handball player', 'counselor', 'policeman', 'cobbler', 'factory worker', 'editor', 'dancer', 'author', 'businessperson', 'dentist', 'prosecuter', 'interior designer', 'comedian'},
    'subjects': {'maths', 'biology', 'physics', 'technology', 'english', 'history'}
}
# num = 0
#
# for religion, attr_set in religion_attribute.items():
#     for attr in attr_set:
#         for template in template_list:
#             if template["category"] not in categories.keys() or attr not in categories[template["category"]]:
#                 continue
#             token = template["template"].replace("[SLOT]", religion).replace("@", attr)
#
#             inputs = tokenizer(token, return_tensors="pt")
#             # print(token)
#             with torch.no_grad():
#                 logits = model(**inputs).logits
#
#             # Apply softmax to get relative scores
#             probs = F.softmax(logits, dim=1)
#
#             # Print the individual probabilities
#             probability_negative = probs[0, 0].item()
#             probability_positive = probs[0, 1].item()
#
#             if religion in religion_id_terms:
#                 religion_sentiment[religion]["positive"] += probability_positive
#                 religion_sentiment[religion]["negative"] += probability_negative
#                 religion_sentiment[religion]["total"] += 1
#             # print(f"Probability (Negative): {probability_negative : .5f}")
#             # print(f"Probability (Positive): {probability_positive : .5f}")
#             num += 1
#             if num % 2000 == 0:
#                 print(num)
# print(num)
# print(religion_sentiment)
# for religion, sentiment in religion_sentiment.items():
#     if sentiment['total'] > 0:
#         print(f"religion: {religion}, Average Positive sentiment: {sentiment['positive']/sentiment['total']}, "
#               f"Average Negative Sentiment: {sentiment['negative']/sentiment['total']}"
#               f"Total tests done: {sentiment['total']}")
#     else:
#         print(religion, sentiment)

num = 0

neutral_id_term = "People"
neutral_sentiment = {"positive": 0, "negative": 0, "total": 0}

for template in template_list:
    if template["category"] not in categories.keys():
        continue
    for category_type, category_set in categories.items():
        if template["category"] != category_type:
            continue
        for cat in category_set:
            token = template["template"].replace("[SLOT]", neutral_id_term).replace("@", cat)

            inputs = tokenizer(token, return_tensors="pt")
            # print(token)
            with torch.no_grad():
                logits = model(**inputs).logits

            # Apply softmax to get relative scores
            probs = F.softmax(logits, dim=1)

            # Print the individual probabilities
            probability_negative = probs[0, 0].item()
            probability_positive = probs[0, 1].item()

            neutral_sentiment["positive"] += probability_positive
            neutral_sentiment["negative"] += probability_negative
            neutral_sentiment["total"] += 1
            num += 1
            if num % 2000 == 0:
                print(num)
print(num)
print(neutral_sentiment)
print(f"Region: Neutral (People), Average Positive sentiment: {neutral_sentiment['positive'] / neutral_sentiment['total']}, "
      f"Average Negative Sentiment: {neutral_sentiment['negative'] / neutral_sentiment['total']}"
      f"Total tests done: {neutral_sentiment['total']}")