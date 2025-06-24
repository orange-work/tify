from flask_restful import fields

business_line_fields = {
    "id": fields.String,
    "name": fields.String,
}

# marshal_with expects a mapping of fields. Wrap the list in a dict so
# marshal_with can properly iterate over the mapping and serialize the list.
business_line_list_fields = {
    "business_lines": fields.List(fields.Nested(business_line_fields))
}
