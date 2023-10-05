import time
from datetime import datetime as f

host_temp = 'hosts' # to test the program as we need adminstartive privilage to run the host_path file
host_path = "/etc/hosts"
redirect = '127.0.0.1' #we can creat a redirect to this site ot create a random page online to redirect the user to read
banned_list = ['www.facebook.com', 'facebook.com', 'x.com', 'www.twitter.com'] #pages i banned to give me access to focus

while True:

    if f(f.now().year, f.now().month, f.now().day,8) < f.now() < f(f.now().year, f.now().month, f.now().day,13):
        print('Working Hours')
        with open(host_path, 'r+') as file:
            content = file.read()
            #print(content)
            for web_site in banned_list:
                if web_site in content:
                    pass
                else:
                    file.write(redirect+' '+ web_site+'\n')
    else:
        with open(host_path, 'r+') as file:
            cont = file.readlines()
            file.seek(0)
            for line in cont:
                if not any(web_site in line for web_site in banned_list):
                    file.write(line)
            file.truncate()
        print('Fun Time!!')
    time.sleep(10)

