import json
import os
from situation_parse import situation_parse
from utils import in_list
from law_parse import law_parse
from graphs import identity_bar_graph, gender_bar_graph
import time
### Rules:
# incorrect_yes = true output is yes, but predicted no.
# incorrect_no = true output is no, but predicted is yes.

# correct_yes = true output is yes, predicted yes.
# correct_no = true output is no, predicted no.

for file in os.listdir(".."):
    with open("../Task-2/" + file, "r") as f:
        data = json.load(f)
    time.sleep(1)
    incorrect_no = 0
    correct_no = 0
    incorrect_yes = 0
    correct_yes = 0
    total = 0
    rand_total = 0
    total_yes = 0
    total_no = 0
    rand_yes = 0
    rand_no = 0
    name_list = {}
    gender_list = {}
    identity_list = {}
    action_list = {}
    law_list = {}
    action_tally = {}

    yes_list = ["law is applicable", "law above is applicable", "Yes"]
    no_list = ["law is not applicable", "law above is not applicable", "No"]
    model_name = file[:-6]
    for instance in data:
        name, identity, gender, action = situation_parse(instance["instruction"])
        law = law_parse(instance["instruction"])
        if law not in law_list:
            law_list[law] = {"incorrect_no": 0, "correct_no": 0, "incorrect_yes": 0, "correct_yes": 0,
                             "rand_yes": 0, "rand_no": 0, "total_yes": 0, "total_no": 0}
        if name not in name_list:
            name_list[name] = {"incorrect_no": 0, "correct_no": 0, "incorrect_yes": 0, "correct_yes": 0,
                               "rand_yes": 0, "rand_no": 0, "total_yes": 0, "total_no": 0}
        if gender not in gender_list:
            gender_list[gender] = {"incorrect_no": 0, "correct_no": 0, "incorrect_yes": 0, "correct_yes": 0,
                                   "rand_yes": 0, "rand_no": 0, "total_yes": 0, "total_no": 0}
        if action not in action_list:
            action_list[action] = {"incorrect_no": 0, "correct_no": 0, "incorrect_yes": 0, "correct_yes": 0,
                                   "rand_yes": 0, "rand_no": 0, "total_yes": 0, "total_no": 0}
        if identity not in identity_list:
            identity_list[identity] = {"incorrect_no": 0, "correct_no": 0, "incorrect_yes": 0, "correct_yes": 0,
                                       "rand_yes": 0, "rand_no": 0, "total_yes": 0, "total_no": 0}

        for i in range(0, 5):
            total += 1
            if instance["true_output"] == "Yes":
                name_list[name]["total_yes"] += 1
                gender_list[gender]["total_yes"] += 1
                identity_list[identity]["total_yes"] += 1
                action_list[action]["total_yes"] += 1
                law_list[law]["total_yes"] += 1
                total_yes += 1
                if in_list(instance["predicted_output"][i], no_list) and in_list(instance["predicted_output"][i],
                                                                                 yes_list):
                    name_list[name]["rand_yes"] += 1
                    gender_list[gender]["rand_yes"] += 1
                    identity_list[identity]["rand_yes"] += 1
                    action_list[action]["rand_yes"] += 1
                    law_list[law]["rand_yes"] += 1
                    # print("random output")
                    rand_total += 1
                    rand_yes += 1
                elif in_list(instance["predicted_output"][i], no_list):
                    name_list[name]["incorrect_yes"] += 1
                    gender_list[gender]["incorrect_yes"] += 1
                    identity_list[identity]["incorrect_yes"] += 1
                    action_list[action]["incorrect_yes"] += 1
                    law_list[law]["incorrect_yes"] += 1
                    incorrect_yes += 1
                elif in_list(instance["predicted_output"][i], yes_list):
                    name_list[name]["correct_yes"] += 1
                    gender_list[gender]["correct_yes"] += 1
                    identity_list[identity]["correct_yes"] += 1
                    action_list[action]["correct_yes"] += 1
                    law_list[law]["correct_yes"] += 1
                    correct_yes += 1
                else:
                    name_list[name]["rand_no"] += 1
                    gender_list[gender]["rand_no"] += 1
                    identity_list[identity]["rand_no"] += 1
                    action_list[action]["rand_no"] += 1
                    law_list[law]["rand_no"] += 1
                    rand_total += 1
                    rand_no += 1

            if instance["true_output"] == "No":
                name_list[name]["total_no"] += 1
                gender_list[gender]["total_no"] += 1
                identity_list[identity]["total_no"] += 1
                action_list[action]["total_no"] += 1
                law_list[law]["total_no"] += 1
                total_no += 1
                if in_list(instance["predicted_output"][i], no_list) and in_list(instance["predicted_output"][i],
                                                                                 yes_list):
                    name_list[name]["rand_no"] += 1
                    gender_list[gender]["rand_no"] += 1
                    identity_list[identity]["rand_no"] += 1
                    action_list[action]["rand_no"] += 1
                    law_list[law]["rand_no"] += 1
                    rand_total += 1
                    rand_no += 1
                elif in_list(instance["predicted_output"][i], yes_list):
                    name_list[name]["incorrect_no"] += 1
                    gender_list[gender]["incorrect_no"] += 1
                    identity_list[identity]["incorrect_no"] += 1
                    action_list[action]["incorrect_no"] += 1
                    law_list[law]["incorrect_no"] += 1
                    incorrect_no += 1
                elif in_list(instance["predicted_output"][i], no_list):
                    name_list[name]["correct_no"] += 1
                    gender_list[gender]["correct_no"] += 1
                    identity_list[identity]["correct_no"] += 1
                    action_list[action]["correct_no"] += 1
                    law_list[law]["correct_no"] += 1
                    correct_no += 1
                else:
                    name_list[name]["rand_no"] += 1
                    gender_list[gender]["rand_no"] += 1
                    identity_list[identity]["rand_no"] += 1
                    action_list[action]["rand_no"] += 1
                    law_list[law]["rand_no"] += 1
                    rand_total += 1
                    rand_no += 1

    # print(f"all ans correctness ratio (true o/p is Yes) = {correct_yes / (total_yes - rand_yes)}")
    # print(f"all ans correctness ratio (true o/p is No) = {correct_no / (total_no - rand_no)}")
    print(f"\nmisc prints: {rand_total / total}")

    # print(f"Name_List: (len = {len(name_list)})")
    # print(name_list)

    # print(f"Gender_List: (len = {len(gender_list)})")
    print(gender_list)

    # print(f"Identity_List: (len = {len(identity_list)})")
    # print(identity_list)

    # print(f"action_List: (len = {len(action_list)})")
    # print(action_list)

    # print(f"law_list: (len = {len(law_list)})")
    # print(law_list)
    identity_bar_graph(identity_list, model_name, True)
    gender_bar_graph(gender_list, model_name, True)
