from pydantic import BaseModel
try:
    from pydantic import field_validator  # Pydantic v2
except ImportError:
    from pydantic import validator as field_validator  # Pydantic v1 fallback

class Configuration(BaseModel):
    """Configuration model for bank dashboard settings"""
    name: str
    value: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Name cannot be empty')
        return v.strip()

    @field_validator('value')
    @classmethod
    def validate_value(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Value cannot be empty')
        return v.strip()
