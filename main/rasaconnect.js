const express = require('express')
const app = express()
const port = 3000
const path = require('path');
const bodyParser = require("body-parser"); 
app.use(bodyParser.urlencoded({extended:false}));
app.use(express.json());
const axios = require('axios');

app.post('/',(req,res) => {
        var abcd = req.body.user;
        console.log("message here ->",abcd);
        const postData = {
            message: abcd
        }
        axios.post("http://192.168.51.90:5005/webhooks/rest/webhook",postData).then((response)=>{
        var resp = response.data[0]['text'];
        console.log('response',resp);
        const modifiedhtml = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RASA Bot</title>

</head>
<body>
    <form method="post" action="/">
        <input type="text" name="user" placeholder="Enter a value">
        <button type="submit" >submit</button>
    </form>
    <br>
    <button id="voicebtn"> Voice </button>
    <br>
    <p>${resp}</p>
    <br>
    <script src="/js/speech.js" type="text/javascript"></script>
</body>
</html>`;
    if (req.body.voice == true) { res.send(response.data[0]); }
    else { res.send(modifiedhtml); } 
        })
})

app.use('/js', express.static(path.join(__dirname, 'js')));

app.get("/",(req,res) => {
    res.sendFile(path.join(__dirname,'/index.html'))
})

app.listen(port, () => {
    console.log("backend has started listening")
})

