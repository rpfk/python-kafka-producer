from Producer import Producer
import getopt
import sys


def main(argv):
    assignment = []

    # Check if the required command line arguments are given
    try:
        opts, args = getopt.getopt(argv, "", ["assignment="])
    except getopt.GetoptError:
        print 'run.py --assignment=<assignment>'
        sys.exit()

    # Get kafka_address from the command line arguments
    for opt, arg in opts:
        if opt == "--assignment":
            assignment = arg

    # Check if assignment is set correctly
    try:
        assignment
    except NameError:
        print 'run.py --assignment=<assignment>'
        sys.exit()

    Producer(assignment)


if __name__ == "__main__":
    main(sys.argv[1:])
