
#functions===================================================================================================
#menu
def Menu():
    print("===========Menu===========")
    print("1. Encryption")
    print("2. Decryption")
    print("0. Exit")
    print("==========================")

    while True: #input validation
        option = input("Enter option: ")

        if option.isdigit() == False:
            print("Please enter an integer.")

        elif int(option) > 2 or int(option) < 0:
            print("Option out of range.")

        else:
            break

    return int(option)

#prompt user for 10 plugboard combinations
def PlugBoardCombinations(plugBoard):
    for i in range(10):
        while True: #input validation
            combination = input("Please enter 2 alphabets to pair on the plugboard (a,b): ")
            combinationList = combination.split(",")
            if  len(combination) < 3 or len(combination) > 3 or len(combinationList) != 2:
                print("Please enter in (a,b) format with only one letter per parameter.\n")

            elif combinationList[0].isdigit() or combinationList[1].isdigit():
                print("Please enter alphabets only.\n")

            elif (combinationList[0] in plugBoard or combinationList[0] in plugBoard.values()) and (combinationList[1] in plugBoard or combinationList[1] in plugBoard.values()):
                print("'{0}' and '{1}' are already in use.\n".format(combinationList[0], combinationList[1]))

            elif combinationList[0] in plugBoard or combinationList[0] in plugBoard.values():
                print("'{0}' is already in use.\n".format(combinationList[0]))

            elif combinationList[1] in plugBoard or combinationList[1] in plugBoard.values():
                print("'{0}' is already in use.\n".format(combinationList[1]))

            else:
                break

        plugBoard[combinationList[0]] = combinationList[1]

    return plugBoard

#prompt user for initial rotor config
def RotorConfig(rConfig):
    while True: #input validation
        config = input("\nPlease enter rotor configuration (3,2,1): ")
        configList = config.split(",")

        if len(configList) != 3:
            print("Please enter in (3,2,1) format with only one integer per parameter.")
        elif configList[0].isalpha() or configList[1].isalpha() or configList[2].isalpha():
            print("Please enter integers only.")

        elif int(configList[0]) > 26 or int(configList[0]) < 1 or int(configList[1]) > 26 or int(configList[1]) < 1 or int(configList[2]) > 26 or int(configList[2]) < 1:
            print("Please enter integers between 1 and 26 inclusive.")        

        else:
            break

    configList = [int(each) for each in configList]

    return configList

#pass through plugboard
def PlugBoard(stringList):
    for key, value in plugBoard.items():
            if stringList[i] == key: #if letter is found in the list of keys
                stringList[i] = value #letter is substituted by value

            elif stringList[i] == value: #if the letter if found in the list of values
                stringList[i] = key #letter is substituted by key

    return stringList

def Stepping(rConfig, stepping1, stepping2, stepping3):
    #increment rotorOne by one
    if rConfig[2] == 26: #if rotor is at 26, change back to 1
        rConfig[2] = 1

    else:
        rConfig[2] += 1

    #stepping
    if rConfig[2] == stepping1:
        if rConfig[1] == 26: #if rotor is at 26, change back to 1
            rConfig[1] = 1

        else:
            rConfig[1] += 1
            
        if rConfig[1] == stepping2:
            if rConfig[0] == 26: #if rotor is at 26, change back to 1
                rConfig[0] = 1

            else:
                rConfig[0] += 1

    return rConfig

def Reflector(stringList):
    for key, value in reflector.items():
            if stringList[i] == key:
                stringList[i] = value

            elif stringList[i] == value:
                stringList[i] = key

    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value #position from reflector

    return stringList

