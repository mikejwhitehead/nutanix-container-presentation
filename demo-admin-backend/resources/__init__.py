import re

from bson import Regex
from marshmallow import Schema, fields, validates_schema, ValidationError

from exceptions.demoadmin_validation_exception import DemoAdminValidationException
from utils import get_utc_now


def update_model_with_new_values(validated_data, model):
    for key, value in validated_data.items():
        model[key] = value
    model.last_modified = get_utc_now()
    model.save()


def format_pagination_response(limit, offset, total_count, object_list_key, object_list):
    return {
        object_list_key: object_list,
        "pagination": {
            "limit": limit,
            "offset": offset,
            "total": total_count
        }
    }


def gen_regex_search_query(search_query):
    # TODO sanitize this user input before querying the DB with it
    pattern = re.compile(search_query)
    regex = Regex.from_native(pattern)
    regex.flags ^= re.UNICODE
    regex.flags ^= re.IGNORECASE
    return regex


class AbstractSchema(Schema):
    class Meta:
        strict = True

    id = fields.Str(dump_only=True)
    last_modified = fields.DateTime(dump_only=True)
    created = fields.DateTime(dump_only=True)

    def handle_error(self, exc, data):
        """Raise our custom exception when (de)serialization fails."""
        raise DemoAdminValidationException(exc.messages)

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        for key in original_data:
            if key not in self.fields:
                raise ValidationError('Unknown field name', key)