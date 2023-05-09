import pprint
from mastodon import Mastodon

mastodon = Mastodon(access_token='pytooter_usercred.secret')
r = mastodon.timeline_home()
pprint.pprint(r)