#pass through rotors 1st time
def First(stringList, rotorOne, rotorTwo, rotorThree):
    letterNo = 0

    #rotorOne---------------------------------------------------------------------
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepP = (letterNo + rConfig[2] - 1) % 26 #check for steppings

    if stepP == 0:
        stepP = 26

    #print("stepP")
    #print(stepP)

    stringList[i] = list(rotorOne.items())[stepP-1][1] #output for rotorOne

    #print("R1 first a")
    #print(stringList[i])

    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepM = (letterNo - rConfig[2] + 1) % 26

    if stepM == 0:
        stepM = 26

    if stepM < 0:
        stepM += 26
    #print("stepM")
    #print(stepM)

    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stepM == value:
            stringList[i] = key
    #print("R1 first b")
    #print(stringList[i])
    #rotorTwo---------------------------------------------------------------------
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepP = (letterNo + rConfig[1] - 1) % 26 #check for steppings

    if stepP == 0:
        stepP = 26

    #print("stepP")
    #print(stepP)
    stringList[i] = list(rotorTwo.items())[stepP-1][1] #output for rotorOne
    #print("R2 first a")
    #print(stringList[i])
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value
    
    stepM = (letterNo - rConfig[1] + 1) % 26

    if stepM == 0:
        stepM = 26

    if stepM < 0:
        stepM += 26
    #print("stepM")
    #print(stepM)
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stepM == value:
            stringList[i] = key
    #print("R2 first b")
    #print(stringList[i])
    #rotorThree---------------------------------------------------------------------
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepP = (letterNo + rConfig[0] - 1) % 26 #check for steppings

    if stepP == 0:
        stepP = 26

    #print("stepP")
    #print(stepP)
    stringList[i] = list(rotorThree.items())[stepP-1][1] #output for rotorOne
    #print("R3 first a")
    #print(stringList[i])
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepM = (letterNo - rConfig[0] + 1) % 26

    if stepM == 0:
        stepM = 26

    if stepM < 0:
        stepM += 26
    #print("stepM")
    #print(stepM)
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stepM == value:
            stringList[i] = key
    #print("R3 first b")
    #print(stringList[i])
    return stringList

#pass through rotors 2nd time
def Second(stringList, rotorOne, rotorTwo, rotorThree):
    letterNo = 0

    #rotoThree---------------------------------------------------------------------
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepP = (letterNo + rConfig[0] - 1) % 26 #check for steppings

    if stepP == 0:
        stepP = 26

    #print("stepP")
    #print(stepP)
    for key1, value1 in rotorThree.items(): 
        for key2, value2 in alphaToNum.items():
            if value1 == key2 and stepP == value2:               
                stringList[i] = key1

    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value
    #print("R3 second a")
    #print(stringList[i])
    stepM = (letterNo - rConfig[0] + 1) % 26

    if stepM == 0:
        stepM = 26

    if stepM < 0:
        stepM += 26
    #print("stepM")
    #print(stepM)
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stepM == value:
            stringList[i] = key
    #print("R3 second b")
    #print(stringList[i])
    #rotorTwo---------------------------------------------------------------------
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepP = (letterNo + rConfig[1] - 1) % 26 #check for steppings

    if stepP == 0:
        stepP = 26

    #print("stepP")
    #print(stepP)
    for key1, value1 in rotorTwo.items(): 
        for key2, value2 in alphaToNum.items():
            if value1 == key2 and stepP == value2:               
                stringList[i] = key1
    #print("R2 second a")
    #print(stringList[i])
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepM = (letterNo - rConfig[1] + 1) % 26

    if stepM == 0:
        stepM = 26

    if stepM < 0:
        stepM += 26
    #print("stepM")
    #print(stepM)
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stepM == value:
            stringList[i] = key
    #print("R2 second b")
    #print(stringList[i])
    #rotorOne---------------------------------------------------------------------
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value

    stepP = (letterNo + rConfig[2] - 1) % 26 #check for steppings
    #print("stepP")
    #print(stepP)
    for key1, value1 in rotorOne.items(): 
        for key2, value2 in alphaToNum.items():
            if value1 == key2 and stepP == value2:               
                stringList[i] = key1
    #print("R1 second a")
    #print(stringList[i])
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stringList[i] == key:
            letterNo = value
    
    stepM = (letterNo - rConfig[2] + 1) % 26

    if stepM < 0:
        stepM += 26
    #print("stepM")
    #print(stepM)
    for key, value in alphaToNum.items(): #find the alphabet's corr. number
        if stepM == value:
            stringList[i] = key
    #print("R1 second b")
    #print(stringList[i])
    return stringList

