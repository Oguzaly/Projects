import paramiko
import requests
import psycopg2
from openpyxl import Workbook,load_workbook
from time import sleep
import sys
import asyncio
import os
import subprocess, os

host = "10.98.225.178"
port = 22
username = "root"
password = "Cms2023@Netas.iptv"

# command = "cd /home/sa-oguzhan.alyaz/iceriktest/;ls -ltr"
#
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# stdin, stdout, stderr = ssh.exec_command(command)
# lines = stdout.readlines()
# print(lines)
db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'



conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

#    cur.execute("select status,count(*) from atlas_cms_vod.plan_profile where content_id in (select id from atlas_cms_vod.content where parent_series_id ='4165173' or id ='4165173') group by status")
cur.execute("select guid from atlas_cms_vod.content where parent_series_id ='4164614' or id ='4164614'")

frsh =cur.fetchall()
for i in frsh:
    print(i[0])
    #print('ffmpeg -i /mnt/atlas/www/contents/'+'{}'.format(i[0])+'/*.mpg  2>&1 |egrep "Input|Duration"')
    #command ='cd /mnt/atlas/www/contents/'+'{}'.format(i[0])+';ls'
    command ='ffmpeg -i /mnt/atlas/www/contents/'+'{}'.format(i[0])+'/*.mpg  2>&1 |egrep "Duration"'

    stdin, stdout, stderr = ssh.exec_command(command)
    line = stdout.readlines()

    p = subprocess.Popen(line,stdout=subprocess.PIPE,shell=False)
    lines = p.communicate()
    print(lines.readlines())
