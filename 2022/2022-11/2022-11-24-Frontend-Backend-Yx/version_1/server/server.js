const express = require('express');
const mysql = require('mysql');
var cors = require('cors')

const routes = require('./routes')
const config = require('./config.json')

const app = express();

// whitelist localhost 3000
app.use(cors({ credentials: true, origin: ['http://localhost:4821'] }));

// Route 1 - register as GET 
app.get('/players', routes.player)

// Route 2 - register as GET 
app.get('/playerCompare', routes.playerCompare)

// Route 3 - top team win/lose againt
app.get('/teamWinLoseMost', routes.teamWinLoseMost)

// Route 3 - top team win/lose againt
app.get('/teamWinRate', routes.teamWinRate)

app.get('/getDriverMostPoints', routes.getDriverMostPoints)

app.get('/get2022Performance', routes.get2022Performance)

app.get('/getBattle', routes.getBattle)

app.get('/getTop10RaceMost', routes.getTop10RaceMost)

app.get('/getTop10LapsMost', routes.getTop10LapsMost)

app.get('/driverLeaderboard', routes.getDriverLeaderboard)

app.get('/constructorLeaderboard', routes.getConstructorLeaderboard)

app.listen(config.server_port, () => {
    console.log(`Server running at http://${config.server_host}:${config.server_port}/`);
});

module.exports = app;
Solve[
    {
     r12 + r13 + r14 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r21 + r23 + r24 + r25 + r26 + r27 + r28 + r29 + r20 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     r11 + r12 + r13 + r15 + r16 + r17 + r18 + r19 + r10 == 1,
     }
    ]