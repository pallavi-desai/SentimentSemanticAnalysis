import pymongo

user_name = "admin"
password = "password"
host_address = "@ec2-3-136-37-219.us-east-2.compute.amazonaws.com"

# connecting to mongodb using the credentials
try:
    mongodb_connection = pymongo.MongoClient("mongodb://" + user_name + ':' + password + host_address + ":27017/newdb")
except Exception as e:
    print(e)

database = mongodb_connection.newdb

movies_data = database['movies'].find({}, {'title': 1, 'genre': 1, 'plot': 1, 'ratings': 1, '_id': 0})

f = open("MovieDataFromMongodb.txt", "w")

for a in movies_data:
    f.write(str(a))
    f.write("\n")

f.close()