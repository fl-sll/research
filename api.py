from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import urllib.parse

app = FastAPI()

uri = "mongodb+srv://Visitor:researchgogogo@reseearch.a2rwr6l.mongodb.net/"

# Connect to MongoDB Atlas
client = MongoClient(uri)
db = client['research']

@app.get("/patterns/")
async def get_all_patterns():
    all_patterns = []
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        for document in collection.find({"patterns": {"$exists": True}}):
            patterns = document.get("patterns", [])
            all_patterns.extend(patterns)
    if all_patterns:
        return {"patterns": all_patterns}
    else:
        raise HTTPException(status_code=404, detail="No patterns found in the entire database")

@app.get("/responses/")
async def get_all_responses():
    all_responses = []
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        for document in collection.find({"responses": {"$exists": True}}):
            responses = document.get("responses", [])
            all_responses.extend(responses)
    if all_responses:
        return {"responses": all_responses}
    else:
        raise HTTPException(status_code=404, detail="No responses found in the entire database")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
