import pytest
from src.translator import morsetotext, texttomorse,identifier

####tests for texttomorse####

def test_basic_texttomorse(): #overall normal test
    assert texttomorse("Hey, here is a normal testing sentence") == ".... . -.-- --..-- / .... . .-. . / .. ... / .- / -. --- .-. -- .- .-.. / - . ... - .. -. --. / ... . -. - . -. -.-. ."
    assert texttomorse ("He lives in a pineapple under the sea. SPONGEBOB SQUAREPANTS") == ".... . / .-.. .. ...- . ... / .. -. / .- / .--. .. -. . .- .--. .--. .-.. . / ..- -. -.. . .-. / - .... . / ... . .- .-.-.- / ... .--. --- -. --. . -... --- -... / ... --.- ..- .- .-. . .--. .- -. - ..."
    assert texttomorse("Gian hain aap") == "--. .. .- -. / .... .- .. -. / .- .- .--."

def test_basicSOS_texttomorse(): #the classic SOS test
    assert texttomorse("SOS") == "... --- ..."

def test_upperlowerinsensitivity_textomorse(): #shows that morse code in not sensitive to uppercase or lowercase letters
    assert texttomorse("hello") == ".... . .-.. .-.. ---"
    assert texttomorse("HELLO") == ".... . .-.. .-.. ---"

def test_numbertest_texttomorse(): #conversion of numbers
    assert texttomorse("123") == ".---- ..--- ...--"
    assert texttomorse("84,900") == "---.. ....- --..-- ----. ----- -----"
    assert texttomorse("505") == "..... ----- ....."

def test_emptystring_texttomorse(): #empty string test
    assert texttomorse("") == ""

####tests for morsetotext####

def test_basic_morsetotext(): #overall normal test
    assert morsetotext(".... . -.-- --..-- / .... . .-. . / .. ... / .- / -. --- .-. -- .- .-.. / - . ... - .. -. --. / ... . -. - . -. -.-. .") == "HEY, HERE IS A NORMAL TESTING SENTENCE"
    assert morsetotext("- ..- -. / - ..- -. / ... .- .... --- --- .-.") == "TUN TUN SAHOOR"
    assert morsetotext(".-- .... .- - / .. ... / - .... .. ... / -... . .... .- ...- .. --- .-. / .--. --- --- .--- .- ..--..") == "WHAT IS THIS BEHAVIOR POOJA?"

def test_basicSOS_morsetotext(): #the classic SOS test
    assert morsetotext("... --- ...") == "SOS"

def test_emptytest_morsetotext(): #empty string test
    assert morsetotext("") == ""

def test_trimmingtest_morsetotext(): #should ideally trim whitespace
    assert morsetotext("        .-- .- -.. . .-. . / -.- .- / -... . - .- / .-- .- -.. . .-. . / -.- . / -... . - .-        ") == "WADERE KA BETA WADERE KE BETA"

####testing both ways to see if their outputs are correct both ways####
#NOTE: all morsecode to text returns will be in uppercase since morsecode only works in uppercase and isnt case sensitive


def test_bothwaystest():
    originaltext = "I HAVE A PEN, I HAVE AN APPLE. UHHH APPLE-PEN. I HAVE A PEN, I HAVE PINEAPPLE. UHHH PINEAPPLE-PEN. APPLE-PEN, PINEAPPLE-PEN. PENPINEAPPLEAPPLEPEN"

    morsecode = texttomorse(originaltext)
    result = morsetotext(morsecode)

    assert result == originaltext


###tests for the identifier function

def test_identifiertests():
    assert identifier("-... . -.-- -... .-.. .- -.. . / -... . -.-- -... .-.. .- -.. . / .-.. . - / .. - / .-. .. .--.") == "Morse"
    assert identifier("-- . / .-- .... . -. / -.- -. . . / ... ..- .-. --. . .-. -.-- / .. ... / -.. ..- .") == "Morse"
    assert identifier("they did surgery on a grape") == "Text"
    assert identifier("We've tried nothing and we're all out of ideas!") == "Text"
