import pymongo
import json
import pprint
import time

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
    pull_requests = db.pull_requests
    comments = db.pull_request_comments
    # print(collection.count_documents({}))
    #document = pull_requests.find({'_id': ObjectId('55c4fae51b48764f1d000011')})
    cursor = comments.find({}).limit(2)

    #print(document2.keys())
    #rint(document.keys())
    docs = []


    start = time.asctime(time.localtime(time.time()))
    for pr in cursor:
        pprint.pprint(cursor)
        for doc in pull_requests.find({'id': pr.get('pullreq_id')}):
            print(doc)
            docs.append(doc)

    end = time.asctime(time.localtime(time.time()))
    print(start + " : " + end)
    with open('docs_file.txt', 'w') as f:
        for item in docs:
            f.write("%s\n" % item)






if __name__ == "__main__":
    main()