#alphabet to number dictionary===============================================================================
alphaToNum = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
            "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20,
            "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

#rotors======================================================================================================
rotorOne = {"a":"e", "b":"k", "c":"m", "d":"f", "e":"l", "f":"g", "g":"d", "h":"q", "i":"v", "j":"z",
            "k":"n", "l":"t", "m":"o", "n":"w", "o":"y", "p":"h", "q":"x", "r":"u", "s":"s", "t":"p",
            "u":"a", "v":"i", "w":"b", "x":"r", "y":"c", "z":"j"}

rotorTwo = {"a":"a", "b":"j", "c":"d", "d":"k", "e":"s", "f":"i", "g":"r", "h":"u", "i":"x", "j":"b",
            "k":"l", "l":"h", "m":"w", "n":"t", "o":"m", "p":"c", "q":"q", "r":"g", "s":"z", "t":"n",
            "u":"p", "v":"y", "w":"f", "x":"v", "y":"o", "z":"e"}

rotorThree = {"a":"b", "b":"d", "c":"f", "d":"h", "e":"j", "f":"l", "g":"c", "h":"p", "i":"r", "j":"t",
              "k":"x", "l":"v", "m":"z", "n":"n", "o":"y", "p":"e", "q":"i", "r":"w", "s":"g", "t":"a",
              "u":"k", "v":"m", "w":"u", "x":"s", "y":"q", "z":"o"}
#reflector===================================================================================================
reflector = {"a":"x", "b":"z", "c":"o", "d":"w", "e":"s", "f":"n", "g":"r", "h":"q", "i":"v", "j":"p",
             "k":"y", "l":"u", "m":"t"}

#main program================================================================================================
while True:
    plugBoard = {}
    rConfig = []

    option = Menu()

    #configuring plugboard
    plugBoard = PlugBoardCombinations(plugBoard)
    
    #prints out plugboard config
    #for key, value in plugBoard:
    #   print(key, value)
        
    #configuring starting settings
    rConfig = RotorConfig(rConfig)
    #print(rConfig)
    
    text = ""

    if option == 1:
        text = input("Please enter plaintext to encrypt: ")

    elif option == 2:
        text = input("Please enter ciphertext to decrypt: ")

    elif option == 0:
        break
    
    #encryption / decryption process
    stepping1 = 8
    stepping2 = 20
    stepping3 = 11
    stringList = list(text)
    #print(stringList)
    output = ""

    for i in range(len(stringList)):#
        #pass through plugboard
        stringList = PlugBoard(stringList)
        #print("After pb")
        #print(stringList[i])

        #pass through rotors 1st time        
        stringList = First(stringList, rotorOne, rotorTwo, rotorThree)
        #print("After first")
        #print(stringList[i])

        #pass through reflector
        stringList = Reflector(stringList)
        #print("\nAfter Reflect " + stringList[i] + "\n")#

        #print(stringList[i])

        #print(stringList[i])

        #pass through rotors 2nd time
        stringList = Second(stringList, rotorOne, rotorTwo, rotorThree)
        #print("After second")
        #print(stringList[i])

        #pass through plugboard again
        stringList = PlugBoard(stringList)
        #print("\n After PB " + stringList[i])#

        #stepping
        Stepping(rConfig, stepping1, stepping2, stepping3)
        
        #print('final')
        #print(stringList[i])

        #add ciphertext letter to output
        output = output + stringList[i]

    if option == 1:
        print("Ciphertext: {}\n".format(output))

    elif option == 2:
        print("Plaintext: {}\n".format(output))

