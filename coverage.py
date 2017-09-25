import sys, os

root = sys.argv[1] + "app/src/main/java"
test_root = sys.argv[1] + "app/src/test/java"
all_methods = {}
tested_methods = {}

def find_methods(x, dir_name, files):
	for file_name in files:
		if ("Presenter" in file_name or "Dao" in file_name):
			file_name_with_path = dir_name + "/" + file_name
			file = open(file_name_with_path)

			public_methods	= []

			for line in file.readlines():	
					
				if ("val" in line 
					and "=" in line
					and ("Observable" in line or "Subject" in line)
					and "private" not in line
					and "internal" not in line
					and "override" not in line):
					method_name = line.split()[1].replace("()", "").replace(":", "")
					public_methods.append(method_name)
					
				if ("fun" in line 
					and "()" in line 
					and "private" not in line 
					and "internal" not in line 
					and "override" not in line):
					method_name = line.split()[1].replace(":", "")
					public_methods.append(method_name)

			if (len(public_methods) > 0):
				all_methods[file_name] = public_methods
				tested_methods[file_name] = []

def find_usages(x, dir_name, files):
	for file_name in files:

		for key in all_methods:
			if (key.split(".")[0] in file_name):

				file_name_with_path = dir_name + "/" + file_name
				file = open(file_name_with_path)
				methods_for_file = all_methods[key]
			
				for line in file.readlines():
					if ("import" in line
						or "fun" in line ):
						continue
					for method in methods_for_file:
						if (method in line):
							if (method not in tested_methods[key]):
								tested_methods[key].append(method)

os.path.walk(root, find_methods, 0)
os.path.walk(test_root, find_usages, 0)

all_methods_count = 0
tested_methods_count = 0

for key in all_methods:
	all_methods_count = all_methods_count + len(all_methods[key])

for key in tested_methods:
	tested_methods_count = tested_methods_count + len(tested_methods[key])

coverage = float(tested_methods_count) / float(all_methods_count)

for file_name in all_methods:
	cov = (float(len(tested_methods[file_name])) / float(len(all_methods[file_name])))
	print(str(len(tested_methods[file_name])) + "/" + str(len(all_methods[file_name])) + 
		" (" + str((round(cov, 3)) * 100 ) + "%) " + file_name)

	for method in all_methods[file_name]:
		if method in tested_methods[file_name]:
			print (" * " + method)
		else :
			print (" - " + method)

print("\nCode Coverage report: ")
print("===========================")
print("|| all methods    " + str(all_methods_count))
print("|| tested methods " + str(tested_methods_count))
print("===========================")
print("|| total coverage " + str((round(coverage, 4)) * 100 ) + "%")
print("===========================")


