import sys, os

path, dirs, files = os.walk(sys.argv[1]).next()
file_count = len(files)

dic = {}

for file_name in files:
	if ("Presenter" in file_name):
		file = open(path + "/" + file_name)

		print(file_name + ":")

		private_methods_count = 0
		public_methods_count = 0

		public_methods	= []

		start_count = False


		for line in file.readlines():


			if (start_count):
				
				if ("val" in line and "private" not in line):
					method_name = line.split()[1]
					print("public val detected: " + method_name)
					public_methods_count = public_methods_count + 1
					public_methods.append(method_name)
					
				if ("fun" in line and "()" in line and "private" not in line):
					method_name = line.split()[1].replace("():", "")
					print("public fun detected: " + method_name)
					public_methods_count = public_methods_count + 1
					public_methods.append(method_name)

			constructor_ended = "{" in line

			start_count = start_count or constructor_ended

		dic[file_name] = public_methods

print(dic)
		
		# print("public methods: " + str(public_methods_count))
		# print("private methods: " + str(private_methods_count))

# print("presenters count:" + str(presenters))
# print("words:" + str(words))

# print("public methods: " + str(len(files)))
# print("public fields: " + str(words))
