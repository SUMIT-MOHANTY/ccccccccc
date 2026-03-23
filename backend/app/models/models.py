from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class TestConfig(BaseModel):
    id: str = Field(default_factory=lambda: str(int(datetime.now().timestamp() * 1000)))
    name: str
    value: Optional[str] = None

    @field_validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Name cannot be empty')
        return v.strip()

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "test-config-1", "value": "sample-value"}
            ]
        }
    }

class ErrorResponse(BaseModel):
    detail: str
    status: int = 400

class SuccessResponse(BaseModel):
    success: bool = True
    data: dict
