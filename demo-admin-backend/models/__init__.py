import datetime
from flask_mongoengine import Document
from mongoengine import ComplexDateTimeField


class UtcComplexDateTimeField(ComplexDateTimeField):
    """ComplexDateTimeField that is assumed to always be in UTC"""
    def _convert_from_string(self, data):
        value = super(UtcComplexDateTimeField, self)._convert_from_string(data)
        return value.replace(tzinfo=datetime.timezone.utc)


class BaseModel(Document):
    meta = {'abstract': True}

    def delete(self, signal_kwargs=None, **write_concern):
        raise Exception("Should not be able to actually delete objects. Do a soft delete.")


class TimestampedModel(BaseModel):
    meta = {'abstract': True}

    last_modified = UtcComplexDateTimeField(required=True)
    created = UtcComplexDateTimeField(required=True)
