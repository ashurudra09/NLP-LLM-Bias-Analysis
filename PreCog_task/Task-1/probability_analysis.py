import matplotlib.pyplot as plt


def relative_sentiment_score(neutral_sentiment, id_sentiment):
    if id_sentiment["total"] == 0 or id_sentiment["total"] < 100:
        return -69
    id_positive = id_sentiment["positive"]/id_sentiment["total"]
    neutral_positive = neutral_sentiment["positive"]/neutral_sentiment["total"]
    return id_positive - neutral_positive

def relative_sentiments(neutral_sentiment, id_sentiment_list):
    rel_sentiment = {}
    for id_term, id_sentiment in id_sentiment_list.items():
        if id_sentiment["total"] == 0:
            continue
        rel_sentiment[id_term] = relative_sentiment_score(neutral_sentiment,id_sentiment)
    return rel_sentiment

def print_relative_sentiments(neutral_sentiment, id_sentiment_list):
    rel_sentiment = relative_sentiments(neutral_sentiment, id_sentiment_list)

    for id_term, rel_score in rel_sentiment.items():
        print(f"Identity term: {id_term}, Relative sentiment: {rel_score : .4f}")

def graph_relative_sentiments(neutral_sentiment, id_sentiment_list, name, save):
    rel_sentiment = relative_sentiments(neutral_sentiment, id_sentiment_list)

    Titles = []
    Values = []
    for id_term, rel_score in rel_sentiment.items():
        if rel_score == -69:
            print(f"{name} term: {id_term}, Relative sentiment: Not enough data")
            continue

        print(f"{name} term: {id_term}, Relative sentiment: {rel_score : .4f}")
        Titles.append(id_term)
        Values.append(rel_score)

    plt.bar(Titles, Values, color=['green' if v >= 0 else 'red' for v in Values])
    plt.xlabel(f'{name} term')
    plt.ylabel('Values')
    plt.xticks(rotation='vertical')
    plt.title(f'Relative Sentiment Graph for {name}')
    plt.tight_layout()

    # Display the graph
    if save:
        plt.savefig(f"graphs/{name}_sentiment_bar.png")
    plt.show()
