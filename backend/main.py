from fastapi import FastAPI
import models
from database import get_database_connection

app = FastAPI()

#MAIN CATEGORY
# Route to add Main Category
@app.post("/maincategory")
async def main_category_add(id:int,name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO majorcategory (id, name) VALUES (%s, %s)"
    values = (id, name)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Main Category item created successfully"}

# Route to delete Main Category
@app.delete("/maincategory")
async def main_category_delete(id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM majorcategory WHERE majorcategory.id = (%s)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Main Category item deleted successfully"}

#Route to display Main Category
@app.get("/maincategory")
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
async def sub_category_add(id:int,name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO subcategory (id, name) VALUES (%s, %s)"
    values = (id, name)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Sub Category item created successfully"}

# Route to delete Sub Category
@app.delete("/subcategory")
async def sub_category_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM subcategory WHERE subcategory.id = (%s)"
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
async def customer_add(id:int,name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO customer (id, name) VALUES (%s, %s)"
    values = (id, name)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer created successfully"}

# Route to delete Customer
@app.delete("/customer")
async def customer_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM customer WHERE cutomer.id = (%s)"
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
async def allergy_add(id:int,name: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO allergy (id, name) VALUES (%s, %s)"
    values = (id,name)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Allergy created successfully"}

# Route to delete Allergy
@app.delete("/allergy")
async def allergy_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM allergy WHERE allergy.id = (%s)"
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
async def ingredient_add(id:int,name: str,quantity: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO ingredient (id, name, quantity) VALUES (%s, %s, %s)"
    values = (id, name, quantity)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Ingredient added successfully"}

# Route to delete Ingredient
@app.delete("/ingredient")
async def ingredient_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM ingredient WHERE ingredient.id = (%s)"
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
    query = "UPDATE ingredient SET quantity = %s WHERE id = %s"
    values = (quantity, id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Ingredient updated successfully"}

###############################################################################

# VARIANT
# Route to add Variant
@app.post("/variant")
async def variant_add(id:int,name: str,description: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO variant (id, name, description) VALUES (%s, %s, %s)"
    values = (id, name, description)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Variant added successfully"}

# Route to delete Variant
@app.delete("/variant")
async def variant_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM variant WHERE variant.id = (%s)"
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
    query = "SELECT * FROM variant"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#Route to update Variant
@app.put("/variant")
async def variant_update(id:int,name: str,description: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE variant SET name = %s and description = %s WHERE id = %s"
    values = (name, description, id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Variant updated successfully"}

################################################################################################

# Composition
# Route to add Composition
@app.post("/composition")
async def composition_add(id:int,variantid:int,ingredientid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO composition (id,variantid,ingredientid) VALUES (%s, %s, %s)"
    values = (id,variantid,ingredientid)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Composition added successfully"}

# Route to delete Composition
@app.delete("/composition")
async def composition_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM composition WHERE composition.id = (%s)"
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
    query = "SELECT * FROM composition"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#Route to update Composition
@app.put("/composition")
async def composition_update(id:int,variantid:int,ingredientid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE composition SET variantid = %s and ingredientid = %s WHERE id = %s"
    values = (variantid, ingredientid, id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Composition updated successfully"}

#################################################################################################

# Offering
# Route to add Offering
@app.post("/offering")
async def offering_add(id:int,majorcatid:int,subcatid:int,variantid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO offering (id,majorcatid,subcatid,variantid) VALUES (%s, %s, %s,%s)"
    values = (id,majorcatid,subcatid,variantid)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Offering added successfully"}

# Route to delete Offering
@app.delete("/offering")
async def offering_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM offering WHERE offering.id = (%s)"
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
    query = "SELECT * FROM offering"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

#######################################################################################

# CUSTOMER PREFERENCE
# Route to add custpref
@app.post("/custpreference")
async def custpreference_add(id:int,custid:int,variantid:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO custpreference (id,custid,variantid) VALUES (%s, %s, %s)"
    values = (id,custid,variantid)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "Customer Preference added successfully"}

# Route to delete custpref
@app.delete("/custpreference")
async def custpreference_delete(id:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM custpreference WHERE custpreference.id = (%s)"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "customer preference deleted successfully"}

#Route to display Composition
@app.get("/custpreference")
async def custpreference_display():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM custpreference"
    cursor.execute(query)
    category = cursor.fetchall()
    connection.close()
    return category

########################################################################################
