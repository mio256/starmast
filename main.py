import pprint
import json
from datetime import date, datetime
from mastodon import Mastodon


def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


mastodon = Mastodon(access_token='pytooter_usercred.secret')
r = mastodon.timeline_home()
pprint.pprint(r)

with open('tmp.json', 'w') as f:
    json.dump(r, f, indent=4, default=json_serial)
