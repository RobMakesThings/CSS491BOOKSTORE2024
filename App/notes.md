started 1/15

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



got read / search done with basic execute statmenrs, this sort of thing will be most likely subect to securtity issues such as sql injection. paramaterizati is super important. 

python -- fast api for backend, and uvicorn server. Fastapi is based on starlette and claims to be fast. DOes basic API docs for you and seems to offer some security protection via pydantic. 

frontend talks to backend in JSON and JWT for authentication
frontend primevue template based on vue JS, using vite as a server. -- it has nice documentation but not the best popularity. Developed by a guy in turkey from what i can tell. 

PrimeVue template 
done 1/29

todo: 
suppliers need to have a list of books they carry, or each book needs to have a supplier that carries it, storing that data may be complicated if there are more than one supplier to a book. 
get muliplte selections to work. 
Bulk edits. 
!! half done -- Integrate a customer, order , and supplier tables. 

make descripton fields, and placeholder images in database.< can do descrioptons with faker<< done 2/15
Cusotmer frontend! 
SHop functionality. - frontend adds titles to cart,
 submits a list of titles to backend, along with payment verification, or Cash on pickup option or something. 

Reviews can do with faker as well 

# users need auth. will need to add cookie req to backend, and cookies to front. 
Make standalone pages for Orders, Books  < done 2/15 
# need to add support for multiple books in here. 
## pages for employee backend
Catalog-- searches books and can show individual title with description < done 2/15 - add to c
Orders -- Manage and view orders -- VIew individual orders.<<done 215>todo: Mark orders as completed. 
Edits/Inventory-- CRUD and stock managment
Suppliers -- Contact info and basically a catalog 
Use faker to generate data < done 
# need to add support for multiple books in here. 
# needs to send each title to orderItems table. make cart object 

Create order pages -- Order overviews, links to Order details with products , prices, etc. 

create product  pages and make a search to product list to prodct details flow. 

Add stock numbers and stock managment, and completed/ processing statuses to order. order dashboard for updates there. 

Mark order completed

2/20 adding auth based on fast api examples. seems like JWT should integrate well with VUE
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-dependencies
updated all users passwords to a hash, so from now on we'll be working with hashes. 

3/2
worked through issues with basic logins. Have it working in some shape or form based on example provided by fast api
add permissions to some endpoints of API? customer level can place orders view books. employee can view orders and customers, manage stock numbers?, manager can add users and manage books? 
now need to get going on integrating auth with frontent, 


todo:

change to post requests for options that change data. keep gets for gets, duh
frontend authorization. 