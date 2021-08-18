from pymongo import  MongoClient
from datetime import datetime
client = MongoClient()  

db= client.dbrestaurants                

Restaurant = db.list_collection_names()         
print(Restaurant)


#Q1
# for doc in db.restaurant.find():
#   print(doc)

#Q2
# for doc in db.restaurant.find(projection={"restaurant_id": True, "name": True, "borough": True, "cuisine": True}):
#   print(doc)

#Q3
# for doc in db.restaurant.find(projection={"restaurant_id": True, "name": True, "borough": True, "cuisine": True, "_id": False}):
#   print(doc)

# Q4
# for doc in db.restaurant.find(projection={"restaurant_id": True, "name": True, "address.zipcode": True, "cuisine": True}):
#   print(doc)

#Q5
# for doc in db.restaurant.find({"borough": "Bronx"}):
#   print(doc)

#Q6
#for doc in db.restaurant.find({"borough": "Bronx"},limit=5):
#  print(doc)

# for doc in db.restaurant.find({"borough": "Bronx"})[0:2]:
#     print(doc)

#Q7 
# print("**********************")
# for doc in db.restaurant.find({"borough": "Bronx"},skip=5,limit=5):
#     print(doc)

#Q8
# for doc in db.restaurant.find({"grades.score" :{"$gt": 90}}):
#    print(doc)

#Q9
# for doc in db.restaurant.find({"grades.score" :{"$gt": 80,"$lt":100}}):
#     print(doc)

#10
# for doc in db.restaurant.find({"address.coord" :{"$lt": -95.754168 }}):
#      print(doc)

#Q11
# for doc in db.restaurant.find({"$and":[{'cuisine':{"$ne":'American '}, 'grades.score':{"$gt":70}, 'address.coord':{'$lt':-65.754168}}]}):
#   print(doc)

#Q12
# for doc in db.restaurant.find({'cuisine':{"$ne": 'American '}, 'grades.score':{"$gt":70},'address.coord':{"$lt":-65.754168}}):
#   print(doc)

#Q13
# from pymongo import  ASCENDING, DESCENDING
# for doc in db.restaurant.find({"$and":[{ 'cuisine': {"$ne": 'American '}, 'grades.grade':'A', 'borough':{"$ne": 'Brooklyn'}}]}).sort([('cuisine', DESCENDING)]):
#   print(doc)

#Q14 
# for doc in db.restaurant.find({"name":{"$regex" : '^Wil'}},projection= { "restaurant_id" : True, "name": True,"borough":True, "cuisine" :True}):
#     print(doc)

#Q15
# for doc in db.restaurant.find({"name":{"$regex" : 'ces$'}},projection= { "restaurant_id" : True, "name": True,"borough":True, "cuisine" :True}):
#    print(doc)

#Q16
# for doc in db.restaurant.find({"name":{"$regex" : '.*Reg.*'}},projection= { "restaurant_id" : True, "name": True,"borough":True, "cuisine" :True}):
#    print(doc)

#Q17
# for doc in db.restaurant.find( { "borough": "Bronx", "$or": [{"cuisine": "American "},{"cuisine": "Chinese"}]}):
#   print(doc)

#Q18
# for doc in db.restaurant.find({"$or": [{"borough": "Staten Island"},{"borough": "Queens"},{"borough": "Bronxor"},{"borough": "Brooklyn"}]},{"restaurant_id" : 1, "name" : 1, "borough": 1, "cuisine": 1}):
#   print(doc)

#Q19
# for doc in db.restaurant.find( {"borough" :{"$nin" :["Staten Island","Queens","Bronx","Brooklyn"]}}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 }):
#   print(doc)

#Q20
#for doc in db.restaurant.find({"grades.score":{"$lte":10}},{"restaurant_id" : 1, "name" : 1, "borough": 1, "cuisine": 1}):
#   print(doc)

#Q21
# for doc in db.restaurant.find({"$or": [{"name":{"$regex" :'^Wil'}},{"$and": [{"cuisine" : {"$ne" :"American "}},{"cuisine" : {"$ne" :"Chinese"}}]}]},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}):
#     print(doc)

#Q22
# for doc in db.restaurant.find({"grades": {"$elemMatch":{'date':datetime.fromisoformat('2014-08-11T00:00:00'),"grade":"A" ,"score" : 11}}},{"restaurant_id" : 1,"name":1,"grades":1}):
#     print(doc) not working properly

#Q23
# for doc in db.restaurant.find({"grades": {"$elemMatch":{'date':datetime.fromisoformat('2014-08-11T00:00:00')}},"grade":"A" ,"1.score" : 9},{"restaurant_id" : 1,"name":1,"grades":1}):
#     print(doc)  # not working


#Q24
# for doc in db.restaurant.find({"address.coord.1": {"$gt" : 42, "$lte" : 52}},{"restaurant_id" : 1,"name":1,"address":1,"coord":1}):
#     print(doc)

#Q25
# from pymongo import  ASCENDING, DESCENDING
# for i in db.restaurant.find({}).sort([("name",ASCENDING)]):
#     print(i)

#Q26
# from pymongo import  ASCENDING, DESCENDING
# for i in db.restaurant.find({}).sort([("name",DESCENDING)]):
#     print(i)

#Q27
# from pymongo import  ASCENDING, DESCENDING
# for doc in db.restaurant.find({}).sort([("cuisine",ASCENDING),("borough",DESCENDING)]):
#     print(doc)

#Q28
# for doc in db.restaurant.find({"address.street": {"$exists": True}}):
#     print(doc)

#Q29
# for doc in db.restaurant.find({"address.coord" :{"$type" : "double"}}):
#     print(doc)


#Q30
# for i in db.restaurant.find({"grades.score": {"$mod": [7,0]}},{"restaurant_id": 1, "name": 1, "grades": 1}):
#     print(i)

#Q31
# for doc in db.restaurant.find({"name": {"$regex" :".*mon.*"}},{"name": 1, "borough": 1, "address.coord": 1,"cuisine": 1}):
#     print(doc)


#Q32
# for doc in db.restaurant.find({"name":{"$regex":"^Mad"}},{"name": True, "borough":True,"address.coord": True, "cuisine": True}):
#     print(doc)