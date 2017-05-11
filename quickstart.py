from instapy import InstaPy

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

dont_like = ['sex', 'nsfw', 'girl', 'pizza', 'gluten', 'weightloss', 'hair', 'popdaily', 'like4like', 'bodybuilder', 'loveme', '#kiss', '#xoxo', '#selfie', 'iloveyou', '#love']
ignore_words = []
friend_list = []
ignore_users = ['foodienepal', 'yamiez_ynr', 'beatricesblog', 'realgoodyummiez']

tags = ['#foodporn', '#foodpics', '#instafood', '#meatporn', '#barbecue', '#grilling', '#onthetable']

InstaPy(username='ekampf', password='Assert123', nogui=True)\
  .login()\
  .set_ignore_users(ignore_users) \
  .set_upper_follower_count(limit=2500) \
  .set_ignore_if_contains(ignore_words) \
  .set_dont_like(dont_like) \
  .like_by_tags(tags, amount=100) \
  .set_do_follow(enabled=True, percentage=20) \
  .set_comment([u'\u0001f924']) \
  .set_do_comment(enabled=True, percentage=20) \
  .end()
