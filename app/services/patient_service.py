from app.models.patient import Patient
from app import db

def get_patient_by_id(patient_id):
    return Patient.query.get(patient_id)


def create_patient(patient_data):
    patient = Patient(id=patient_data['id'], data=patient_data)
    db.session.add(patient)
    db.session.commit()

    return patient

