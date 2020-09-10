import datetime
import requests
import json

from functools import reduce
from collections import defaultdict

from bson import ObjectId
from bson.errors import InvalidId
from werkzeug.exceptions import abort

from app import logger

UTC = datetime.timezone.utc

def get_object_id_from_str_or_404(id_str):
    try:
        object_id = ObjectId(id_str)
    except (InvalidId, TypeError):
        abort(404)
    return object_id


def get_utc_now():
    """Return a timezone-aware datetime object for current UTC time"""
    return datetime.datetime.now(UTC)


def get_truncated_string_from_byte_stream(byte_stream, bytes_to_get=200):
    truncated_bytes = [x for _, x in zip(range(bytes_to_get), byte_stream)]
    return reduce(lambda x, y: x + y, truncated_bytes)
