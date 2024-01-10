const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

// Simple user and admin database (for example purposes)
const users = {
    'user': { 'password': 'userpassword' },
    'admin': { 'password': 'adminpassword' }
};

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    if (username in users) {
        if (password === users[username].password) {
            if (username === 'admin') {
                res.redirect('/admin');
            } else {
                res.redirect('/welcome');
            }
        }
    } else {
        res.redirect('/');
    }
});

app.get('/welcome', (req, res) => {
    res.sendFile(path.join(__dirname + '/welcome.html'));
});

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname + '/admin.html'));
});

app.get('/video.html', (req, res) => {
    const room = req.query.room;
    res.sendFile(path.join(__dirname + '/video.html'), { room: room });
});

app.get('/contact.html', (req, res) => {
    res.sendFile(path.join(__dirname + '/contact.html'));
});

module.exports = app; // Export the app object