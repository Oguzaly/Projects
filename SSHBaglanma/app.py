# from pexpect import pxssh
#
# ip= "10.98.228.146"
# myusername= "root"
# mypassword="Cms2023@Netas.iptv"
#
#
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

host = "10.98.228.146"
port = 22
username = "root"
password = "Cms2023@Netas.iptv"

command = "ls -ltr"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
