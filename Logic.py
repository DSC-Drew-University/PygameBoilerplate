#grab contents from file and puts it into a list then feeds it to Save_Dictionary to be turned into a dictionary
def Pull_Dictionary(File, Keys, Dictionary):
	f= open(File, "r")
	dictionary = f.read()
	f.close()
	dictionary = dictionary.split("\n")
	Save_Dictionary(dictionary, Keys, Dictionary)

# The next two functions manage saving and loading the contents of a file system
# Takes a list and turns it into a dictionary main purpose for turning contents of text file into a dictionary
def Save_Dictionary(dictionary, Keys, Dictionary):
	if dictionary[0] == "":
		if len(dictionary) > 1:
			Keys.append(dictionary[1])
			Save_Dictionary(dictionary[1:], Keys, Dictionary)
		else:
			print ("working")
	elif dictionary[0] == Keys[-1]:
		Dictionary[dictionary[0]] = []
		Save_Dictionary(dictionary[1:], Keys, Dictionary)
	else:
		Dictionary[Keys[-1]].append(dictionary[0])
		Save_Dictionary(dictionary[1:], Keys, Dictionary)
	
# file writing from Dicitonary
def Push_Dictionary(File,Keys, Dictionary):
	f= open(File, "w+")
	for key in Keys:
		f.write("\n" + key + "\n")
		for item in Dictionary[key]:
			f.write(item + "\n")
	f.close()

#end file reading
