from pexpect import pxssh

ip= "10.98.228.146"
myusername= "root"
mypassword="Cms2023@Netas.iptv"


s = pxssh.pxssh()
if not s.login ('ip', '22','myusername', 'mypassword'):
    print ("SSH session failed on login.")
    print (str(s))
else:
    print ("SSH session login successful")
    s.sendline ('ls -l')
    s.prompt()         # match the prompt
    print (s.before)     # print everything before the prompt.
    s.logout()
