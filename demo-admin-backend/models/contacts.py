from mongoengine import StringField, URLField, BooleanField, queryset_manager, EmbeddedDocumentField, EmbeddedDocument, \
    EmbeddedDocumentListField

from models import TimestampedModel

class ContactModel(TimestampedModel):
    meta = {'collection': 'contacts'}
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    company_name = StringField()
    phone_number = StringField()
    deleted = BooleanField(default=False)

    @queryset_manager
    def objects(self, queryset):
        return queryset.filter(deleted=False)

    @queryset_manager
    def objects_including_deleted(self, queryset):
        return queryset