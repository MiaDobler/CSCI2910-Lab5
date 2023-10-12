#LotR API - Lab 5
import requests
import json

#key = kxTkKFL3JRyaIDDoLknv 


#using https://www.youtube.com/watch?v=63nw00JqHo0 as resource
def menu():
    print("Menu for The One API Implementation \n--------------------\n")
    print("[1] Look up a Character")
    print("[0] Exit Program")

menu()

option = int(input("Enter option choice: "))
while option!=0:
    if option == 1:
        #currently repeats the following in a loop when option one has been called
        userInput = input("What character do you want: ")
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

    else:
        print("Invalid option.")







#some initial issues with the API accessing and how to do it with a token, tried different methods, settled on this:
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


