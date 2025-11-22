from src.morsedictionary import morsedictionary,textdictionary

def texttomorse(message):
    """Converts plaintext message to morse code"""
    uppermessage = message.upper()
    morsecode = ""
    for element in uppermessage:
        try:
            morsecode += morsedictionary[element] + " "
        except KeyError: 
            raise ValueError(f"ERR: {element} cannot be expressed in morse")
        
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
                    raise ValueError(f"ERR: {alphabetcode} cannot be converted to plaintext")
        text += " "

    return text.strip()

def identifier(userinput:str):
    userinput = userinput.strip()

    if userinput == "":
        raise ValueError("ERR: Empty text, can't identify")


    morsecharacters = set('.- /')
    inputcharacters = set(userinput.strip())

    if inputcharacters.issubset(morsecharacters):
        return "Morse"
    else:
        return "Text"
    
def translate(userinput):
    resultidentifier = identifier(userinput)

    if resultidentifier == "Morse":
       plain = morsetotext(userinput)
       morse = userinput
    elif resultidentifier == "Text":
        morse = texttomorse(userinput)
        plain = userinput

    return morse, plain
    


    
