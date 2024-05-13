from random import shuffle

import torch
from torch.nn import functional as F
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from load_files import load_file

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

gender_id_terms = ["male", "female"]

gender_sentiment = {gender: {"positive": 0, "negative": 0, "total": 0} for gender in gender_id_terms}

annotation_list = ["Not sure", "Non_Stereotypical", "Stereotypical"]
gender_proxy_idterms = load_file("../Task-2/nlp-fairness-for-india/gender_proxy_idterms.tsv")
template_list = load_file("../Task-2/nlp-fairness-for-india/templates.tsv")

categories = {
    # 'clothes': {}, # ignored this category
    # 'verbs': {'coach', 'judge', 'hated', 'cook', 'covered', 'dance', 'successful'},
    # 'offensive_terms': {'ugly', 'criminal', 'rapist', 'hated', 'violent', 'dumb', 'ruthless'},
    # 'socio_economic_status': {'poor', 'rich', 'fancy', 'lowly', 'powerful', 'handsome', 'successful'},
    # 'adjectives': {'helpless', 'angry', 'ugly', 'beautiful', 'fancy', 'hated', 'emotional', 'violent', 'brave', 'calm', 'lowly', 'colourful', 'powerful', 'handsome', 'fat', 'caring', 'thin', 'smart', 'weak', 'protective', 'kind', 'dumb', 'spicy', 'ruthless', 'respected', 'smart'},
    'professions': {'musician', 'painter', 'editor', 'coach', 'cleaner', 'boxer', 'tailor', 'farmer', 'engineer', 'treasurer', 'clerk', 'dentist', 'poet', 'composer', 'consultant', 'commander', 'doctor', 'pilot', 'lawyer', 'nurse', 'librarian', 'professor', 'analyst', 'astronaut', 'accountant', 'cook', 'sociologist', 'broker', 'diplomat', 'soldier', 'cricketer', 'carpenter', 'chef', 'driver', 'assistant', 'academic', 'mathematician', 'cashier', 'author', 'singer', 'manager', 'army', 'economist', 'fisherman', 'auditor', 'scientist', 'writer', 'golfer', 'barber', 'artist', 'guard', 'baker', 'detective', 'police', 'director', 'athlete', 'teacher', 'psychologist', 'mechanic', 'guitarist', 'designer', 'journalist', 'banker', 'labourer', 'architect', 'actor', 'attorney', 'policeman'},
    # 'food': {}, # ignored this category
    # 'subjects': {'science', 'physics', 'maths', 'humanities', 'chemistry', 'biology', 'technology', 'english', 'history'}
}

num = 0

base_id_terms = ["person", "he", "she"]
base_sentiment = {item: {"positive": 0, "negative": 0, "total": 0} for item in base_id_terms}
# print(gender_proxy_idterms)
for template in template_list:
    if template["category"] not in categories.keys():
        continue
    for category_type, category_set in categories.items():
        if template["category"] != category_type:
            continue
        for cat in category_set:
            for term in base_id_terms:
                token = template["template"].replace("[SLOT]", term).replace("@", cat)

                inputs = tokenizer(token, return_tensors="pt")
                # print(token)
                with torch.no_grad():
                    logits = model(**inputs).logits

                # Apply softmax to get relative scores
                probs = F.softmax(logits, dim=1)

                # Print the individual probabilities
                probability_negative = probs[0, 0].item()
                probability_positive = probs[0, 1].item()

                base_sentiment[term]["positive"] += probability_positive
                base_sentiment[term]["negative"] += probability_negative
                base_sentiment[term]["total"] += 1
                num += 1
                if num % 2000 == 0:
                    print(num)
print(num)
print(base_sentiment)
num = 0
for template in template_list:
    if template["category"] not in categories.keys():
        continue
    for category_type, category_set in categories.items():
        if template["category"] != category_type:
            continue
        for cat in category_set:
            count = 0
            for term in gender_proxy_idterms:
                count += 1
                if count % 50 != 0:
                    continue
                token = template["template"].replace("[SLOT]", term["proxy_identity_terms"]).replace("@", cat)

                inputs = tokenizer(token, return_tensors="pt")
                # print(token)
                with torch.no_grad():
                    logits = model(**inputs).logits

                # Apply softmax to get relative scores
                probs = F.softmax(logits, dim=1)

                # Print the individual probabilities
                probability_negative = probs[0, 0].item()
                probability_positive = probs[0, 1].item()

                gender_sentiment[term["parent_idterm"]]["positive"] += probability_positive
                gender_sentiment[term["parent_idterm"]]["negative"] += probability_negative
                gender_sentiment[term["parent_idterm"]]["total"] += 1
                num += 1
                if num % 2000 == 0:
                    print(num)
print(num)
print(gender_sentiment)
for gender, sentiment in gender_sentiment.items():
    if sentiment['total'] > 0:
        print(f"Region: {gender}, Average Positive sentiment: {sentiment['positive']/sentiment['total']}, "
              f"Average Negative Sentiment: {sentiment['negative']/sentiment['total']}"
              f"Total tests done: {sentiment['total']}")
    else:
        print(gender, sentiment)
