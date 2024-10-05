
suspect_1 = {
    "name": "John Doe",
    "age": 35,
    "address": "123 Sandford High Street",
    "charges": ["Theft", "Fraud", "Burglary"],
    "partner": "Samantha",
    "bank_balance": 43.98,
}

suspect_2 = {
    "name": "Jane Smith",
    "age": 28,
    "address": "436 Elm Street",
    "charges": ["Forgery", "Harassment"],
    "partner": "Tony",
    "bank_balance": 437.65,
}

suspect_3 = {
    "name": "Sam Brown",
    "nickname" : "smokey",
    "age": 42,
    "address": "789 Oak Avenue",
    "charges": ["Burglary", "Assault", "Theft", "Vehicle Crime"],
    "partner": "John Doe",
    "bank_balance": 12.50,
}


suspect_database = {
    "S1" : suspect_1,
    "S2" : suspect_2,
    "S3" : suspect_3,
}

print(f"The address for Suspect 2 is: {suspect_database["S2"]["address"]}")

suspect_database["S1"]["charges"].append("Resisting Arrest")

suspect_database["S3"]["address"] = "123 High Street"

print(suspect_database["S1"]["charges"])



suspect_4 = {
    "name": "David Blacksmith",
    "age": 60,
    "address": "7 Insull Avenue",
    "charges": ["Vandalism", "Criminal Damage"],
    "partner": "Shirley",
    "bank_balance": 2.70,
}

suspect_database["S4"] = suspect_4

# del suspect_database["S3"]

for suspect_id, suspect_info in suspect_database.items():
    print(suspect_info["name"])