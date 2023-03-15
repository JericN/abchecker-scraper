import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "peso weak dollar strong until:2022-12-31 since:2022-10-01 -filter:replies"
tweets = []
limits = 1500

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent])

df = pd.DataFrame(tweets, columns=["date", "username", "rawContent"])
print(df)
df.to_csv('raw_data.csv', index=False)