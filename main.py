import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "peso weak dollar strong until:2022-12-31 since:2022-01-01 -filter:replies"
tweets = []
limits = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limits:
        break

    attr = [getattr(tweet,i) for i in vars(tweet)]
    user = [getattr(tweet.user,i) for i in vars(tweet.user)]
    tweets.append(attr + user)

columns = [i for i in vars(tweet)] + [i for i in vars(tweet.user)]

df = pd.DataFrame(tweets, columns=columns)
df.to_csv('test1.csv', index=False)












# @dataclasses.dataclass
# class Tweet(snscrape.base.Item):
# 	url: str
# 	date: datetime.datetime
# 	rawContent: str
# 	renderedContent: str
# 	id: int
# 	user: 'User'
# 	replyCount: int
# 	retweetCount: int
# 	likeCount: int
# 	quoteCount: int
# 	conversationId: int
# 	lang: str
# 	source: typing.Optional[str] = None
# 	sourceUrl: typing.Optional[str] = None
# 	sourceLabel: typing.Optional[str] = None
# 	links: typing.Optional[typing.List['TextLink']] = None
# 	media: typing.Optional[typing.List['Medium']] = None
# 	retweetedTweet: typing.Optional['Tweet'] = None
# 	quotedTweet: typing.Optional['Tweet'] = None
# 	inReplyToTweetId: typing.Optional[int] = None
# 	inReplyToUser: typing.Optional['User'] = None
# 	mentionedUsers: typing.Optional[typing.List['User']] = None
# 	coordinates: typing.Optional['Coordinates'] = None
# 	place: typing.Optional['Place'] = None
# 	hashtags: typing.Optional[typing.List[str]] = None
# 	cashtags: typing.Optional[typing.List[str]] = None
# 	card: typing.Optional['Card'] = None
# 	viewCount: typing.Optional[int] = None
# 	vibe: typing.Optional['Vibe'] = None

# 	username = snscrape.base._DeprecatedProperty('username', lambda self: self.user.username, 'user.username')
# 	outlinks = snscrape.base._DeprecatedProperty('outlinks', lambda self: [x.url for x in self.links] if self.links else [], 'links (url attribute)')
# 	outlinksss = snscrape.base._DeprecatedProperty('outlinksss', lambda self: ' '.join(x.url for x in self.links) if self.links else '', 'links (url attribute)')
# 	tcooutlinks = snscrape.base._DeprecatedProperty('tcooutlinks', lambda self: [x.tcourl for x in self.links] if self.links else [], 'links (tcourl attribute)')
# 	tcooutlinksss = snscrape.base._DeprecatedProperty('tcooutlinksss', lambda self: ' '.join(x.tcourl for x in self.links) if self.links else '', 'links (tcourl attribute)')
# 	content = snscrape.base._DeprecatedProperty('content', lambda self: self.rawContent, 'rawContent')

# 	def __str__(self):
# 		return self.url






# @dataclasses.dataclass
# class User(snscrape.base.Item):
# 	# Most fields can be None if they're not known.

# 	username: str
# 	id: int
# 	displayname: typing.Optional[str] = None
# 	rawDescription: typing.Optional[str] = None # Raw description with the URL(s) intact
# 	renderedDescription: typing.Optional[str] = None # Description as it's displayed on the web interface with URLs replaced
# 	descriptionLinks: typing.Optional[typing.List[TextLink]] = None
# 	verified: typing.Optional[bool] = None
# 	created: typing.Optional[datetime.datetime] = None
# 	followersCount: typing.Optional[int] = None
# 	friendsCount: typing.Optional[int] = None
# 	statusesCount: typing.Optional[int] = None
# 	favouritesCount: typing.Optional[int] = None
# 	listedCount: typing.Optional[int] = None
# 	mediaCount: typing.Optional[int] = None
# 	location: typing.Optional[str] = None
# 	protected: typing.Optional[bool] = None
# 	link: typing.Optional[TextLink] = None
# 	profileImageUrl: typing.Optional[str] = None
# 	profileBannerUrl: typing.Optional[str] = None
# 	label: typing.Optional['UserLabel'] = None

# 	descriptionUrls = snscrape.base._DeprecatedProperty('descriptionUrls', lambda self: self.descriptionLinks, 'descriptionLinks')
# 	linkUrl = snscrape.base._DeprecatedProperty('linkUrl', lambda self: self.link.url if self.link else None, 'link.url')
# 	linkTcourl = snscrape.base._DeprecatedProperty('linkTcourl', lambda self: self.link.tcourl if self.link else None, 'link.tcourl')
# 	description = snscrape.base._DeprecatedProperty('description', lambda self: self.renderedDescription, 'renderedDescription')