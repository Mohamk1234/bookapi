from pickle import FALSE
from flask import Flask, Response, request
import db
import json
import datetime
from datetime import date
from bson.objectid import ObjectId


app = Flask(__name__)

@app.route("/booklist/bookname/<name>", methods=['GET'])
def get_by_name(name):

    books = list(db.db.booklist.find({
        "book_name":{
            "$regex":".*"+name+".*",
            "$options":"i"
            }
        },
        {"book_name":1,"_id":0}
        ))

    return Response(
        response = json.dumps(books),
        status=200,
        mimetype="application/json")

@app.route("/booklist/rent/", methods=["GET"])
def get_by_rate():
    lower = int(request.args.get("lower"))
    upper = int(request.args.get("upper"))
    books = list(db.db.booklist.find({
        "$and":[
            {
            "rent":{"$gt":lower}
            },
            {"rent":{"$lt":upper}}
            ]
            },
             {"book_name":1,"_id":0}
            ))

    return Response(
        response = json.dumps(books),
        status=200,
        mimetype="application/json")

@app.route("/booklist/custom/", methods=["GET"])
def get_by_multiple_arguments():
    name = request.args.get("name")
    category = request.args.get("category")
    lower = int(request.args.get("lower"))
    upper = int(request.args.get("upper"))
    if(name is None or category is None or lower is None or upper is None):
        return "Invalid Request Format"
    books = list(db.db.booklist.find(
        {"$and":[{"rent":{"$gt":lower}},{"rent":{"$lt":upper}},
    {"book_name":{"$regex":".*"+name+".*","$options":"i"}},
    {"category":{"$regex":".*"+category+".*","$options":"i"}}
    ]},
     {"book_name":1,"_id":0}
     ))
    
    return Response(
        response = json.dumps(books),
        status=200,
        mimetype="application/json")




@app.route("/transactions/bookissue/", methods=["POST"])
def add_book_issue():
    issue = request.get_json()
    date = datetime.datetime.now()
    db.db.transactions.insert_one(
        {
            "book_name":issue['book_name'],
            "person_name":issue['person_name'],
            "date_issued":date
            })
    return "successfully Issued"

@app.route("/transactions/bookreturn/", methods=["POST"])
def add_book_return():
    issue = request.get_json()
    today = datetime.datetime.now()
    rent_per_day = db.db.booklist.find_one(
        {
            "book_name":{
                "$regex":".*"+issue['book_name']+".*","$options":"i"
                }},{"rent":1,"_id":0})
    issue_date = db.db.transactions.find_one(
        {"$and":[{
            "book_name":
            {"$regex":".*"+issue['book_name']+".*",
            "$options":"i"
            }}, 
    {"person_name":issue['person_name']}
    ]})
    rent = rent_per_day['rent'] * ((today-issue_date['date_issued']).days+1)
    print(rent)
    db.db.transactions.update_one({"$and":[{"book_name":{"$regex":".*"+issue['book_name']+".*","$options":"i"}}, 
    {"person_name":issue['person_name']}
    ]}, {"$set":{"date_returned": today, "rent": rent}})
    
    return "successfully Returned"



@app.route("/transactions/person/<name>", methods=["GET"])
def list_of_books_issued(name):
    books = db.db.transactions.distinct("book_name",{"person_name": name})

    return Response(
        response = json.dumps(books),
        status=200,
        mimetype="application/json"
    )

@app.route("/transactions/generatedrent/<name>", methods=["GET"])
def rentgenerated(name):
    rent = list(db.db.transactions.aggregate([
        {
            "$match":{"book_name":name}
        },
        {
            "$group":{
                "_id":"$book_name",
                "totalrent":{"$sum":"$rent"}
            }
        }
    ]))
 
    return Response(
        response = json.dumps(rent),
        status=200,
        mimetype="application/json")

@app.route("/transactions/listofpeople/<name>", methods=["GET"])
def listofpeople(name):
    totalcount = list(db.db.transactions.aggregate([
        {
            "$match":{"book_name":name}
        },
        {
            "$group":{
                "_id":"$person_name",
            }
        }
    ]))
    currentlyissuedcount = list(db.db.transactions.aggregate([
        {
            "$match":{"book_name":name,"rent":{"$exists":False}}
        },
        {
            "$group":{
                "_id":"$person_name",
            }
        }
    ]))
    
    return Response(
        response = json.dumps(
            [
                ['total', totalcount],
                ['currentlyissued', currentlyissuedcount]
            ]
            ),
        status=200,
        mimetype="application/json")

@app.route("/transactions/daterange/",methods=["GET"])
def issued_in_date_range():
    lower = datetime.datetime.strptime(request.args.get("lower"), '%d/%m/%y')
    upper = datetime.datetime.strptime(request.args.get("upper"), '%d/%m/%y')
    books = list(db.db.transactions.find(
        {
            "$and":[
                {
                "date_issued":{"$lt":upper}
                },
                {
                "date_issued":{"$gt":lower}
                }
            ]
        },
        {
            "book_name":1,
            "person_name":1
        }
    ))
   
    for book in books:
        book["_id"]= str(book["_id"])
    return Response(
        response = json.dumps(books),
        status=200,
        mimetype="application/json")


if __name__ == "__main__":
    app.run(port=8000, debug=True)