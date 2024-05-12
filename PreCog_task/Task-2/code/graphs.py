import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy import average

from utils import get_bias_sq


def plot_graph(keys, incorrect_no_ratios, incorrect_yes_ratios, title, x, y,save):
    fig, subplots = plt.subplots(2, 1, figsize=(x, y))
    # print(subplots)

    subplots[0].barh(keys, incorrect_no_ratios, color=['green' if v >= 0 else 'red' for v in incorrect_no_ratios])
    subplots[0].set_xlabel(f"{title}")
    subplots[0].set_ylabel("incorr_no_ratio")
    subplots[0].set_title(f"{title} plot (incorrect no ratio)")

    subplots[1].barh(keys, incorrect_yes_ratios, color=['green' if v >= 0 else 'red' for v in incorrect_yes_ratios])
    subplots[1].set_xlabel(f"{title}")
    subplots[1].set_ylabel("incorr_yes_ratio")
    subplots[1].set_title(f"{title} plot (incorrect yes ratio)")

    gs = gridspec.GridSpec(2, 2, width_ratios=[3, 3], height_ratios=[3, 3])
    fig.suptitle("Combined Bar Graphs")
    plt.tight_layout()

    if save:
        plt.savefig(f"../graphs/{title}_plot.png")
    # plt.show()
    plt.close()


def identity_bar_graph(identity_list, model_name, save):
    # Extract keys and values
    keys = [key for key in identity_list.keys()]
    yes_nonrand_totals = [identity_list[key]['total_yes'] - identity_list[key]['rand_yes'] for key in
                          identity_list.keys()]
    no_nonrand_totals = [identity_list[key]['total_no'] - identity_list[key]['rand_no'] for key in
                         identity_list.keys()]
    incorrect_no_ratios = [
        (identity_list[key]['incorrect_no'] / (identity_list[key]['total_no'] - identity_list[key]['rand_no'])) for key in
        identity_list.keys()]
    incorrect_yes_ratios = [
        (identity_list[key]['incorrect_yes'] / (identity_list[key]['total_yes'] - identity_list[key]['rand_yes'])) for key
        in
        identity_list.keys()]

    # print(incorrect_yes_ratios)
    # print(incorrect_no_ratios)
    Region_keys = keys[:32]
    avg_incorr_yes = 0
    avg_incorr_no = 0
    avg_total_yes = 0
    avg_total_no = 0
    for key in Region_keys:
        avg_incorr_yes += identity_list[key]["incorrect_yes"]
        avg_incorr_no += identity_list[key]["incorrect_no"]
        avg_total_no += identity_list[key]["total_no"] - identity_list[key]['rand_no']
        avg_total_yes += identity_list[key]["total_yes"] - identity_list[key]['rand_yes']
    avg_incorr_no /= len(Region_keys)
    avg_incorr_yes /= len(Region_keys)
    avg_total_no /= len(Region_keys)
    avg_total_yes /= len(Region_keys)
    avg_incorr_yes_ratio = round(avg_incorr_yes/avg_total_yes,8)
    avg_incorr_no_ratio = round(avg_incorr_no/avg_total_no,8)
    for i in range(len(Region_keys)):
        incorrect_yes_ratios[i] -= avg_incorr_yes_ratio
        incorrect_no_ratios[i] -= avg_incorr_no_ratio
    # print(avg_incorr_no, avg_incorr_yes)
    Region_keys = [key[2:] for key in Region_keys]
    Religion_keys = keys[32:38]
    avg_incorr_yes = 0
    avg_incorr_no = 0
    avg_total_yes = 0
    avg_total_no = 0
    for key in Religion_keys:
        avg_incorr_yes += identity_list[key]["incorrect_yes"]
        avg_incorr_no += identity_list[key]["incorrect_no"]
        avg_total_no += identity_list[key]["total_no"] - identity_list[key]['rand_no']
        avg_total_yes += identity_list[key]["total_yes"] - identity_list[key]['rand_yes']
    avg_incorr_no /= len(Religion_keys)
    avg_incorr_yes /= len(Religion_keys)
    avg_total_no /= len(Religion_keys)
    avg_total_yes /= len(Religion_keys)
    avg_incorr_yes_ratio = round(avg_incorr_yes/avg_total_yes,8)
    avg_incorr_no_ratio = round(avg_incorr_no/avg_total_no,8)
    for i in range(32,38):
        incorrect_yes_ratios[i] -= avg_incorr_yes_ratio
        incorrect_no_ratios[i] -= avg_incorr_no_ratio
    Religion_keys = [key[2:] for key in Religion_keys]
    Caste_keys = keys[38:]
    avg_incorr_yes = 0
    avg_incorr_no = 0
    avg_total_yes = 0
    avg_total_no = 0
    for key in Caste_keys:
        avg_incorr_yes += identity_list[key]["incorrect_yes"]
        avg_incorr_no += identity_list[key]["incorrect_no"]
        avg_total_no += identity_list[key]["total_no"] - identity_list[key]['rand_no']
        avg_total_yes += identity_list[key]["total_yes"] - identity_list[key]['rand_yes']
    avg_incorr_no /= len(Caste_keys)
    avg_incorr_yes /= len(Caste_keys)
    avg_total_no /= len(Caste_keys)
    avg_total_yes /= len(Caste_keys)
    avg_incorr_yes_ratio = avg_incorr_yes/avg_total_yes
    avg_incorr_no_ratio = avg_incorr_no/avg_total_no
    for i in range(38,45):
        incorrect_yes_ratios[i] -= round(avg_incorr_yes_ratio,8)
        incorrect_no_ratios[i] -= round(avg_incorr_no_ratio,8)
    Caste_keys = [key[2:] for key in Caste_keys]
    # print(Region_keys)
    # print(Religion_keys)
    # print(Caste_keys)
    print()
    print(model_name)
    print("Region:")
    print((get_bias_sq(incorrect_yes_ratios[:32])+get_bias_sq(incorrect_no_ratios[:32]))/2)
    print("Religion:")
    print((get_bias_sq(incorrect_yes_ratios[32:38])+ get_bias_sq(incorrect_no_ratios[32:38]))/2)
    print("Caste:")
    print((get_bias_sq(incorrect_yes_ratios[38:])+get_bias_sq(incorrect_no_ratios[38:]))/2)
    plot_graph(Region_keys, incorrect_no_ratios[:32],incorrect_yes_ratios[:32], model_name +"_Region", 10, 11, save)
    plot_graph(Religion_keys, incorrect_no_ratios[32:38],incorrect_yes_ratios[32:38], model_name + "_Religion", 10, 11, save)
    plot_graph(Caste_keys, incorrect_no_ratios[38:],incorrect_yes_ratios[38:], model_name + "_Caste", 10, 11, save)


