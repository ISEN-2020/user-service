# User Management

Uer Management is a microservice in the next-generation cloud-native library system.

## Installation / Run

Create Docker image whith source code.

```bash
docker build -t <IMAGENAME> .
```
Then run your docker image.

```bash
docker run <IMAGENAME> .
```

## Usage

Connect the microservice (docker:user-management) to the other.
The User Management microservice API is used for management of the client's DataBase (register,delete).
With a security level to check rights.

## Manual Installation
####Prerequisite
Meaven v3.6.3 / OpenJDK v14.02 / Java

####Commands
Create .jar file

```bash
mvn spring-boot:repackage
```

Run .jar file

```bash
java -jar ./target/user-management-1.0.0.jar
```



## Team
Devellopment platform - PORTEIL CALLONICO DOL - Sept 2020
