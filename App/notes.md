This backend uses python running on fastapi for the HTTP server, SQL alchmey for interacting with SQL , faker for generating data, and lots of dependencies as well. 

debian base install on virtual box. 

https://www.virtualbox.org/wiki/Linux_Downloads  
I chose debain 12
Create project folder on desktop

virtual env with python to project folder

im using vscode on the debian box for development, but maybe you could set up a shared folder if you want to do it on the main desktop. Or we can just integrate files. 

https://www.geeksforgeeks.org/python-virtual-environment/
https://fastapi.tiangolo.com/
https://www.sqlalchemy.org/

install fastapi and  uvicorn

install sqlalcmey 
I was using dbeaver, a GUI for databases-- to use it, you may need to add a user to the database using mariadb command line. 
using mariadb


mariadb connecter , sql alchemy , fastapi all need to be installed. Mariadb connector may or may not come with one of the other libraries. 
starting services: 
systemctl start mariadb 


starting app
uvicorn backend:app -- reload

once app is started, should be able to navigate to api docs page and can interact from there. its localhost:8000/docs for me. 

All of the current stuff is using get requests, im pretty sure this is bad for whatever reason. one task could be to change those to posts. 
authentication returns a JWT token . 
