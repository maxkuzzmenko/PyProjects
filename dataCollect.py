def dataCollect():
    printList = ["Username", "Password", "EMail"]
    forbiddenCharacters = (' ', '.', ',', ';', '"', "'")
    credentials = {}
    for data in printList:
        print("Please enter your " + data, end=': ')
        inputValue = input()

        while (data != "Username" or data != "Password") and any(item in inputValue for item in forbiddenCharacters):
            print("Sorry, you cannot use any special characters in your " + data)
            print("Try again", end=": ")
            inputValue = input()
            continue
    return credentials
print(dataCollect())