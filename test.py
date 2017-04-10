from Producer import Producer

fid = open('assignment.json', 'r')
assignment = fid.read()
fid.close()

Producer(assignment)
