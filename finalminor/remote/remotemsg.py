import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("karan-Inspiron-3521",username='karan',password='k@ran')
stdin, stdout, stderr = client.exec_command('export DISPLAY=:0;notify-send "warning" "world"')




