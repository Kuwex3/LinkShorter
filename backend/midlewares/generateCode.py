from string import digits, ascii_uppercase, ascii_lowercase
import random

alph = str(digits+ascii_lowercase+ascii_uppercase)

def generateCode():
    rawMass = []
    for _ in range(6):
        symbol = random.choice(alph)
        rawMass.append(symbol)
    code = "".join(rawMass)
    return code