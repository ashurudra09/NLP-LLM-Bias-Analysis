from probability_analysis import print_relative_sentiments, graph_relative_sentiments
from load_files import load_file
# region_sentiment = {'andamanese': {'positive': 0, 'negative': 0, 'total': 0}, 'assamese': {'positive': 1085.886233099096, 'negative': 560.1137662999972, 'total': 1646}, 'bengali': {'positive': 1235.167834324704, 'negative': 410.83216661022743, 'total': 1646}, 'bihari': {'positive': 940.2712482272764, 'negative': 359.72875178136746, 'total': 1300}, 'chattisgarhi': {'positive': 721.8257397575944, 'negative': 320.17425857667695, 'total': 1042}, 'delhiite': {'positive': 0, 'negative': 0, 'total': 0}, 'goan': {'positive': 697.9204973082233, 'negative': 437.0795012170274, 'total': 1135}, 'gujarati': {'positive': 1213.2342405714153, 'negative': 432.76576020942593, 'total': 1646}, 'jharkhandi': {'positive': 1041.2232989832119, 'negative': 474.77670275521814, 'total': 1516}, 'kannadiga': {'positive': 758.1183667246078, 'negative': 153.8816309527174, 'total': 912}, 'kashmiri': {'positive': 990.9565926393843, 'negative': 492.04340824535757, 'total': 1483}, 'keralite': {'positive': 0, 'negative': 0, 'total': 0}, 'madhya pradeshi': {'positive': 1030.3424388750718, 'negative': 447.65756349501316, 'total': 1478}, 'maharashtrian': {'positive': 0, 'negative': 0, 'total': 0}, 'manipuri': {'positive': 605.0061407252215, 'negative': 254.99385854197317, 'total': 860}, 'marathi': {'positive': 955.3801079856348, 'negative': 605.6198926748475, 'total': 1561}, 'marwari': {'positive': 0, 'negative': 0, 'total': 0}, 'meghalayan': {'positive': 730.407119034644, 'negative': 131.59288058243692, 'total': 862}, 'mizo': {'positive': 14.193264741130406, 'negative': 43.8067351449281, 'total': 58}, 'odiya': {'positive': 812.2575174351514, 'negative': 773.7424851506221, 'total': 1586}, 'pahari': {'positive': 0, 'negative': 0, 'total': 0}, 'punjabi': {'positive': 1051.8512098057545, 'negative': 594.1487905425747, 'total': 1646}, 'rajasthani': {'positive': 1333.8096958122915, 'negative': 297.19030481208756, 'total': 1631}, 'sikkemese': {'positive': 0, 'negative': 0, 'total': 0}, 'tamilian': {'positive': 1187.5388141182775, 'negative': 443.4611875646078, 'total': 1631}, 'telugu': {'positive': 342.88482961052796, 'negative': 109.1151696471643, 'total': 452}, 'tripuri': {'positive': 291.23053426120896, 'negative': 104.7694650899357, 'total': 396}, 'uttar pradeshi': {'positive': 1015.5025654722413, 'negative': 570.4974329329125, 'total': 1586}, 'uttarakhandi': {'positive': 1196.970670556766, 'negative': 434.029328809469, 'total': 1631}, 'arunachali': {'positive': 713.8339268234558, 'negative': 183.16607519086392, 'total': 897}, 'haryanvi': {'positive': 603.254807521007, 'negative': 316.74519252579194, 'total': 920}, 'himachali': {'positive': 176.951924117835, 'negative': 91.04807678141515, 'total': 268}}
# region_neutral = {'positive': 1263.7371337812656, 'negative': 382.26286679922487, 'total': 1646}
#
# religion_sentiment = {'buddhist': {'positive': 1524.4369183703966, 'negative': 1450.5630834045878, 'total': 2975}, 'christian': {'positive': 2313.6517669221357, 'negative': 661.3482321461706, 'total': 2975}, 'hindu': {'positive': 1807.9726783852675, 'negative': 1167.027319909539, 'total': 2975}, 'jain': {'positive': 2054.64800421815, 'negative': 920.3519963065992, 'total': 2975}, 'muslim': {'positive': 1277.750911775307, 'negative': 1697.249088749777, 'total': 2975}, 'sikh': {'positive': 1894.1628421043279, 'negative': 1080.8371564257613, 'total': 2975}}
# religion_neutral = {'positive': 2003.2974480340781, 'negative': 971.7025513478584, 'total': 2975}
#
# gender_sentiment = {'male': {'positive': 48076.48702869889, 'negative': 22973.512981947628, 'total': 71050}, 'female': {'positive': 45698.046645604394, 'negative': 25351.9533544304, 'total': 71050}}
# gender_neutral = {'positive': 1272.588857295661, 'negative': 373.4111420423433, 'total': 1646}
# gender_he = {'positive': 1217.7993506733037, 'negative': 428.20065026813245, 'total': 1646}
# gender_she = {'positive': 1251.8115325699036, 'negative': 394.188465070285, 'total': 1646}
# gender_occ_sentiment = {'male': {'positive': 35054.13020820428, 'negative': 15945.869788899232, 'total': 51000}, 'female': {'positive': 32972.23964701373, 'negative': 18027.760353154037, 'total': 51000}}
# gender_occ_neutral = {'positive': 813.3619418824092, 'negative': 206.63805779704126, 'total': 1020}
# gender_occ_he = {'positive': 775.6102442797273, 'negative': 244.38975585770095, 'total': 1020}
# gender_occ_she = {'positive': 800.4499701182358, 'negative': 219.55002758320188, 'total': 1020}
# graph_relative_sentiments(region_neutral, region_sentiment, "Region", 1)
# graph_relative_sentiments(religion_neutral, religion_sentiment, "Religion", 1)
# print_relative_sentiments(religion_neutral, religion_sentiment)
# print_relative_sentiments(gender_neutral, gender_sentiment)
#
# graph_relative_sentiments(gender_neutral, gender_sentiment, "Gender", 1)
# graph_relative_sentiments(gender_he, gender_sentiment, "Gender_wrt_he", 1)
# graph_relative_sentiments(gender_she, gender_sentiment, "Gender_wrt_she", 1)
# graph_relative_sentiments(gender_occ_neutral, gender_occ_sentiment, "Gender", 1)
# graph_relative_sentiments(gender_occ_he, gender_occ_sentiment, "Gender_wrt_he", 0)
# graph_relative_sentiments(gender_occ_she, gender_occ_sentiment, "Gender_wrt_she", 0)
# region_individual_annotation = load_file("../../nlp-fairness-for-india/region_individual_annotation.tsv")
# religion_individual_annotation = load_file("../../nlp-fairness-for-india/religion_individual_annotation.tsv")


caste_neutral = {'positive': 1284.2600174564286, 'negative': 511.73998157776805, 'total': 1796}
caste_sentiment = {'brahmin person': {'positive': 734.1079829287482, 'negative': 1061.8920190454082, 'total': 1796}, 'dalit person': {'positive': 255.37302261515288, 'negative': 1540.6269794801337, 'total': 1796}, 'khsatirya person': {'positive': 1223.426568957162, 'negative': 572.5734308193205, 'total': 1796}, 'vaishya person': {'positive': 1300.002596277831, 'negative': 495.997403126923, 'total': 1796}, 'obc person': {'positive': 286.42717287453706, 'negative': 1509.5728259054013, 'total': 1796}, 'sc/st person': {'positive': 930.9542868236458, 'negative': 865.0457133897289, 'total': 1796}, 'shudra person': {'positive': 883.898889700853, 'negative': 912.1011095136128, 'total': 1796}}

print_relative_sentiments(caste_neutral, caste_sentiment)
graph_relative_sentiments(caste_neutral, caste_sentiment, "Caste", 1)
