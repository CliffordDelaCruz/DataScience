#strings.py
#Strings can be delimited by single or souble quotation marks (quotes have to match)

single_quote_string='data science'
double_quoted_string="data science"

tab_string = "\t"   # represents the tab character
len(tab_string)     # is 1

#to add backslashes as part of the string and not to format, use raw strings (r" ")
not_tab_string = r"\t"  #represents the characters '\' and 't'
len(not_tab_string)     # is 2

#you can create multiline strings
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

#f-string
first_name = "Clifford"
last_name = "Dela Cruz"

full_name1 = first_name + " " + last_name               #string addition
full_name1 = "{0} {1}".format(first_name, last_name)    #string.format

full_name3 = f"{first_name} {last_name}"