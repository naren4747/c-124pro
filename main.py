from flask import Flask,jsonify,request

app=Flask(__name__)

Contact=[
    {
        "id":1,
        "Name":u"office",
        "number":u"9057293463",
        "done":False
    },
    {
        "id":2,
        "Name":u"home",
        "number":u"4956239571",
        "done":False
    }
]

@app.route("/add-data",methods=["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data of the contact"
        },400)

    newContact={
        "id":Contact[-1]["id"]+1,
        "Name":request.json["Name"],
        "description":request.json.get("number",""),
        "done":False
    }

    Contact.append(newContact)

    return jsonify({
        "status":"succes",
        "messge":"contact added succes"
    })

@app.route("/get-data")

def getTask():
    return jsonify({
        "data":Contact
    })

if(__name__=="__main__"):
    app.run(debug=True)