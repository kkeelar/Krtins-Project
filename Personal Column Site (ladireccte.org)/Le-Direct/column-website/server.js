const express = require('express');
const bodyParser = require('body-parser');
const admin = require('firebase-admin');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

const serviceAccount = require(path.join(__dirname, 'ledirect-d1772-firebase-adminsdk-h47yz-a73183a5f6.json'));

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'login.html'));
});

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'admin.html'));
});

app.get('/adminJoe', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'adminJoe.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
