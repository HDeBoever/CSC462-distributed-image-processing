import sys, os, string, threading
import paramiko
outlock = threading.Lock()
def workon(host, letter):
	cmd = 'sudo docker run -e ID=' + letter + ' -v ~/efs-mount-point/split_images:/split_images -v ~/efs-mount-point/processed_split_images:/processed_split_images videoproject /bin/bash'
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, username='ec2-user', password='', key_filename='/home/ec2-user/ssh/testing2.pem')
	stdin, stdout, stderr = ssh.exec_command(cmd)
	stdin.write('ec2-user\n')
	stdin.flush()
	with outlock:
		print stdout.readlines()
def main():
	hosts = ['54.218.47.25', '34.222.23.75', ] # etc
	threads = []
	letters = ['A', 'B', 'C', 'D']
	i = 0
	for h in hosts:
		t = threading.Thread(target=workon, args=(h, letters[i]))
		i = i + 1
		t.start()
		threads.append(t)
	for t in threads:
		t.join()
main()
