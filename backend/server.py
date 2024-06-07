from flask import Flask, request
from flask_cors import CORS
from dbcontroller import Database
import json

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:8080", "allow_headers": "Access-Control-Allow-Origin"}})


@app.route('/', methods=["GET"])
def main():
    return "Hello, world!"


@app.route('/data/requests', methods=["POST", "GET", "DELETE"])
def send_requests():
    if request.method == "POST":
        Database.write_data_in_database(json.loads(request.data), "request")
    db = Database()
    db.create_connect()
    data = db.send_sql_request("select * from requests")
    db.close()
    return Database.convert_data_in_json(data=data, type_data="requests")


@app.route('/data/delete/requests', methods=["POST"])
def delete_request():
    Database.delete_data_in_database(json.loads(request.data), type_data="requests")
    return "True"


@app.route('/data/services', methods=["POST", "GET"])
def send_services():
    db = Database()
    db.create_connect()
    data = db.send_sql_request("SELECT * FROM services")
    db.close()
    return Database.convert_data_in_json(data=data, type_data="services")


@app.route('/data/addictions', methods=["POST", "GET"])
def send_addictions():
    if request.method == "POST":
        Database.write_data_in_database(json.loads(request.data), "addiction")
    db = Database()
    db.create_connect()
    data = db.send_sql_request("select services.name_service, addictions.id_req from addictions, services where addictions.id_service = services.id_service;")
    db.close()
    return Database.convert_data_in_json(data=data, type_data="addictions")


if __name__ == '__main__':
    app.run(debug=True)