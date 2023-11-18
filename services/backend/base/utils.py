from hashids import Hashids
from django.conf import settings

hashids = Hashids(salt=settings.HASHIDS_SALT, min_length=settings.HASHIDS_MIN_LENGTH)


def encode_id(id):
    return hashids.encode(id)


def decode_hashid(hashid):
    try:
        return hashids.decode(hashid)[0]
    except IndexError:
        return None
