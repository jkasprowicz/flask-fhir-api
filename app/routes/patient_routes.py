from flask import Blueprint, jsonify, request
from app.models.patient import Patient
from app import db


patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/Patient/<id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get(id)

    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    return jsonify(patient.data)


@patient_bp.route('/Patient', methods=['POST'])
def create_patient():
    patient_data = request.json

    patient = Patient(id=patient_data['id'], data=patient_data)

    db.session.add(patient)
    db.session.commit()

    return jsonify(patient_data), 201


@patient_bp.route('/Patient/<id>', methods=['PUT'])
def update_patient(id):
    patient = Patient.query.get(id)

    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    patient_data = request.json
    patient_data = patient_data
    db.session.commit()

    return jsonify(patient.data)


@patient_bp.route('/Patient/<id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(id)

    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    db.session.delete(patient)
    db.session.commit

    return jsonify({"message": "Patient delete successfully"}), 200

