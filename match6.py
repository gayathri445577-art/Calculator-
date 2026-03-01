#Input color:
#"red" → Stop
#"yellow" → Ready
#"green" → Go
colour=input("enter the colour").strip( )
match colour:
	case "red":
		print("stop")
	case " yellow":
		print(" ready")
	case "green":
		print("go")