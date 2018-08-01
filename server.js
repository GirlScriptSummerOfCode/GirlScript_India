var express=require('express');
var app=express();
var port=process.env.PORT || 8080
app.use(express.static(_dirname));
app.get("/", fuction(req,res)
{
    res.render("canvas");
})
app.listen(port,fuction())
{
    console.log("app running");
}