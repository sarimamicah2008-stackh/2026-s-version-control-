from fastapi import FastAPI

app = FastAPI()

menu = [
    {"name": "samosa",
     "category": "appetizer",
     "price": 1000,
     "vegetarian": "true"},
     {"name": "chicken wings",
      "category": "appetizer",
      "price": 2000,
      "vegetarian": "false"},
      { "name": "spring rolls",
       "category": "appetizer",
       "price": 1500,
       "vegetarian": "true"},
       {"name": "puff puff",
        "category": "appetizer",
        "price": 1000,
        "vegetarian": "true"},
        {"name": "jollof rice",
         "category": "main-course",
         "price": 1600,
         "vegetarian": "false"},
        {"name": "coconut rice",
         "category": "main-course",
         "price": 1600,
         "vegetarian": "false"},
         {"name": "fried rice",
          "category": "main-course",
          "price": 1600,
          "vegetarian": "false"},
          {"name": "creamy pasta",
           "category": "main-course",
           "price": 1700,
           "vegetarian": "true"},
           {"name": "egusi soup",
            "category": "main-course",
            "price": 2000,
            "vegetarian": "false"},
            {"name": "banana bread",
             "category": "dessert",
             "price": 1000,
             "vegetarian": "true"},
             {"name": "caramel icecream",
              "category": "dessert",
              "price": 1300,
              "vegetarian": "true"},
              {"name": "red velvet cookies",
               "category": "dessert",
               "price": 1200,
               "vegetarian": "true"},
]

@app.get("/menu")
def get_menu():
    return menu

@app.get("/appetizers")
def get_appetizers():
    return [item for item in menu if item["category"] == "appetizer"]

@app.get("/main-courses")
def get_main_courses():
    return[item for item in menu if item["category"] == "main-course"]

@app.get("/desserts")
def get_desserts():
    return[item for item in menu if item["category"] == "dessert"]

@app.get("/item/{item_name}")
def get_item(item_name: str):
    for item in menu:
        if item["name"].lower() == item_name.lower():
                              return item
                              return {"message": "item not found"}

@app.get("/category/{category_name}")
def get_category(category_name: str):
       return [item for item in menu if item["category"].lower() == category_name.lower()]

@app.get("/price/{item_name}")
def get_price(item_name: str):
       for item in menu:
              if item["name"].lower() == item_name.lower():
                     return {"name": item["name"], "price":
                             item["price"]}
                     return {"message": "item not found"}

@app.get("/vegetarian-options")
def get_vegetarian_options():
       return [item for item in menu if item["veetarian"]]

@app.get("/total-items")
def get_total_items():
       return max(menu, key=lambda
                  item: item["price"])

@app.get("/total-items")
def get_total_items():
       return {"total_items": len(menu)}