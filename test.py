from enum import Enum

class Test(str, Enum):
    name = "Alex"

def pr(model: Test):
    print(model.value)

pr("Bob")