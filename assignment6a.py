import json
state_capitals = {
    "Maharashtra": "Mumbai",
    "Gujarat":"Gandhinagar",
    "Uttar pradesh": "Lucknow",
    "Karnataka": "Bangaluru",
    "Tamilnadu": "Chennai",
    "Westy bengal": "Kolakata",
    "Rajasthan": "Jaipur"
}
with open("C:\\Users\\Public\\python\\state_capitals.json",'w')as json_file:
    json.dump(state_capitals,json_file)