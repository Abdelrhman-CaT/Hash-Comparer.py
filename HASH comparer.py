you = input("Enter your HASH value -- > ")
auth = input("Enter authentic HASH value --> ")
print("\n");

if(auth.upper() == you.upper()):
	print("True\n")
else:
	print("False\n")