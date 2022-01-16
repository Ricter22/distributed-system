const path = require('path');
const http = require('http');
const express = require('express');
const bcrypt = require('bcrypt');
const cors = require('cors');

//Database connection
const mongoose = require('mongoose');

//chat-db or localhost
mongoose.connect('mongodb://chat-db:27017/TEST', {
    useNewUrlParser: true,
    
}).then(()=>{
    console.log('Database connected...');
}).catch(err=>{
    console.log(err);
    })

const userFromDb = require('./models/userModelDb');

const app = express();
const server = http.createServer(app);
//const io = socketio(server);

// Set static folder
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({extended : true}));
app.use(express.json());
app.use(cors());

app.post('/register', function(request, response){
    let username = request.body.username;
    let password = request.body.password;
    //let image = request.body.file;
    
    userFromDb.findOne({'username': username/*, 'password':password*/}, function(err, result){
            if(err){ console.log("Error with the database");};
            
            if(result!=null){
                return response.status(422).send({'msg':'user already registered'});
            }
            else{
                const userSavedInDb = new userFromDb({username:username, password:password/*, image:image*/});
                userSavedInDb.save();
                response.status(200).send({'msg':'succesful'});
            }
        })
});

app.post('/auth', function(request, response) {
    let username = request.body.username;
    let password = request.body.password;
    

    //here we search the username in the database, if we find it we search 
    //his encrypted password and compare it with the password that we receive from the post
    userFromDb.findOne({'username': username}, function(err, result){
        if(err){ console.log("Error with the database");};

        if(result==null){
            return response.status(422).send({'msg':'user not registered'});        }
        else{   
            result.comparePassword(password, function(err, isMatch) {
                if (err){console.log(err)} 
                //console.log(password, isMatch);
                if (isMatch){
                    response.status(200).send({'msg':'user signed in'});
                }else{
                    return response.status(422).send({'msg':'Wrong password'});                }
            });
        }
    })
});

const PORT = 8080 || process.env.PORT;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));