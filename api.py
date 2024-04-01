from bson import ObjectId
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

class PatternModel(BaseModel):
    pattern: str

class ResponseModel(BaseModel):
    response: str
    
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

@app.post("/patterns/")
async def create_pattern(pattern: PatternModel):
    try:
        # Insert the pattern into MongoDB
        result = collection.insert_one({"pattern": pattern.pattern})
        # Return the inserted pattern
        return JSONResponse(content={"message": "Pattern created successfully", "id": str(result.inserted_id)}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

@app.put("/patterns/{pattern_id}")
async def update_pattern(pattern_id: str, pattern: PatternModel):
    try:
        # Update the pattern in MongoDB
        result = collection.update_one({"_id": ObjectId(pattern_id)}, {"$set": {"pattern": pattern.pattern}})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Pattern not found")
        # Return success message
        return JSONResponse(content={"message": "Pattern updated successfully"})
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

@app.delete("/patterns/{pattern_id}")
async def delete_pattern(pattern_id: str):
    try:
        # Delete the pattern from MongoDB
        result = collection.delete_one({"_id": ObjectId(pattern_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Pattern not found")
        # Return success message
        return JSONResponse(content={"message": "Pattern deleted successfully"})
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
    
@app.post("/responses/")
async def create_response(response: ResponseModel):
    try:
        # Insert the response into MongoDB
        result = collection.insert_one({"response": response.response})
        # Return the inserted response
        return JSONResponse(content={"message": "Response created successfully", "id": str(result.inserted_id)}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

@app.put("/responses/{response_id}")
async def update_response(response_id: str, response: ResponseModel):
    try:
        # Update the response in MongoDB
        result = collection.update_one({"_id": ObjectId(response_id)}, {"$set": {"response": response.response}})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Response not found")
        # Return success message
        return JSONResponse(content={"message": "Response updated successfully"})
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

@app.delete("/responses/{response_id}")
async def delete_response(response_id: str):
    try:
        # Delete the response from MongoDB
        result = collection.delete_one({"_id": ObjectId(response_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Response not found")
        # Return success message
        return JSONResponse(content={"message": "Response deleted successfully"})
    except Exception as e:
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
