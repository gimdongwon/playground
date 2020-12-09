const express = require("express");
const app = express();

const port = 3100;

app.use(express.json());
app.use("/static", express.static("public"));

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.post("/", (req, res) => {
  console.log(req.body);
  res.send("Got a Post request");
});
app.put("/user", (req, res) => {
  res.send("Got a put request");
});
app.delete("/user", (req, res) => {
  res.send("Got a delete request");
});

app.listen(port, () => {
  console.log(`Listening Service at ${port}`);
});

console.log(__dirname);
