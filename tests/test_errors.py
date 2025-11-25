import pytest
from src.translator import *


def test_errors_mtt():
    with pytest.raises(ValueError):
        morsetotext("REF DO SOMETHING")
        morsetotext("............")

def test_errors_ttm():
    with pytest.raises(ValueError):
        texttomorse("#baller")
        texttomorse("~code~")
        texttomorse("WE ARE 90% DONE WITH THISSSS!!!")
        texttomorse("\U0001F614")

def test_errors_translator():
    raise NotImplementedError

def test_errors_identifier():

    with pytest.raises(ValueError):
        identifier("")
    assert identifier("////////") == "Morse"
    