from typing import Optional
from pydantic import BaseModel

# This contains Main Category of Chocolates
# eg., Chocolates, Wafer, Syrups, Assorted
class MainCategory(BaseModel):
    id: int
    name: str

# This contains Sub Category of Chocolates
# eg., Chocolates - Classic, Premium, Wafer, Syrups, Assorted
class SubCategory(BaseModel):
    id: int
    name: str

# This contains Variants in the sub category of Chocolates
# eg., Tropical, FruitNNut, Mocha, Hazelnut, Dark Passion etc
class Variant(BaseModel):
    id: int
    name: str
    descryption: str
    allergyid: int

# This contains all ingredients required
class Ingredient(BaseModel):
    id: int
    name: str
    quantity: int

# This contains the composition for each chocolate
class Composition(BaseModel):
    id: int
    variantid: int
    ingredientid: int

# This contains all Offerings of chocolate
class Offering(BaseModel):
    id: int
    majorid: int
    subcatid: int
    variantid: int

# This contains all allergies related to chocolate
class Allergy(BaseModel):
    id: int
    name: str

# This contains all customers
class Customer(BaseModel):
    id: int
    name: str
    phone: str

# This contains all Preferences/likings of each customer
class CustPreference(BaseModel):
    id: int
    custid: int
    variantid: int

# This contains all allergies for a customer w.r.t. chocolate
class CustAllergy(BaseModel):
    id: int
    custid: int
    allergyid: int







