# from main import FastAPI

# # Create an instance of FastAPI
# app = FastAPI()

# # Sample data for demonstration
# weather_data = {
#     "London": {"temperature": 15, "condition": "Cloudy"},
#     "New York": {"temperature": 22, "condition": "Sunny"},
#     "Tokyo": {"temperature": 18, "condition": "Rainy"}
# }

# # Define a route to fetch weather data
# @app.get("/weather")
# def get_weather(city: str):
#     """
#     Fetches weather data for a given city.
#     Args:
#         city (str): The name of the city.
#     Returns:
#         dict: Weather details for the city or an error message.
#     """
#     if city in weather_data:
#         return {
#             "city": city,
#             "temperature": weather_data[city]["temperature"],
#             "condition": weather_data[city]["condition"]
#         }
#     else:
#         return {"error": "City not found"}

# # Run the server using: uvicorn filename:app --reload
import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def index():
return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name):
return {"name": name}