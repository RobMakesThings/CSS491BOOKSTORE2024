This backend uses python running on fastapi for the HTTP server, SQL alchmey for interacting with SQL , faker for generating data, and lots of dependencies as well. 

debian base install on virtual box. 
Create project folder on desktop

virtual env with python to project folder
https://fastapi.tiangolo.com/
install fastapi and  uvicorn
install sqlalcmey 
I was using dbeaver, a GUI for databases-- to use it, you may need to add a user to the database using mariadb command line. 
using mariadb


mariadb connecter , sql alchemy , fastapi
starting services: 
systemctl start mariadb 

dbeaver connect
starting app-- reload for development
uvicorn backend:app -- reload

npm run dev for frontend. 
