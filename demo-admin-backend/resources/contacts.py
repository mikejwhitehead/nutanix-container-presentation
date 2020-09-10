from flask_restful import Resource
import secrets
import json

from marshmallow import fields, validate, post_load
from werkzeug.exceptions import abort

from models.contacts import ContactModel
from resources import AbstractSchema, update_model_with_new_values, gen_regex_search_query, format_pagination_response
from utils import get_utc_now
from flask import request, url_for
from ast import literal_eval
from app import logger

class ContactSchema(AbstractSchema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    company_name = fields.Str()
    phone_number = fields.Str()


contact_schema = ContactSchema()

class Contact(Resource):
    def get(self, id_str):
        model = ContactModel.objects(id=id_str).get_or_404()

        return contact_schema.dump(model).data

    def delete(self, id_str):
        model = ContactModel.objects(id=id_str).get_or_404()
        model.deleted = True
        model.save()

        return None, 204

    def put(self, id_str):
        model = ContactModel.objects(id=id_str).get_or_404()
        validated_data = contact_schema.load(request.get_json()).data
        update_model_with_new_values(validated_data, model)

        return contact_schema.dump(model).data

class Contacts(Resource):
    def post(self):
        validated_data = contact_schema.load(request.get_json()).data

        model = ContactModel(**validated_data)
        now = get_utc_now()
        model.created = now
        model.last_modified = now
        model.save()

        return contact_schema.dump(model).data, 201

    def get(self):
        search_query = request.args.get("search", "")
        limit = int(request.args.get("limit", 10))
        offset = int(request.args.get("offset", 0))

        query_set = ContactModel.objects(__raw__={'last_name': gen_regex_search_query(search_query)})

        total_count = query_set.count()
        models = query_set.skip(offset).limit(limit)

        return format_pagination_response(limit, offset, total_count, "contacts",
                                          contact_schema.dump(models, many=True).data)

