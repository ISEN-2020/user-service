# User Management

Uer Management is a microservice in the next-generation cloud-native library system.

## Installation / Run

Create Docker image whith source code.

```bash
docker build -t <IMAGENAME> .
```
Then run your docker image.

```bash
docker run -e MYSQL_DB_HOST=jdbc:mysql://192.168.43.228:3306/user?serverTimezone=UTC -e MYSQL_DB_USERNAME=root -e MYSQL_DB_PASSWORD=root -p 8080:8080 <IMAGENAME>
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


## Usage

Connect the microservice (docker:user-management) to the other.
The User Management microservice API is used for management of the client's DataBase (register,delete).
With a security level to check rights.

## Manual Installation
#### Prerequisite
Java 14.0.2 / Meaven v3.6.3

#### Commands
Create .jar file


```bash
mvn spring-boot:repackage
```

Run .jar file

```bash
java -jar ./target/user-management-1.0.0.jar
```



## Team
Development platform - PORTEIL CALLONICO DOL - Sept 2020

