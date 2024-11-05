from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
import models
from database import get_database_connection

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("chochouse.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS majorcategory (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subcategory (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS variant (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  description TEXT,
  allergyid INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  quantity INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS composition (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  variantid INTEGER,
  ingredientid INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS offering (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  majorcatid INTEGER,
  subcatid INTEGER,
  variantid INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS allergy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS customer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  phone TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS custpreference (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  custid INTEGER,
  variantid TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS custallergy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  custid INTEGER,
  allergyid INTEGER
)''')



app = FastAPI()



#MAIN CATEGORY
# Route to add Main Category
@app.post("/maincategory")
async def main_category_add(name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO majorcategory (name) VALUES (?)"
    values = (name,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Main Category item added successfully"}

# Route to delete Main Category
@app.delete("/maincategory")
async def main_category_delete(id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM majorcategory WHERE majorcategory.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Main Category item deleted successfully"}

#Route to display Main Category
@app.get("/maincategory/",response_class=HTMLResponse)
async def main_category_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM majorcategory"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

##################################################   
#SUBCATEGORY
# Route to add Sub category
@app.post("/subcategory")
async def sub_category_add(name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO subcategory (name) VALUES (?)"
    values = (name,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Sub Category item created successfully"}

# Route to delete Sub Category
@app.delete("/subcategory")
async def sub_category_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM subcategory WHERE subcategory.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Sub Category item deleted successfully"}

#Route to display Main Category
@app.get("/subcategory")
async def sub_category_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM subcategory"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

##########################################################################

#CUSTOMER

# Route to add Customer
@app.post("/customer")
async def customer_add(name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO customer (name) VALUES (?)"
    values = (name,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer created successfully"}

# Route to delete Customer
@app.delete("/customer")
async def customer_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM customer WHERE customer.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer deleted successfully"}

#Route to display Customer
@app.get("/customer")
async def customer_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

##################################################################################

# Allergy
# Route to add Allergy
@app.post("/allergy")
async def allergy_add(name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO allergy (name) VALUES (?)"
    values = (name,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Allergy created successfully"}

# Route to delete Allergy
@app.delete("/allergy")
async def allergy_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM allergy WHERE allergy.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Allergy deleted successfully"}

#Route to display Allergy
@app.get("/allergy")
async def allergy_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM allergy"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

####################################################################

# INGREDIENTS
# Route to add Ingredient
@app.post("/ingredient")
async def ingredient_add(name: str,quantity: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO ingredient (name, quantity) VALUES (?, ?)"
    values = (name, quantity,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Ingredient added successfully"}

# Route to delete Ingredient
@app.delete("/ingredient")
async def ingredient_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM ingredient WHERE ingredient.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Ingredient deleted successfully"}

#Route to display Ingredient
@app.get("/ingredient")
async def ingredient_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM ingredient"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#Route to update Ingredient
@app.put("/ingredient")
async def ingredient_update(id: int, quantity: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE ingredient SET quantity = ? WHERE ingredient.id = ?"
    values = (quantity, id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Ingredient updated successfully"}

###############################################################################

# VARIANT
# Route to add Variant
@app.post("/variant")
async def variant_add(name: str,description: str,allergyid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO variant (name, description,allergyid) VALUES (?, ?, ?)"
    values = (name, description,allergyid,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Variant added successfully"}

# Route to delete Variant
@app.delete("/variant")
async def variant_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM variant WHERE variant.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Variant deleted successfully"}

#Route to display Variant
@app.get("/variant")
async def variant_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM variant v, allergy A WHERE V.allergyid = A.id"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#Route to update Variant
@app.put("/variant")
async def variant_update(id:int,name: str,description: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE variant SET name = ? and description = ? WHERE variant.id = ?"
    values = (name, description, id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Variant updated successfully"}

################################################################################################

# Composition
# Route to add Composition
@app.post("/composition")
async def composition_add(variantid:int,ingredientid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO composition (variantid,ingredientid) VALUES (?, ?)"
    values = (variantid,ingredientid,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Composition added successfully"}

# Route to delete Composition
@app.delete("/composition")
async def composition_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM composition WHERE composition.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Composition deleted successfully"}

#Route to display Composition
@app.get("/composition")
async def composition_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM composition C, Variant V, Ingredient I WHERE C.variantid = V.id AND C.ingredientid = I.id"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#Route to update Composition
@app.put("/composition")
async def composition_update(id:int,variantid:int,ingredientid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE composition SET variantid = ? and ingredientid = ? WHERE composition.id = ?"
    values = (variantid, ingredientid, id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Composition updated successfully"}

#################################################################################################

# Offering
# Route to add Offering
@app.post("/offering")
async def offering_add(majorcatid:int,subcatid:int,variantid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO offering (majorcatid,subcatid,variantid) VALUES (?, ?, ?)"
    values = (majorcatid,subcatid,variantid,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Offering added successfully"}

# Route to delete Offering
@app.delete("/offering")
async def offering_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM offering WHERE offering.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Offering deleted successfully"}

#Route to display Offering
@app.get("/offering")
async def offering_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM offering O, majorcategory M, subcategory S, variant V WHERE O.majorcatid = M.id AND O.subcatid = S.id AND O.variantid = V.id"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#######################################################################################

# CUSTOMER PREFERENCE
# Route to add custpref
@app.post("/custpreference")
async def custpreference_add(custid:int,variantid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO custpreference (custid,variantid) VALUES (?, ?)"
    values = (custid,variantid,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer Preference added successfully"}

# Route to delete custpref
@app.delete("/custpreference")
async def custpreference_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM custpreference WHERE custpreference.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer preference deleted successfully"}

#Route to display custpreference
@app.get("/custpreference")
async def custpreference_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM custpreference CP, customer C, variant V WHERE CP.custid = C.id AND CP.variantid = V.id"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

########################################################################################

# CUSTOMER ALLERGY

# Route to add custallergy
@app.post("/custallergy")
async def custallergy_add(custid:int,allergyid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO custallergy (custid,allergyid) VALUES (?, ?)"
    values = (custid,allergyid,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer Allergy added successfully"}

# Route to delete custallergy
@app.delete("/custallergy")
async def custallergy_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM custpreference WHERE custallergy.id = (?)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer allergy deleted successfully"}

#Route to display custallergy
@app.get("/custallergy")
async def custallergy_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM custpreference CP, customer C, allergy A WHERE CP.custid = C.id AND CP.allergyid = A.id"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

################################################################################################