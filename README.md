# Flask FHIR API

This project is a Flask-based API that implements basic functionalities for managing patient data using FHIR (Fast Healthcare Interoperability Resources) principles. It allows users to perform basic CRUD (Create, Read, Update, Delete) operations on patient records. The API is built with Flask, SQLAlchemy for database management, and Flask-Migrate for database migrations.

## Features

- **GET** `/Patient/<id>`: Retrieve patient information by ID.
- **POST** `/Patient`: Create a new patient record.
- **PUT** `/Patient/<id>`: Update an existing patient's information.
- **DELETE** `/Patient/<id>`: Delete a patient record by ID.
- **Database Management**: Uses SQLite for database storage, SQLAlchemy for ORM, and Flask-Migrate for schema management.

## Setup and Installation

### Prerequisites

1. **Python 3.x**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv env-api
    ```

3. **Activate the Virtual Environment**:
    - On macOS/Linux:
      ```bash
      source env-api/bin/activate
      ```
    - On Windows:
      ```bash
      .\env-api\Scripts\activate
      ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Set Up the Database**:
    - Initialize the database and apply migrations with Flask-Migrate:
      ```bash
      flask db init
      flask db migrate -m "Initial migration"
      flask db upgrade
      ```

2. **Run the Application**:
    ```bash
    flask run
    ```
    The Flask server will start and be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### API Endpoints

- **GET** `/Patient/<id>`
    - **Description**: Retrieve patient information by their `id`.
    - **Response**:
      ```json
      {
          "id": 1,
          "name": "John Doe",
          "age": 30,
          "gender": "Male"
      }
      ```
    - **Status Codes**:
      - `200 OK`: Patient found.
      - `404 Not Found`: Patient not found.

- **POST** `/Patient`
    - **Description**: Create a new patient record.
    - **Request Body** (JSON):
      ```json
      {
          "id": 2,
          "name": "John Kasprowicz",
          "age": 27,
          "gender": "Male"
      }
      ```
    - **Response**:
      ```json
      {
          "id": 2,
          "name": "John Kasprowicz",
          "age": 27,
          "gender": "Male"
      }
      ```
    - **Status Codes**:
      - `201 Created`: Patient created successfully.
      - `400 Bad Request`: Missing required fields.

- **PUT** `/Patient/<id>`
    - **Description**: Update an existing patient's record.
    - **Request Body** (JSON):
      ```json
      {
          "name": "John Kasprowicz Updated",
          "age": 28,
          "gender": "Male"
      }
      ```
    - **Response**:
      ```json
      {
          "id": 2,
          "name": "John Kasprowicz Updated",
          "age": 28,
          "gender": "Male"
      }
      ```
    - **Status Codes**:
      - `200 OK`: Patient updated successfully.
      - `404 Not Found`: Patient not found.

- **DELETE** `/Patient/<id>`
    - **Description**: Delete a patient record by their `id`.
    - **Response**:
      ```json
      {
          "message": "Patient deleted successfully"
      }
      ```
    - **Status Codes**:
      - `200 OK`: Patient deleted successfully.
      - `404 Not Found`: Patient not found.

## Testing with Postman

You can use Postman to test the API endpoints:

1. **GET** `/Patient/<id>`: Retrieve patient information by providing a valid patient ID.
2. **POST** `/Patient`: Create a new patient by sending a `POST` request with patient data.
3. **PUT** `/Patient/<id>`: Update patient data by sending a `PUT` request with updated information.
4. **DELETE** `/Patient/<id>`: Delete a patient record by providing the patient ID.

Ensure that your Flask application is running when using Postman to make API requests.

## Flask Migrate

This project uses **Flask-Migrate** to manage database migrations. Here are the essential commands:

- **Initialize Migrations**:
    ```bash
    flask db init
    ```

- **Create Migration Files**:
    ```bash
    flask db migrate -m "Message describing migration"
    ```

- **Apply Migrations**:
    ```bash
    flask db upgrade
    ```

## Conclusion

This project serves as a simple implementation of a FHIR-based API for patient data management. It is a great starting point for learning about RESTful APIs, Flask, SQLAlchemy, Flask-Migrate, and FHIR standards in healthcare applications. 

Feel free to fork and modify the project for your own needs!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

