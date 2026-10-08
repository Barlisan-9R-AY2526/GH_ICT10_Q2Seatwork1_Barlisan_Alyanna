# 2nd QTR Seatwork 1
from pyscript import display, document

def get_nickname(e):
    document.getElementById('output1').innerHTML = " "
    country_nicknames = {
        "philippines": "The Pearl of the Orient Seas",
        "singapore": "The Lion City",
        "vietnam": "The Land of the Ascending Dragon",
        "indonesia": "The Emerald of the Equator",
        "thailand": "The Land of Smiles",
        "malaysia": "The Land of Truly Asia",
        "cambodia": "The Kingdom of Wonder",
        "myanmar": "The Golden Land",
        "brunei": "The Abode of Peace",
        "laos": "The Land of a Million Elephants",
        "timor-leste": "The Land of the Rising Sun in South East Asia"
    }

    country = document.getElementById('country_input').value.lower()

    # message if nickname not valid
    nickname = country_nicknames.get(country, "Sorry, I don't have a nickname for that country.")

    display(f"Nickname: {nickname}", target='output1')