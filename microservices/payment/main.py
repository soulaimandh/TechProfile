from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/retrieve-sample-data")
async def retrieve_sample_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/api/sample-data/")
        dict1 = {'source': "I'm payment service"}
        sample_data = response.json()
        merged_dict = {**dict1, **sample_data}
        return merged_dict
