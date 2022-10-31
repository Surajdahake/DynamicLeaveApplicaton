print("------------Dynamic Leave Application----------")

from datetime import date

try:

	name=input("Enter Your Name : ")
	teacher=input("Enter Teacher Name : ")
	today = date.today()
	lt=input('''Enter Leave Tenure : ''')
	clas=int(input("Enter Class : "))
	section=input("Enter Section : ")
	Subline=input("Enter Subject Line : ")
	Reason=input('''Enter Reason : ''')

	print(f'''	Name: {name}
	Teacher Name: {teacher}
	Date of Application : {today}
	Leave Tenture : {lt}
	Class : {clas}
	Section : {section}
	Subject Line : {Subline}
	Reason : {Reason}''')

except NameError:
	print("You Entered Something wrong")
except ValueError:
	print("Integer Value only")
except SyntaxError:
	print("You Entered Something wrong")