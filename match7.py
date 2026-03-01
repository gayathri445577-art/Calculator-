#Input dictionary and check:
#1 key → Small dict
#2–4 keys → Medium dict
#4 keys → Large dict
a={"a":"gaya","b":"anu","c":"chinnu","d":"reya"}
match len(a):
	case 1:
		print("small dict")
	case 2 | 3:
		print(" medium dict")
	case 4 | 5:
		print(" large dict")