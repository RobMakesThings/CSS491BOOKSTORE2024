# CSS491BOOKSTORE2024
Backend setup
Full setup is in setup.md in the app folder

This backend uses python running on fastapi for the HTTP server, SQL alchmey for interacting with SQL , faker for generating data. Its bascially an API for books, orders users, and all that stuff. A frontend would just need to talk to this API to display stuff. Its got an interactive documtation system thats really helpful for figuring out what code needs to do.

I built this on linux install using debian 12. I use virtualbox, but this should work on other platforms after an operating system is installed.

Ive included instructions for installing the image, which is probably way easier. Its an open format so maybe it works with other stuff if you like VMware or something.
OVF image:
https://drive.google.com/drive/folders/1AB2iiTNsk-eXsO5IHcn__IR_gzqCF-5R?usp=sharing 

https://www.virtualbox.org/

Install OVF image
in virtual box:  File > import appliance and choose image. make sure to choose a base folder that has some free space.
start machine and login. password is password for user

open project folder in code in terminal it would be :

code ./Desktop/project/bookstore
starting app, inside of vs code. navigate to python file and press play button in top right , in the terminal window opened, run the following

uvicorn backend:app -- reload
once app is started, should be able to navigate to api docs page and can interact from there. its localhost:8000/docs for me.
I have uploaded so far the backend documents. 

Overall, the app should be able to display a library of books, and be able to make a cart of books to checkout. I dont think integrating a payment processing service makes any sense at all. 

![Screenshot from 2024-06-15 19-17-49](https://github.com/mastaginger/CSS491BOOKSTORE2024/assets/51903522/75447ba6-e072-46bc-8967-f4d18dcdc00b)
 This is the screenshot of the backend api docs up and running. Inside of the next folder there are some super basic directions for setting everything up. 
 
![Capture](https://github.com/mastaginger/CSS491BOOKSTORE2024/assets/51903522/a41a9c92-9807-43f0-ac00-188976877bca)
