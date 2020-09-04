import re
line =" This is a practice test"
match=re.match(r'(.*) is (.*?).*',line,re.M|re.I)
if match:
    print("match.group",match.group())
    print("match.group", match.group(1))
else:
    print("No Match")
