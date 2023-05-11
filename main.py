import os
import json
from datetime import date, datetime
from mastodon import Mastodon
from dotenv import load_dotenv
load_dotenv()


def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


mastodon = Mastodon(
    os.environ['CLIENT_ID'],
    os.environ['CLIENT_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['API_BASE_URL'],
)

r = mastodon.timeline_home()
for i in r:
    print(i.account.username)
    print(i.content)

with open('tmp.json', 'w') as f:
    json.dump(r, f, indent=4, default=json_serial)
