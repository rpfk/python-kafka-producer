from Producer import Producer
from StringIO import StringIO
import pycurl

# get the assignment from the assignment url
assignment_buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://raw.githubusercontent.com/rpfk/python-kafka-producer-assignment/master/assignment.json')
c.setopt(c.WRITEDATA, assignment_buffer)
c.perform()
c.close()
assignment = assignment_buffer.getvalue()

# run the producer
Producer('localhost:21', assignment)
