import paramiko

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())

file=open("information.txt","r")
contents=file.read()
file.close()

for inf in contents.split("\n"):
    try:
        IP=inf.split("-")[0]
        user=inf.split("-")[1]
        passwd=inf.split("-")[2]
        print("IP: {}- {}- {}".format(IP,user,passwd))
        client.connect(IP,username=user,password=passwd)

        file=open("commands.txt","r")
        contents1=file.read()
        file.close()
        for command in contents1.split("\n"):
            stdin,stdoud,stderr=client.exec_command(str(command))
            print(stdoud.readlines())
        client.close()
    except:
        pass

