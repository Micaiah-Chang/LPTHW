from passlib.hash import bcrypt

def encrypt_this(password):
	return bcrypt.encrypt(password, rounds = 10)

def verify_this(password,hash):
	return bcrypt.verify(password,hash)
	
if __name__ == "__main__":
	
	while True:
		password = raw_input("Please enter a test password: ")
		hash = encrypt_this(password)
		print "Your hash is", hash
		password = raw_input("Retype your password to be verified: ")
		# print string(verify_this(password))
		if verify_this(password, hash)==True:
			print "Congrats! You retyped your password!"
		else:
			print "Incorrect password."
		if raw_input("Do you want to try again? Y/N\t") == "No":
			break 