def gender_bar_graph(gender_list, model_name, save):
    # Extract keys and values
    keys = list(gender_list.keys())
    # print(keys)
    incorrect_no_ratios = [
        gender_list[key]['incorrect_no'] / (gender_list[key]['total_no'] - gender_list[key]['rand_no']) for key in
        gender_list.keys()]
    incorrect_yes_ratios = [
        gender_list[key]['incorrect_yes'] / (gender_list[key]['total_yes'] - gender_list[key]['rand_yes']) for key in
        gender_list.keys()]
    # print(keys)
    avg_incorr_yes = 0
    avg_incorr_no = 0
    avg_total_yes = 0
    avg_total_no = 0
    for key in keys:
        avg_incorr_yes += gender_list[key]["incorrect_yes"]
        avg_incorr_no += gender_list[key]["incorrect_no"]
        avg_total_no += gender_list[key]["total_no"] - gender_list[key]['rand_no']
        avg_total_yes += gender_list[key]["total_yes"] - gender_list[key]['rand_yes']
    avg_incorr_no /= len(keys)
    avg_incorr_yes /= len(keys)
    avg_total_no /= len(keys)
    avg_total_yes /= len(keys)
    avg_incorr_yes_ratio = avg_incorr_yes/avg_total_yes
    avg_incorr_no_ratio = avg_incorr_no/avg_total_no
    for i in range(2):
        incorrect_yes_ratios[i] -= avg_incorr_yes_ratio
        incorrect_no_ratios[i] -= avg_incorr_no_ratio

    print("Gender:")
    print((get_bias_sq(incorrect_yes_ratios)+get_bias_sq(incorrect_no_ratios))/2)
    plot_graph(keys,incorrect_no_ratios,incorrect_yes_ratios, model_name + "_Gender", 10, 11, save)
