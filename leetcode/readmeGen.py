'''
Built this README File
'''
import os, sys, pickle
import subprocess as sp


class Command(object):
    """Run a command and capture its output string, error string and exit status"""
    def __init__(self, command):
        self.command = command 

    def run(self, shell=True):
        process = sp.Popen(self.command, shell = shell, stdout = sp.PIPE, stderr = sp.PIPE)
        self.pid = process.pid
        self.output, self.error = process.communicate()
        self.failed = process.returncode
        return self

    @property
    def returncode(self):
        return self.failed

README_DUMP = """
# Auto Generated README File
### [LeetCode](https://leetcode.com/) Problems in Python
Uses the excellent [LeetCode CLI](https://github.com/skygragon/leetcode-cli)
\n
"""
README_FNAME = "README.md"
PICKLE_FNAME = "lc.pickle"
NUM_LINES = 6

rop = open(README_FNAME, 'w')
rop.truncate()
rop.write(README_DUMP)

if not os.path.exists(PICKLE_FNAME):
    l = {'passing': {}, 'failing': {}}
    with open('lc.pickle', 'wb') as handle:
        pickle.dump(l, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    with open('lc.pickle', 'rb') as handle:
        l = pickle.load(handle)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    filename, file_extension = os.path.splitext(f)
    if file_extension == ".py" and f not in l["passing"]:
        # Get problem details from .py file
        fop = open(f)
        lines = []
        for i in range(NUM_LINES):
            lines.append(fop.readline().rstrip())
        problem_no, problem_name = get_problem(lines[1])
        problem_url = get_problem_url(lines[3])
        problem_level = get_problem_level(lines[5])
        fop.close()

        # Submit the problem
        c = Command("leetcode submit " + f)
        c.run()
        if c.failed:
            print "Failed to submit on LeetCode! Try by hand. Filename=" + f
        else:
            if "Accepted" in c.output:
                l[passing][f] = {}
                l[passing][f]["filename"] = filename
                l[passing][f]["num"] = problem_no
                l[passing][f]["name"] = problem_name
                l[passing][f]["url"] = problem_url
                l[passing][f]["level"] = problem_level
    elif file_extension == ".py" and f in l["passing"]:
        print "Skipping " + f + " as it is already passing"
    else:
        print "Skipping " + f
        '''
        lines = []
        fop = open(f)
        for i in range(NUM_LINES):
            lines.append(fop.readline().rstrip())
        if lines[0] == MARKER and lines[-1] == MARKER:
            rop.write(f + " : " + lines[1] + "\n")
            rop.write("\n")
        else:
            print("Missed file: " + f)
        '''
with open('lc.pickle', 'wb') as handle:
    pickle.dump(l, handle, protocol=pickle.HIGHEST_PROTOCOL)
rop.close()
