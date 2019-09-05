from pymongo import MongoClient
import pandas as pd

class MongoHandler():

    def insert_to_mongo(self):
        df = pd.read_csv('data/2011_summary.csv')

        myclient = MongoClient("mongodb://127.0.0.1:27017/")
        mydb = myclient.sandbox

        mydb.insert_many(df.to_dict('records'))