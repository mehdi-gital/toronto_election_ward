const express = require('express')
const app = express()
const assert = require('assert');

var bodyParser = require('body-parser')
app.use( bodyParser.json() );      
app.use(bodyParser.urlencoded({     
  extended: true
})); 
app.use(bodyParser.text({ type: 'text/html'}));

const MongoClient = require('mongodb').MongoClient;
const dbUrl = "mongodb://localhost:27017";

const redisClient = require('redis').createClient;
const redis = redisClient(6379, 'localhost');

MongoClient.connect(dbUrl, (err, database) => {
    assert.equal(null, err);
    db = database.db('Main');
    console.log('Connected to mongodb on port 27017');
    
});

const PORT = 3000

app.get('/myapp', (req,res) => {
    res.send('Hello world!');
});

app.get('/graph', (req, res) => {
    res.sendFile('../assets/graph.html', {root: __dirname});
});

app.get('/query', (req, res) => {
    var stream = db.collection('tweets').find({}).stream();

    stream.on('data', (data) => {
        res.write(JSON.stringify(data));
    });
    stream.on('end', () => {
        res.end();
    });
});

app.post('/echo', (req,res) => {
    console.log(req.body);
    res.send(req.body);
})

app.post('/query', (req,res) => {
    var stream = db.collection('tweets').find(req.body).stream();

    stream.on('data', (data) => {
        res.write(JSON.stringify(data));
    })
    stream.on('end', () => {
        res.end();
    })
})

app.listen(PORT, () => {
    console.log("Server listening on port " + PORT);
});

