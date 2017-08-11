import os

assignment = 'assignments02-04'

with open('bme590netids.csv', 'r') as f:
    os.chdir(assignment)
    for line in f:
        netid = line.rstrip('\n')

        if os.path.isdir(netid):
            print('[%s] Local repo exists; pulling latest updates.' % netid)
            os.chdir(netid)
            os.system('git pull')
            os.chdir('..')
        else:
            print('[%s] Local repo does not exist; cloning.' % netid)
            os.system('git clone git@gitlab.oit.duke.edu:%s/%s.git %s' % (netid, assignment, netid))
