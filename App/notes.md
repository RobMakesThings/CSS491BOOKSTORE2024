This backend uses python running on fastapi for the HTTP server, SQL alchmey for interacting with SQL , faker for generating data, and lots of dependencies as well. Its bascially an API for books, orders users, and all that stuff. A frontend would just need to talk to this API to display stuff. Its got an interactive documtation system thats really helpful for figuring out what code needs to do. 

debian base install on virtual box. 
install virtual box, then can install debain using an ISO from debians website. https://www.debian.org/download


I chose debain 12, but might switch to debain 11 cause that one seems to be more avaialble on cloud providers. 
11 uses python 3.9, which i have to change a few lines of code to use. might not be a big deal. 


install using ISO by creating a new machine. Settings i chose were 30gb disk, 4 cores, and 4196 of RAM. . i like to make sure guest additions are available for drag and drop and other conviences. 
Installing may take a few minutes. 

Create project folder on desktop
Debian is kinda wierd IMO, no sudo by defailt, you can switch to root user and just omit sudo commands, or add yourself to sudoers group while root user. either works find. \

Install code. 
https://code.visualstudio.com/docs/setup/linux has the instructions, and download. 


virtual env with python to project folder
https://linuxconfig.org/how-to-set-up-a-python-virtual-environment-on-debian-10-buster is a good one. 
or maybe 
https://www.geeksforgeeks.org/python-virtual-environment/


im using vscode on the debian box for development, but maybe you could set up a shared folder if you want to do it on the main desktop. Or we can just integrate files. 

https://fastapi.tiangolo.com/
https://www.sqlalchemy.org/
-
##install dependencies in virtual env with pip##

pip install fastapi
pip install sqlalchemy
pip install faker for data creation
can extract files in this folder to project file that we set up the virtual ENV in. 


install mariaDB
apt install mariadb-server
and mariadb connector 
https://mariadb.com/docs/server/connect/programming-languages/c/install/#Installation_via_Package_Repository_(Linux)
$ sudo apt install libmariadb3 libmariadb-dev
had to install python3-dev to get mariaDB python installed 


pip install mariadb
https://mkyong.com/mysql/how-to-install-mariadb-on-debian-11/ has some steps. also 
once maria db installed add user for API 


I was using dbeaver, a GUI for databases for managing and looking at the database. A little easier than command line. although should be able to create database there  as well. 
using mariadb
copy paste schema



mariadb connecter , sql alchemy , fastapi all need to be installed. Mariadb connector may or may not come with one of the other libraries. 
starting services: 
systemctl start mariadb 
need to run schema to create tables, users, etc. 



starting app
uvicorn backend:app -- reload

once app is started, should be able to navigate to api docs page and can interact from there. its localhost:8000/docs for me. 

All of the current stuff is using get requests, im pretty sure this is bad for whatever reason. one task could be to change those to posts. 


authentication returns a JWT token . 
