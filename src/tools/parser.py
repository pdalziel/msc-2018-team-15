import pymongo
import json

from bson import ObjectId
from pymongo import MongoClient


# gh_pullrequemments


def connect_to_db(conn_str=None, db_port=None):
    client = MongoClient(conn_str, db_port)
    db = client.github
    return db

def get_raw_json():
    pass



def filter_lang():
    pass


def extract_meta_data():
    pass



def process_raw_text():
    pass


def analyse_sentiment():
    pass


def main():
    conn_str = 'localhost'
    db_port = 27017
    db = connect_to_db(conn_str, db_port)
    collection = db.pull_requests
    #print(collection.count_documents({}))
    document = collection.find_one({'_id': ObjectId('560f1ad71b48761186002a2b')})
    print(document)




if __name__ == "__main__":
    main()
