from Producer import Producer
import getopt
import sys
import pycurl
from StringIO import StringIO


def main(argv):
    # Default values
    assignment_url = 'https://raw.githubusercontent.com/rpfk/python-kafka-producer-assignment/master/assignment.json'
    kafka_address = '192.168.21.21:9092'

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
            assignment_url = arg

    # Check if kafka address is set correctly
    try:
        kafka_address
    except NameError:
        print 'kafka address is not set correctly, check the kafka address'
        print 'run.py --kafka-address=<kafka-address> --assignment-url=<assignment-url>'
        sys.exit()

    # Check if assignment is set correctly
    try:
        assignment_url
    except NameError:
        print 'assignment url is not set correctly, check the assignment url'
        print 'run.py --kafka-address=<kafka-address> --assignment-url=<assignment-url>'
        sys.exit()

    # get the assignment from the assignment url
    assignment_buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, assignment_url)
    c.setopt(c.WRITEDATA, assignment_buffer)
    c.perform()
    c.close()
    assignment = assignment_buffer.getvalue()

    # Run the producer if everything is set correctly
    Producer(kafka_address, assignment)


if __name__ == "__main__":
    main(sys.argv[1:])
