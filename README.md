# Installation for Windows Users
Please follow the following instructions if your are running on a Windows machine

## Running containers to setup Micro-services and Complex Micro-services
1) cd backend
2) docker-compose build
3) docker-compose up

## Bootstrapping the database with the required data
1) Run WampServer 
2) Go to phpMyAdmin
3) Log in
4) Click on "Import" tab on the landing page
5) Select on "databases.sql" file
6) Check if the required information has been bootstrapped into the database
7) Click User accounts
8) Click Add user account and specify the following:
    User name: (Use text field:) is123
    Host name: (Any host) %
    Password: Change to No Password
9) Select Data, this will check SELECT, INSERT, UPDATE, DELETE, FILE
10) Click Go and a new user: is213 will be added. This will allow remote access to the database

## Setting up Kong API Gateway
1) Go to localhost:1337
2) Log in to Kong using Admin details. If no account, setup Admin account using details provided.
3) Click on the "Snapshots" tab
4) Click on "Import"
5) Select "studyBuddyAPIGateway.json" and import
6) Click on "Details" of the newest snapshot
7) Click on "Restore"
8) Select everything except "Routes"
9) Click on "Import Objects"
10) Repeat steps 6 to 9 BUT select ONLY "Routes"

### Setting up Kong API Admin account
1) Username: admin
2) Email: <your email address>
3) Password: adminadmin
4) Sign in using the account created
5) Create new connection; using Name: Default and Kong Admin URL: http://kong:8001

### Limitations
Due to the limitation of the API, in order to call the Imgur API, it must be called from 127.0.0.1.
This issue will be avoided if we use a domain name.


# Installation for Mac Users
Please follow the following instructions if your are running on a Windows machine

## Running containers to setup Micro-services and Complex Micro-services
1) cd backend
2) docker-compose build
3) docker-compose up

## Bootstrapping the database with the required data
1) Run MampServer 
2) Go to phpMyAdmin
3) Log in
4) Click on "Import" tab on the landing page
5) Select on "databases.sql" file
6) Check if the required information has been bootstrapped into the database
7) Click User accounts
8) Click Add user account and specify the following:
    User name: (Use text field:) is123
    Host name: (Any host) %
    Password: Change to No Password
9) Select Data, this will check SELECT, INSERT, UPDATE, DELETE, FILE
10) Click Go and a new user: is213 will be added. This will allow remote access to the database

## Setting up Kong API Gateway
1) Go to localhost:1337
2) Log in to Kong using Admin details. If no account, setup Admin account using details provided.
3) Click on the "Snapshots" tab
4) Click on "Import"
5) Select "studyBuddyAPIGateway.json" and import
6) Click on "Details" of the newest snapshot
7) Click on "Restore"
8) Select everything except "Routes"
9) Click on "Import Objects"
10) Repeat steps 6 to 9 BUT select ONLY "Routes"

### Setting up Kong API Admin account
1) Username: admin
2) Email: <your email address>
3) Password: adminadmin
4) Sign in using the account created
5) Create new connection; using Name: Default and Kong Admin URL: http://kong:8001

### Limitations
Due to the limitation of the API, in order to call the Imgur API, it must be called from 127.0.0.1.
This issue will be avoided if we use a domain name.