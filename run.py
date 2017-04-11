from Producer import Producer
import getopt
import sys
import pycurl
from StringIO import StringIO


def main(argv):
    kafka_address = []
    assignment = []

    # Check if the required command line arguments are given
    try:
        opts, args = getopt.getopt(argv, "", ["kafka-address=", "assignment-url="])
    except getopt.GetoptError:
        print 'run.py --kafka-address=<kafka-address> --assignment-url=<assignment-url>'
        sys.exit()

    # Get kafka_address from the command line arguments
    for opt, arg in opts:
        if opt == "--kafka-address":
            kafka_address = arg
        elif opt == "--assignment-url":

            # get the assignment from the assignment url
            assignment_buffer = StringIO()
            c = pycurl.Curl()
            c.setopt(c.URL, arg)
            c.setopt(c.WRITEDATA, assignment_buffer)
            c.perform()
            c.close()
            assignment = assignment_buffer.getvalue()

    # Check if kafka address is set correctly
    try:
        kafka_address
    except NameError:
        print 'kafka address is not set correctly, check the kafka address'
        print 'run.py --kafka-address=<kafka-address> --assignment-url=<assignment-url>'
        sys.exit()

    # Check if assignment is set correctly
    try:
        assignment
    except NameError:
        print 'assignment is not set correctly, check the assignment url'
        print 'run.py --kafka-address=<kafka-address> --assignment-url=<assignment-url>'
        sys.exit()

    # Run the producer if everything is set correctly
    Producer(kafka_address, assignment)


if __name__ == "__main__":
    main(sys.argv[1:])
