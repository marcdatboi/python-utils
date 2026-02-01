



# Imports
from src.Logger import Logging


### Test File ###
def test():
    obj = Logging(r"C:\DevFolder\python\marc_utils\tests\test.txt")
    obj.log("Hey! This is a test!", Logging.Severity.INFO)
    obj.log("Hey this is a fatal error!", Logging.Severity.FATAL)

if __name__ == "__main__":
    test()