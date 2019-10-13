from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://mwangiKibui:mwangiKibui@karuconnect-kcamz.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('group_tasks')
optns = db.mongo_crud


#count docs
docs = optns.count_documents({})
#print(f'hello you have {docs} documents')

#inserting doc
#only one
new_car = {
    'name':'MarkX',
    'make':'Toyota',
    'year of manufacture':'2010'
}
#optns.insert_one(new_car)
#inserting many
cars = [
    {
        'name': 'Vitz',
        'make': 'Toyota',
        'year of manufacture': '2013'
    },
    {
        'name': 'Impreza',
        'make': 'Subaru',
        'year of manufacture': '2015'
    }
]
#optns.insert_many(cars)

#Find docs----.find() shall return a cursor
cars = list(optns.find())

#finding one document
car = optns.find_one({'make':'Subaru'})

#updating documents
updated_car = {
    'name':'nice impreza'
}
optns.update_one({'make':'Subaru'},{'$set':updated_car})
#update_many shall update all of them

#deleting documents
car_to_delete = {
    'make':'Subaru'
}
optns.delete_one(car_to_delete)
#record shall be deleted