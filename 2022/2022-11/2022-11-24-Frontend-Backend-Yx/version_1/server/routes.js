let config = require('./config.json')
let mysql = require('mysql');
let e = require('express');
let { connect } = require('./server');

// TODO: fill in your connection details here
let connection = mysql.createConnection({
    host: config.rds_host,
    user: config.rds_user,
    password: config.rds_password,
    port: config.rds_port,
    database: config.rds_db
});
connection.connect();


// Route 1 (Player Info)
async function player(req, res) {
    var map = `*`
    var query = (req.query.id == "undefined" || ! req.query.id) ? 
    `SELECT ${map} from Players`:
    `SELECT ${map} from Players where PLAYER_ID = ${req.query.id}`;
    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

// Route 2 (Player Comparison)
async function playerCompare(req, res) {
    var sqlRun = `with
    a_team as (
      select distinct
      SEASON,
      TEAM_ID
      from Players
      where PLAYER_ID = ${req.query.ida}
    ),
    
    b_team as (
      select distinct
      SEASON,
      TEAM_ID
      from Players
      where PLAYER_ID = ${req.query.idb}
    ),
    
    a_home as (
      select distinct
      g.SEASON,
      g.GAME_ID,
      g.HOME_TEAM_WINS as A_WINS
      from Games g
      right join a_team a
      on g.SEASON = a.SEASON
      and g.HOME_TEAM_ID = a.TEAM_ID
      right join b_team b
      on g.SEASON = b.SEASON
      and g.VISITOR_TEAM_ID = b.TEAM_ID
    ),
    
    a_visitor as (
      select distinct
      g.SEASON,
      g.GAME_ID,
      1 - g.HOME_TEAM_WINS as A_WINS
      from Games g
      right join b_team b
      on g.SEASON = b.SEASON
      and g.HOME_TEAM_ID = b.TEAM_ID
      right join a_team a
      on g.SEASON = a.SEASON
      and g.VISITOR_TEAM_ID = a.TEAM_ID
    ),
    
    a_b_games as
    (
    select *
    from a_home
    union all
    select *
    from a_visitor
    )
    
    select distinct
    SEASON,
    count(distinct GAME_ID) as N_GAMES,
    count(distinct if(A_WINS = 1, GAME_ID, NULL)) as N_GAMES_A_WINS,
    count(distinct if(A_WINS = 0, GAME_ID, NULL)) as N_GAMES_B_WINS
    from a_b_games
    where SEASON is not null
    group by 1
    order by 1;`

    connection.query(sqlRun, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

// Route 3 (Top Team Win/Lose Against)
async function teamWinLoseMost(req, res) {
    var sqlRun = `with
    is_home_team as
    (
    select distinct
    SEASON,
    GAME_ID,
    HOME_TEAM_ID as TEAM_ID,
    VISITOR_TEAM_ID as OPPONENT_ID,
    HOME_TEAM_WINS as WINS
    from Games
    where HOME_TEAM_ID = ${req.query.id}
    ),
    
    is_visitor_team as
    (
    select distinct
    SEASON,
    GAME_ID,
    VISITOR_TEAM_ID as TEAM_ID,
    HOME_TEAM_ID as OPPONENT_ID,
    1 - HOME_TEAM_WINS as WINS
    from Games
    where VISITOR_TEAM_ID = ${req.query.id}
    ),
    
    base as
    (
    select *
    from is_home_team
    union all
    select *
    from is_visitor_team
    ),
    
    base_agg as
    (
    select distinct
    SEASON,
    OPPONENT_ID,
    COUNT(DISTINCT if(WINS = 1, GAME_ID, NULL)) as N_WINS,
    COUNT(DISTINCT if(WINS = 0, GAME_ID, NULL)) as N_LOSSES
    from base
    group by 1, 2
    ),
    
    base_agg_ranked as
    (
    select distinct
    SEASON,
    OPPONENT_ID,
    N_WINS,
    N_LOSSES,
    rank() over (partition by season order by N_WINS desc) as RANK_N_WINS_DESC,
    rank() over (partition by season order by N_LOSSES desc) as RANK_N_LOSSES_DESC
    from base_agg
    )
    
    select distinct
    SEASON,
    OPPONENT_ID,
    N_WINS,
    N_LOSSES
    from base_agg_ranked
    where RANK_N_WINS_DESC <= 3
    or RANK_N_LOSSES_DESC <= 3
    order by season, N_WINS desc;`

    connection.query(sqlRun, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function teamWinRate(req, res) {
    var sqlRun = `SELECT G.SEASON, ROUND(\
        SUM(CAST(G. HOME_TEAM_WINS AS FLOAT)) / \
        COUNT(CAST(G. HOME_TEAM_WINS AS FLOAT)),4)*100 \
        AS winning_rate \
        FROM games G \
        JOIN teams T \
        ON T.TEAM_ID = G.HOME_TEAM_ID \
        WHERE T.NICKNAME \
        LIKE "${req.query.team}" \
        OR T.ABBREVIATION LIKE "${req.query.team}" \
        GROUP BY G.SEASON\
    `
    connection.query(sqlRun, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function getConstructorLeaderboard(req, res) {
    let where = !req.query.year ? "" : `where year = ${req.query.year}`
    let query = `
        select cs.constructorStandingsId, cs.raceId, cs.constructorId, cs.position, cs.positionText, cs.wins,
        races.year, constructors.name, max(points) as points from constructorStandings cs
        left join races on cs.raceId = races.raceId
        left join constructors on cs.constructorId = constructors.constructorId
        ${where} 
        group by races.year, constructors.name
        order by races.year, points desc;
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function getDriverLeaderboard(req, res) {
    let where = !req.query.year ? "" : `where year = ${req.query.year}`
    let query = `
        select ds.driverStandingsId, ds.raceId, ds.driverId, max(ds.points) as points,
        ds.position, ds.positionText, ds.wins, races.year, CONCAT(forename,' ',surname) as fullName
        from driverStandings ds left join races
        on ds.raceId = races.raceId
        left join drivers on ds.driverId = drivers.driverId
        ${where}
        group by races.year, fullName
        order by races.year, points desc;    
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

// Performance of drivers in 2022 during the first lap since start
async function get2022Performance(req, res) {
    let where = !req.query.year ? "" : `where year = ${req.query.year}`
    let query = `
        select temp1.raceId, temp1.driverId, temp1.constructorId, grid, temp2.position as positionAfterLap
        from (select * from results where raceId >= 1074 and raceId <1085) as temp1
        left join (select * from lapTimes where raceId >= 1074 and raceId <1085 and lap =1) as temp2
        on temp1.raceId = temp2.raceId and temp1.driverId = temp2.driverId;
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function getBattle(req, res) {
    let where = !req.query.year ? "" : `where year = ${req.query.year}`
    let query = `
        select * from results
        left join races on results.raceId = races.raceId
        left join (select driverId, CONCAT(forename,' ',surname) as fullName from drivers) as tmp
        on results.driverId = tmp.driverId ${where};
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function getTop10RaceMost(req, res) {
    let query = `
        select CONCAT(forename,' ',surname) as driverName, count(races.raceId) as total from results join status on results.statusId = status.statusId
        join races on results.raceId = races.raceId
        join drivers on results.driverId = drivers.driverId
        join constructors on constructors.constructorId = results.constructorId
        join circuits on circuits.circuitId = races.circuitId
        group by driverName
        order by total desc
        limit 10;    
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function getTop10LapsMost(req, res) {
    let query = `
        select CONCAT(forename,' ',surname) as driverName, sum(laps) as total from results join status on results.statusId = status.statusId
        join races on results.raceId = races.raceId
        join drivers on results.driverId = drivers.driverId
        join constructors on constructors.constructorId = results.constructorId
        join circuits on circuits.circuitId = races.circuitId
        group by driverName
        order by total desc
        limit 10;    
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

async function getDriverMostPoints(req, res) {
    let query = `
        select year, CONCAT(forename,' ',surname) as driverName, sum(points) as total from results join status on results.statusId = status.statusId
        join races on results.raceId = races.raceId
        join drivers on results.driverId = drivers.driverId
        join constructors on constructors.constructorId = results.constructorId
        join circuits on circuits.circuitId = races.circuitId
        group by year, driverName
        order by total desc
        limit 1;
    `;

    connection.query(query, function (error, results) {
        if (error) {
            console.log(error);
            res.json({error: error});
        } else if (results) {
            if (results.length == 0) {
                console.log("Results have length 0!")
                res.json({results: []});
            } else {
                console.log(results);
                res.json({results: results});
            }
        }
    })
}

module.exports = {
    player,
    playerCompare,
    teamWinLoseMost,
    teamWinRate,
    getConstructorLeaderboard,
    getDriverLeaderboard,
    get2022Performance,
    getBattle,
    getTop10RaceMost,
    getTop10LapsMost,
    getDriverMostPoints
}