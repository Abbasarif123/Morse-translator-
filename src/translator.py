from src.morsedictionary import morsedictionary,textdictionary

def texttomorse(message):
    uppermessage = message.upper()
    morsecode = ""
    errorelement = []
    for index,element in enumerate(uppermessage):
        try:
            morsecode += morsedictionary[element] + " "
        except KeyError: 
            return "ERROR, THIS CHARACTER CANNOT BE EXPRESED IN MORSECODE"
        
    return  f"{morsecode.strip()}"

def morsetotext(morsecode):
    text = ""
    morsewordlist = morsecode.split(" / ")
    for morseword in morsewordlist:
        morseletter = morseword.split(" ")

        for alphabetcode in morseletter:
            if alphabetcode != "":
                try:
                    text += textdictionary[alphabetcode]
                except KeyError:
                    return "INVALID MORSECODE"
        text += " "

    return text.strip()


def identifier(userinput):
    if userinput == "" or userinput.isspace():
        raise ValueError( "Error, can't identify")


    morsecharacters = set('.- /')
    inputcharacters = set(userinput.strip())

    if inputcharacters.issubset(morsecharacters):
        return "Morse"
    else:
        return "Text"
    


    
