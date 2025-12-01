const express = require('express');
const path = require('path');
const app = express();
const port = 8080;

app.set('view engine','ejs');
app.set('views',path.join(__dirname,'views'));

app.use(express.static(path.join(__dirname,'public')));

app.get('/',(req,res) =>{
    console.log('Index');
    res.render('index');
});

app.get('/blog',(req,res) => {
    console.log('Here');
    res.render('blog',{text:'World'});
});

app.listen(port,() =>{
    console.log(`App is runnin at http://localhost:${port}`)
});
