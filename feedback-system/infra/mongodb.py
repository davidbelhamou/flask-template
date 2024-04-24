from pymongo import MongoClient
from typing import List
from config import config


class MongoDB:

    def __init__(self, env='dev', port=1111):
        self.client = None
        self.env = env
        self.conf = config.get_config(self.env)
        self.uri = self.conf['uri']
        self.port = self.conf['port']
        self.db_name = self.conf['database']

    def initialize(self):
        self.client = MongoClient(self.uri)
        return self.client

    def connect(self):
        try:
            if not self.client:
                self.initialize()
                self.db = self.client[self.db_name]

        except Exception as ex:
            print(f"Failed to connect, {ex}")

    def add_one(self, collection, doc, get_id=False):
        try:
            if not self.client:
                self.connect()
            if get_id:
                return self.db[collection].insert_one(doc).inserted_id
            self.db[collection].insert_one(doc)
        except Exception as ex:
            print("Failed...")

    def insert_bulk(self, collection, list_):
        try:
            if not self.client:
                self.connect()
            res = self.db[collection].insert_many(list_, ordered=False)
            res.inserted_ids
        except Exception:
            raise Exception('Failed inserting many')

    def find_document(self, collection, query):
        ...

    def count_documents(self, collection):
        if not self.client:
            self.connect()
        return self.db[collection].count_documents({})

    def delete_document(self, collection, query):
        if not self.client:
            self.connect()
        self.db[collection].delete_one(query)

    def find(self, collection, query):
        if not self.client:
            self.connect()
        cursor = self.db[collection].find(query)
        return [ele for ele in cursor]


