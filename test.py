from flask import Flask,request
import pymongo

client = pymongo.MongoClient("mongodb+srv://saikiran9298:<saikiran9298>@cluster0.bl0on.mongodb.net/college_chatbot?retryWrites=true&w=majority")
db = client.test  
print(client)

app = Flask(__name__)
@app.route('/webhook', methods=["GET","POST"])
def webhook():
    req=request.json(force=True)
    session= req["sessions"]
    query= req["queryResult"]["queryText"]
    result= req["queryResult"]["fulfillmentText"]
    data= {"Query":query,
           "Result":result}
    mycol=mydb["session"]
    mycol.insert(data,check_keys=False)

if __name__ == '__main__':
    app.run()
    
