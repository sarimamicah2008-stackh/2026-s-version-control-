from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def home():
    return "welocme to my API"

@app.get("/about")
def about():
    return {
        "name": "Sarima",
        "age": 18,
        "city": "Port-Harcourt"
    }

@app.get("/hobbies")
def hobbies():
    return [
        "reading",
        "drawing",
        "sleeping",
        "listening to music",
        "coding"
    ]

@app.get("/skills")
def skills():
    return {
        "python": "beginner",
        "FastAPI": "beginner",
        "writting": "intermidiate",
        "drawing": "advanced"
    }
@app.get("/favorite-food")
def favorite_food():
    return {
        "name": "Bole",
        "origin": "Port-Harcourt",
        "spicy": "true"
    }
