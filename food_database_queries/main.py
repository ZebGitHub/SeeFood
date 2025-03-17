import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "root", 
    database = "hashim" 
)

sku = "1105917" #input("Enter a barcode to get a food: ") 
allergen = "wheat"
lower_allergen = allergen.lower()
upper_allergen = allergen.upper()

#input("Enter an allergen: ")

search_string = f"SELECT food.fdc_id AS SKU, branded_food.ingredients AS Ingredients, food.description AS Description FROM hashim.food INNER JOIN hashim.branded_food ON hashim.food.fdc_id=hashim.branded_food.fdc_id WHERE food.fdc_id = '{sku}';"

cursor = mydb.cursor()

cursor.execute(search_string)
columns = cursor.description
result = cursor.fetchall()

column_names = []
for column in columns: 
    column_names.append(column[0])


for i in range(len(column_names)): 
    print(column_names[i] + ":   " + result[0][i])