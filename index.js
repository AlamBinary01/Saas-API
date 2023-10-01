const express = require('express');
const bodyParser= require("body-parser")
const app = express();
require('dotenv').config()
const userRoutes = require('./api/routes/userRoute')
const mongoConnection= require("./api/config/databaseConnection")
const oriaCheck= require("./api/routes/oriaCheck")
const errorHandler= require("./api/middleware/errorHandling")
const port= process.env.PORT
const loginGoogle= require("./api/routes/loginGoogle")
const chatBot= require("./api/routes/chatbot")
// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use("/user", userRoutes);
app.use("/oria", oriaCheck);
app.use("/chat",chatBot)
app.use("/",loginGoogle)

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});