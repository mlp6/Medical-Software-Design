from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import os
import uuid

app = Flask(__name__)
engine = create_engine("postgresql://postgres:{0}@db:5432/postgres".format(os.environ.get("POSTGRES_PASSWORD")), max_overflow=20)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    uuid=Column(UUID, primary_key=True)
    first_name=Column("first_name", String(32))
    last_name=Column("last_name", String(32))
    netid=Column("netid", String(10)) 
    github_username=Column("github_username", String(32))

    def __init__(self, uuid, first_name, last_name, netid, github_username):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.netid = netid 
        self.github_username = github_username
    
    def as_dict(self):
        return {
            "uuid": self.uuid,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "netid": self.netid, 
            "github_username": self.github_username
        }

Base.metadata.create_all(engine)

REQUIRED_REQUEST_KEYS = [
    "first_name",
    "last_name",
    "netid", 
    "github_username"
]

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

def validate_new_student_request(req):
    for key in REQUIRED_REQUEST_KEYS:
        if key not in req.keys():
            raise ValidationError("Key '{0}' not present in request".format(key))

@app.route("/", methods=['GET'])
def hello():
    return (
        """
        Welcome to the BME590 class test server.
        """
    )

@app.route("/list", methods=['GET'])
def list():
    session = Session()
    students = session.query(Student).all()
    dict_array = [student.as_dict() for student in students]
    return jsonify(dict_array)

@app.route("/student", methods=['POST'])
def add_student():
    r = request.get_json() # Parses input request data as json
    try:
        validate_new_student_request(r)
    except ValidationError as inst:
        return jsonify({"message": inst.message}), 500

    session = Session()
    s = Student(
        uuid=str(uuid.uuid4()), 
        first_name=r['first_name'], 
        last_name=r['last_name'], 
        netid=r['netid'], 
        github_username=r['github_username'])

    session.add(s)
    result = {
        "message": "Added user {0} successfully to the class list".format(request.json["first_name"]),
        "created_user_uuid": s.uuid
    }
    session.commit()
    session.close()

    return jsonify(result) 

@app.route("/sum", methods=['POST'])
def sum():
    r = request.get_json()
    try:
        s = r['a'] + r['b']
    except:
        return jsonify({"message": "Error occurred, check your inputs"}), 500

    return jsonify({"result": s})
