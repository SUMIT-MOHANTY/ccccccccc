import re
from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    """Marshmallow schema for User model validation"""

    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)

    @validates('email')
    def validate_email(self, value):
        """Validate email format using regex"""
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise ValidationError('Invalid email format')

    @validates('password')
    def validate_password(self, value):
        """Validate password length"""
        if len(value) < 8 or len(value) > 128:
            raise ValidationError('Password must be between 8 and 128 characters')

    class Meta:
        strict = True
