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
10) Repeat steps 9 to 12 BUT select ONLY "Routes"

### Setting up Kong API Admin account
1) Username: admin
2) Email: <your email address>
3) Password: adminadmin
4) Sign in using the account created
5) Create new connection; using Name: Default and Kong Admin URL: http://kong:8001