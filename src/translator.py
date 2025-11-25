from src.morsedictionary import morsedictionary,textdictionary

def texttomorse(message):
    """Converts plaintext message to morse code"""
    uppermessage = message.upper()
    morsecode = ""
    for element in uppermessage:
        try:
            morsecode += morsedictionary[element] + " "
        except KeyError: 
            raise ValueError(f"{element} cannot be expressed in morse")
        
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
                    raise ValueError(f"{alphabetcode} cannot be converted to plaintext")
        text += " "

    return text.strip()



def identifier(userinput:str):
    userinput = userinput.strip()

    if userinput == "":
        raise ValueError("Empty text, can't identify")


    morsecharacters = set('.- /')
    inputcharacters = set(userinput.strip())

    if inputcharacters.issubset(morsecharacters):
        return "Morse"
    else:
        return "Text"
    
def polish_morse(morse:str) -> list[list[str]]:

    morse_words = morse.split("/")
    morse_letters = [word.strip().split() for word in morse_words]

    return morse_letters

def translate(userinput:str):

    def strip_morse(morse: str):
        """To ensure morse code doesn't start with spaces"""

        while morse[0] in ['/', ' '] or morse[-1] in ['/', ' ']:
            morse = morse.strip(' ').strip('/')

            if len(morse) == 0:
                raise ValueError("Empty morse string given")
        
        return morse


    if not userinput:
        raise ValueError("Input is empty")

    resultidentifier = identifier(userinput)

    if resultidentifier == "Morse":
       morse = strip_morse(userinput)
       plain = morsetotext(morse)
    elif resultidentifier == "Text":
        plain = userinput.strip()
        morse = texttomorse(plain)

    return morse, plain
    


if __name__ == "__main__":
    print(translate("///"))
