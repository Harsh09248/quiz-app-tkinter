import requests

parameters = {
    "amount": 10,     
    "category": 18,       
    "type": "boolean",
    "difficulty":"easy"

}



response = requests.get(url="https://opentdb.com/api.php?",params=parameters)
response.raise_for_status()
data =  response.json()
question_data = data["results"]




