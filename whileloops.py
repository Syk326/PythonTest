# while loops
def nearest_square(limit):
    number = 0
    while (number+1) ** 2 < limit:
        number += 1
    return number ** 2
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

# black jack
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand) <= 21:
    hand.append(card_deck.pop()) #removes from deck
print(hand)

# headline ticker for news, up to 140 chars
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    if len(news_ticker) + len(headline) <= 140:
        news_ticker += headline + " "
    else:
        for letter in headline:
            if len(news_ticker) < 140:
                news_ticker += letter
            else:
                break;
print(news_ticker)
# alternative for above, shorter
news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140: # just take first 140 after creating full
        news_ticker = news_ticker[:140]
        break;
print(news_ticker)
