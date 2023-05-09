import os
from mastodon import Mastodon
from dotenv import load_dotenv
load_dotenv()

Mastodon.create_app(
    'pytooterapp',
    api_base_url=os.environ['API_BASE_URL'],
    to_file='pytooter_clientcred.secret'
)

mastodon = Mastodon(client_id='pytooter_clientcred.secret',)
email = input('email > ')
password = input('password > ')
mastodon.log_in(
    email,
    password,
    to_file='pytooter_usercred.secret'
)
