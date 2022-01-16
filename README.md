# distributed-system
Distributed system project Reutlingen university WS 21/22
Made by Manuel Correa Gomez and Riccardo Terrenzi

## Description
Our application is composed by 3 services:
* AuthService
* GifService
* ChatService

And a database:
* MongoDB

## Functionalities
### AuthService
AuthService is a NodeJs service that provides authentication functionalities such as Login and Registration. 

We used Express to create our server because of the ease of use and versatility. We encrypt the passwords using Bcrypt in collaboration with Mongoose functionalities of “pre-save”.

We are aware that this service is not fully secured. We know that for proper deployment we have to provide TLS certification for the connections between client, server and database

### ChatService
It is a real-time communication service realised using NodeJS and Socket.io. We decided to use NodeJs and Socket.io because we were already familiar with both of them, also they will be easily scalable in the future, for example with Node Cluster and Socket.io Cluster adapter. 
We chose Socket.io in particular because it’s quite easy to implement, performant, but also reliable and scalable.

In our homepage it’s possible to see a real-time online-users list, chat with people and send every type of media.
Regarding the chat itself the bidirectional channel between the Socket.IO server (Node.js) and the Socket.IO client is established with a WebSocket connection, while Engine.IO is in charge of the low level connection between server and client.

More in detail we use the Socket.io rooms to organise the recipients, so, for example, the private chat is a room with just two users, while the global room is open to everybody.


### GifService
We decided to use Python’s Flask library with Docker as a example of a microservice that is just for serving media. It can also serve images but we took the inspiration of a service like Giphy.


We set it up in a way we can create a dynamic menu, approach of trendys gif and similar features can be implemented since when the user open the gif menu the device receives the name of the media in pages of N gifs. N is set with IMGS_PER_MENU_PAGE constant in main.py.

The pages are accessed by ``IP/menu/<int:page>`` and returns a simple JSON with the information
Once the file names has been received then they are asked to ``IP/media/<name>``

### Mongo
We used MongoDB to build a highly available and scalable chat application if it was needed in the future.
In order to achieve easy and fast developing we used MongoDB in collaboration with Mongoose library, which provides amazing features for queries.

### Docker
We have 4 Docker images and they are build by docker-compose.yml on 4 different services
* node: Here we have our node-js chat service working.
* gif-service: Here is the gif consulting and retrieving.
* auth: Here we have the authentication service running.
* mongo: We have our database with persistent storage.

## Instructions
Since we are using docker-compose it is easy to set up all the services.
```
sudo docker-compose build && sudo docker-compose up
```
After finishing building you can use the chat in http://0.0.0.0:3000/
