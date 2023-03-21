# Import
import config.config as config
from adfly import AdflyApi


def short(url):
    api = AdflyApi(
        user_id=config.user_id,
        public_key=config.public_key,
        secret_key=config.secret_key,
    )

    return api.shorten(url)
