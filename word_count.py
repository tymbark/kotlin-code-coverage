import sys

file=open(sys.argv[1])
howMany = 0
words = []

for word in file.read().split():
    howMany = howMany +1
    words.append(word)

print(howMany)
# print(words)