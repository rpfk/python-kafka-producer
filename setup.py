import getopt
import sys
from daemon import daemon


def main(argv):
    zk_hosts = []

    # Check if the required command line arguments are given
    try:
        opts, args = getopt.getopt(argv, "", ["zk_hosts="])
    except getopt.GetoptError:
        print 'setup.py --zk_hosts=<zk_hosts>'
        sys.exit()

    # Get zk_hosts from the command line arguments
    for opt, arg in opts:
        if opt == "--zk_hosts":
            zk_hosts = arg

    # Check if zk_hosts are set correctly
    try:
        zk_hosts
    except NameError:
        print 'setup.py --zk_hosts=<zk_hosts>'
        sys.exit()

    # Start the calculation
    daemon(zk_hosts)


if __name__ == "__main__":
    main(sys.argv[1:])
