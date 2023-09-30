from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")

dbs = client.list_database_names()

test_db = client.test
collection = test_db.list_collection_names()

production = client.production
person_collection = production.person_collection

def create_documents():
    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen"]
    last_names = ["Ruscica", "Smith", "Bart", "Cater", "Pit", "Geral"]
    ages = [21, 40, 23, 19, 34, 67]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name" : first_name, "last_name" : last_name, "age": age}

        docs.append(doc)

    person_collection.insert_many(docs)


def find_all_people():
    people = person_collection.find()

    for person in people:
        print(person)


def find_by_field():
    person = person_collection.find_one({"first_name": "Tim"})
    print(person)

def find_all_people():
    count = person_collection.count_documents(filter={})
    print(count)

def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)

    person = person_collection.find_one({"_id" : _id})

    print(person)


def get_age_range(min_age, max_age):
    query = {"$and" : [
            {"age": {"$gte": min_age}},
            {"age": {"$lte": max_age}}
        ]}


    people = person_collection.find(query).sort("age")

    for person in people:
        print(person)

def project_columns():
    columns = {"_id": 0, "first_name" : 1, "last_name": 1}
    people = person_collection.find({}, columns)

    for person in people:
        print(person)
project_columns()