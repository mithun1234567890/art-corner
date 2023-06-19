from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(max=1000, required=True)
    password = fields.Str(validate=validate.Length(max=500), required=True, load_only=True)
