'''
Built this README File
'''
import os, sys, pickle

README_DUMP = """
Auto Generated README File
--------------------------
\t -- LeetCode Problems in Python [https://leetcode.com/]\n
\t -- Uses the excellent LeetCode CLI [https://github.com/skygragon/leetcode-cli]\n
\n
"""
README_FNAME = "README.md"

rop = open(README_FNAME, 'w')
rop.truncate()
rop.write(README_DUMP)



files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    filename, file_extension = os.path.splitext(f)
    if file_extension == ".py":
        lines = []
        fop = open(f)
        for i in range(NUM_LINES):
            lines.append(fop.readline().rstrip())
        if lines[0] == MARKER and lines[-1] == MARKER:
            rop.write(f + " : " + lines[1] + "\n")
            rop.write("\n")
        else:
            print("Missed file: " + f)

rop.close()
