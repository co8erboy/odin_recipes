#!/usr/bin/env python3

def steps_format():
	condition = True
	str = ""
	while condition == True:
		content = input("paste step: ")
		if content != "":
			str += "<li>{}</li>\n".format(content)
		else:
			condition = False
	print(str)

#steps_format()

def ingredients_format(text):
	lst = text.split("\n")
	str = ""
	for i in lst:
		print("<li>" + i + "</li>")
		#print(str.format("<li>{}</li>\n",i))
		#str += str.format("<li>{}</li>\n",i)
	print(str)
#ingredients_format()