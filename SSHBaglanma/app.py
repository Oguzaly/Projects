# from pexpect import pxssh
# ip= "***"
# myusername= "***"
# mypassword="***"
# s = pxssh.pxssh()
# if not s.login ('ip', '22','myusername', 'mypassword'):
#     print ("SSH session failed on login.")
#     print (str(s))
# else:
#     print ("SSH session login successful")
#     s.sendline ('ls -l')
#     s.prompt()         # match the prompt
#     print (s.before)     # print everything before the prompt.
#     s.logout()
import paramiko
host = "***"
port = ***
username = "***"
password = "***"
command = "cd /data/;find . -name '*.vtt' -type f >> /home/deneme.txt"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
