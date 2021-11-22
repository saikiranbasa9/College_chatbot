#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
from fastapi import FastAPI
if __name__=="__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb+srv://saikiran9298:<saikiran9298>@cluster0.bl0on.mongodb.net/college_chatbot?retryWrites=true&w=majority")
    db = client.test  
    print(client)
    
app = FastAPI()


# In[24]:


@app.route('/webhook',methods=["GET","POST"])
async def webhook():
    req=request.json(force=True)
    session=req["session"]
    query=req["queryResult"]["queryText"]
    result=req["queryResult"]["fulfillment"]
    data={"Query":query,
         "Result":result}
    mycol=mydb["session"]
    mycol.insert(data,check_keys=False)
    return 

