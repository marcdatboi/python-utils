



# Imports
from enum import Enum
import sys
from colorama import Fore, Style
from datetime import date, datetime
import os







#### LOGGER CLASS ####
class Logging:



    #### SEVERITY LEVEL ENUM CLASS ####
    class Severity(Enum):
        INFO = 0
        DEBUG = 1
        WARNING = 2
        ERROR = 3
        CRITICAL = 4
        FATAL = 5  # Should stop the program


    ### Logging Constructor ###
    def __init__(self, path_to_text_file: str):
        self.path = path_to_text_file
        self.is_first_time = True

        # Validate path
        if self.path.lower().endswith(".txt") not in self.path:
            raise FileNotFoundError("File provided does not direct to a .txt file!")


    ### Turns the severity enum to a colored string
    def get_severity(self, severity: Severity):
        match severity:
            case Logging.Severity.INFO:
                return "INFO"

            case Logging.Severity.DEBUG:
                return "DEBUG"

            case Logging.Severity.WARNING:
                return "WARNING"

            case Logging.Severity.ERROR:
                return "ERROR"

            case Logging.Severity.CRITICAL:
                return "CRITICAL"

            case Logging.Severity.FATAL:
                return "FATAL"


    ### Logs a message inside of a text file ###
    def log(self, msg, severity: Severity):

        line = sys._getframe(1)

        # Actual message
        if (self.is_first_time):
            with open(self.path, "w") as file:
                file.write("\n" * 4)
                file.write("=== New Run Instance ===\n")

                file.write("-" * 26 + "\n")
                file.write(f"[{self.get_severity(severity)}] >> Line: {line.f_lineno}\n")
                file.write(f"-> {os.path.abspath(sys.argv[0])}\n")
                file.write(f"# {date.today()} | {datetime.now().strftime('%I:%M %p')}\n")
                file.write(f">> {msg}\n")
            self.is_first_time = False

        else:
            with open(self.path, "a") as file:
                file.write("-" * 26 + "\n")
                file.write(f"[{self.get_severity(severity)}] >> Line: {line.f_lineno}\n")
                file.write(f"-> {os.path.abspath(sys.argv[0])}\n")
                file.write(f"# {date.today()} | {datetime.now().strftime('%I:%M %p')}\n")
                file.write(f">> {msg}\n")

        # Only if a fatal error log was called.
        if severity == Logging.Severity.FATAL:
            print(Fore.RED + "FATAL ERROR: Emergency Shutdown started.\nTerminating Program..." + Style.RESET_ALL)
            sys.exit(1)