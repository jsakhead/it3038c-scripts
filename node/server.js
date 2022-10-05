const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

var ut_sec = os.uptime();
var ut_day = ut_sec/86400
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
   
ut_sec = Math.floor(ut_sec);
ut_day = Math.floor(ut_day);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
  
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;

var total_memory = os.totalmem();
var total_mem_in_kb = total_memory/1024;
var total_mem_in_mb = total_mem_in_kb/1024;

total_mem_in_mb = Math.floor(total_mem_in_mb);
toal_mem_in_mb = total_mem_in_mb%1024;

var free_memory = os.freemem();
var free_mem_in_kb = free_memory/1024;
var free_mem_in_mb = free_mem_in_kb/1024;

free_mem_in_mb = Math.floor(free_mem_in_mb);
free_mem_in_mb = free_mem_in_mb%1024;

const cpuCount = os.cpus().length

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${ut_day} Day(s) ${ut_hour} Hour(s) 
         ${ut_min} minute(s) and  
       	 ${ut_sec} second(s) </p>
        <p>Total Memory: ${total_mem_in_mb} MB </p>
        <p>Free Memory: ${free_mem_in_mb} MB </p>
        <p>Number of CPUs: ${cpuCount} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");