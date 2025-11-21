from morsedictionary import morsedictionary,textdictionary

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
    
