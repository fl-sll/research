from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import urllib.parse

app = FastAPI()

uri = "mongodb+srv://Visitor:researchgogogo@reseearch.a2rwr6l.mongodb.net/"

# Connect to MongoDB Atlas
client = MongoClient(uri)
db = client['research']
collection = db['data']

class PatternResponse(BaseModel):
    patterns: list[str]
    responses: list[str]

class TagCreate(BaseModel):
    tag: str
    data: PatternResponse


@app.get("/patterns/")
async def get_all_patterns():
    try:
        patterns = collection.distinct("patterns")
        return patterns
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

@app.get("/tags/")
async def get_all_tags():
    try:
        tags = collection.distinct("tag")
        return tags
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)


@app.get("/responses/")
async def get_all_responses():
    try:
        responses = collection.distinct("responses")
        return responses
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
