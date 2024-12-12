from pydantic import BaseModel, ValidationError

class PatientModel(BaseModel):
    id: str
    resourceType: str
    name: list
    gender: str
    birthDate: str


def validate_patient(data):
    try:
        return PatientModel(**data)
    except ValidationError as e:
        raise ValueError(e.json())