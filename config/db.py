from pymongo import MongoClient

uri = 'mongodb+srv://samose96:Santiago147258@cluster0.qjhrn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

conn = MongoClient(uri)
db = conn.myFirstDatabase

