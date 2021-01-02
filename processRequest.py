
import sys
import interpreter

from interpreter import JSONtoEvent
from send import sendEmail
import send

def main(argv):
    event = JSONtoEvent(argv[1])
    send.sendEmail(event)

if __name__ == "__main__":
    main(sys.argv)