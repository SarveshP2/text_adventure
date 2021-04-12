input1 = input("Do you want To play(yes/no)")
if input1 == "yes":
	input1 = input("you are the Detective theif is murdered a boy you want to investigate the murder (yes/no)")
	if input1 == "yes":
		input1 = input("thief is in the house you want go to (house/forest)")
		if input1 == "house":
			print("theif found thank you ")
		else:
			print("you lose")
	else:
		print("go and sleep")

else:
	print("Why you came to the case")