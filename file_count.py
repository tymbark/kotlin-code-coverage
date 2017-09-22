import sys, os

path, dirs, files = os.walk(sys.argv[1]).next()

print("files: " + str(len(files)))

