a=input("input a character:-")
if a>="A" and a<="Z" or a>="a" and a<="z":
	print("alphabet")
elif a>="0" and a<="9":
	print("digit")
elif a=="@" or a=="#":
	print("special ")
else:
	print("not")