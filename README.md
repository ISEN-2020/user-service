# User Management

Uer Management is a microservice in the next-generation cloud-native library system.

## Prerequisites
You need to have on your computer :
MySQL click on the following link to download it
https://dev.mysql.com/downloads/installer/

Docker Desktop
https://www.docker.com/products/docker-desktop


## Installation / Run

Create Docker image whith source code.

```bash
docker build -t <IMAGENAME> .
```
Then run your docker image.

In order to run your docker image you need to have a running database on your computer (cf "Setup Database section below)

You need to get your computer IP to do so, open a terminal and run the following command:

```bash
ipconfig
```

The info you're looking for is called IPv4 address, right down the corresponding numbers


```bash

docker run -e MYSQL_DB_HOST=jdbc:mysql://<YOUR_COMPUTER_IP>:3306/user?serverTimezone=UTC -e MYSQL_DB_USERNAME=root -e MYSQL_DB_PASSWORD=root -p 8080:8080 <IMAGENAME>
```

## Setup Database

Start MySQL 

```bash
mysql -h localhost -u root -p
```

In MySQL cmd, start scipt DataBase constructor

```bash
source <SQL FILE>
```

In MySQL Workbench you need to change the "User and Privileges" of your user "root".
Under the section "User and Privileges"  clik on "root" on the right panel, change the parameter "Limit to Hosts Matching" to "%", click "Apply".


## Usage

Connect the microservice (docker:user-management) to the other.
The User Management microservice API is used for management of the client's DataBase (register,delete).
With a security level to check rights.

### **Create User :**

#### **Request :**

```bash
POST http://localhost:8080/saveUser
```

```bash
{
    "name": "john",
    "emailAddress": "john@gmail.com",
    "password": "johnpwd"
}
```

#### **Response :**

```bash
200 OK
```

```bash
NO BODY
```

### **List User :**

#### **Request :**

```bash
GET http://localhost:8080/getUsers
```

```bash
NO BODY
```

#### **Response :**

```bash
200 OK
```

```bash
[
    {
        "id": 9,
        "name": "john",
        "emailAddress": "john@gmail.com",
        "password": "johnpwd",
        "enabled": true,
        "role": "ROLE_USER"
    },
    {
        "id": 10,
        "name": "john2",
        "emailAddress": "john2@gmail.com",
        "password": "john2pwd",
        "enabled": true,
        "role": "ROLE_USER"
    },

    ...

]
```

### **Delete User :**

#### **Request :**

```bash
POST http://localhost:8080/deleteUser
```

```bash
9
```

#### **Response :**

```bash
200 OK
```

```bash
{
    "id": 9,
    "name": "john",
    "emailAddress": "john@gmail.com",
    "password": "johnpwd",
    "enabled": true,
    "role": "ROLE_USER"
}
```


## Manual Installation
#### Prerequisite
Java 14.0.2 / Meaven v3.6.3

#### Commands
Create .jar file


```bash
mvn spring-boot:repackage
```

if the above command is not working, try the following one :

```bash
mvn clean install spring-boot:repackage
```

Run .jar file

```bash
java -jar ./target/user-management-1.0.0.jar
```
## Team
Development platform - LEFEVRE DESPRES GONIN - Sept 2021

