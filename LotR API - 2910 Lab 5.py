#LotR API - Lab 5
import requests
import json

#key = kxTkKFL3JRyaIDDoLknv 


userInput = input("What character do you want: ")

#some initial issues with the API accessing and how to do it with a toke, tried different methods, settled on this:
API_URL = f"https://the-one-api.dev/v2/character?name={userInput}"
headers = {
    'Authorization': 'Bearer kxTkKFL3JRyaIDDoLknv',
}
response = requests.get(API_URL, headers=headers)


if response.status_code == 200:
    data = response.json() 
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    data = None

print (response.json())

print("\n" +
                      "Menu for The One API Implementation \n" +
                      "--------------------\n" +
                      "[1] Get a quote\n" +
                      "[2] Look up Character\n" +
                      "[3] End the Program\n" +
                      "\n")
userinputt = ("Please enter the number of your choice: ")

def number_to_string(userinputt):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
