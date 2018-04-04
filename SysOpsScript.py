import subprocess,sys,re,socket,os,shlex,csv

# validition function to check ip addresess before changing keys#
def valid_ip4_addr(ip):
	try: 
		socket.inet_aton(ip)
	except socket.error:
		return False
	return True

#checks to see if key being sent through ssh-copy-id has correct permissions#
#required either 400 or 600, otherwise this script will not work without requring a password# 
def valid_permission(authorized_key,keyPath):
	args = ["stat","-c '%a'", keyPath]
	permission = subprocess.check_output(args)
	return '400' in permission or '600' in permission

#initialize vars#
key = "authorized_key_exercise.pub"
keyPathLocal = os.path.abspath(key)
outputArr = []

#commands to be executed on server#
hostCommand = "hostname"
ipCommand = "hostname -I"
mtimeCommand = "ls -l ~/.ssh/authorized_keys" 
atimeCommand = "ls -lu ~/.ssh/authorized_keys"
ctimeCommand = "ls -lc ~/.ssh/authorized_keys"
updatedKeyCommand = "cat ~/.ssh/authorized_keys"
commandList = [hostCommand,ipCommand,mtimeCommand,ctimeCommand,atimeCommand,updatedKeyCommand]
command = " && ".join(commandList)

#main#
if not valid_permission(key,keyPathLocal):
	print("Authorized key file does not have correct permissions (400) or (600)")
	print("System exiting")
	sys.exit()
for line in sys.stdin:
	ip = re.sub('/s+','',line.strip('\n\r'))
	if not valid_ip4_addr(ip):
		print("ip is not in valid ip4 format " + ip)
	#	continue
	#   would skip over unvalid_ip4 addresses but I need my ipv6 for test purposes
	scpCommand = "ssh-copy-id -i " + keyPathLocal + " " + ip 
	os.system(scpCommand)
	args = ['ssh','-T',ip] # -T option prevents a pseudo-terminal allocation
					  	   # that interrupts with stdin in subprocess
	process = subprocess.Popen(args,stdin=subprocess.PIPE,
									stdout=subprocess.PIPE) #forks a new process
															#given new file discriptors stdin,stdout
	output = process.communicate(input= command)[0] #closes stdin
	outputArr.append(re.sub('\n','\n,',output.lstrip('\n').rstrip('\n')))
	process.wait() #waits for child process to end

with open("output.csv", "wb") as myfile:
	wr = csv.writer(myfile)
	wr.writerow(outputArr)