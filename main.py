# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
def read_file_content(story):
    # [assignment] Add your code here 
    with open(story, 'r') as p:
        file = p.read()

    return (file)

output = read_file_content("story.txt")
print(output)

def count_words():
    text = open("story.txt", "r")
    d = dict()
    for line in text:
	    line = line.strip()

	    line = line.lower()

	    line = line.translate(line.maketrans("", "", string.punctuation))
	    words = line.split(" ")

	    for word in words:
		    if word in d:
			    d[word] = d[word] + 1
		    else:
			    d[word] = 1

    for key in list(d.keys()):
	    print(key, ":", d[key])

count_words()
