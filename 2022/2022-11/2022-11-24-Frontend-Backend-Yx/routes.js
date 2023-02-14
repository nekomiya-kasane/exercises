const config = require('./config.json')
const mysql = require('mysql');
const e = require('express');

// DONE: fill in your connection details here
const connection = mysql.createConnection({
    host: config.rds_host,
    user: config.rds_user,
    password: config.rds_password,
    port: config.rds_port,
    database: config.rds_db
});
connection.connect();


// ********************************************
//            SIMPLE ROUTE EXAMPLE
// ********************************************

// Route 1 (handler)
async function hello(req, res) {

    connection.query(`SELECT *  
    FROM status`, function (error, results, fields) {

        if (error) {
            console.log(error)
            res.json({ error: error })
        } else if (results) {
            res.json({ results: results })
        }
    })

    return

    // Convert all queries to lowercase without deleting the original ones
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }

    // a GET request to /hello?name=Steve
    if (req.query.name) {
        res.send(`Hello, ${req.query.name}! Welcome to the FIFA server!`)
    } else {
        res.send(`Hello! Welcome to the FIFA server!`)
    }
}


// ********************************************
//                  WARM UP 
// ********************************************

// Route 2 (handler)
async function jersey(req, res) {

    // Convert all queries to lowercase without deleting the original ones
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }

    const colors = ['red', 'blue', 'white']
    const jersey_number = Math.floor(Math.random() * 20) + 1
    const name = req.query.name ? req.query.name : "player"

    if (req.params.choice === 'number') {
        // DONE: TASK 1: inspect for issues and correct 
        res.json({ message: `Hello, ${name}!`, jersey_number: jersey_number })
    } else if (req.params.choice === 'color') {
        var lucky_color_index = Math.floor(Math.random() * 2);
        // DONE: TASK 2: change this or any variables above to return only 'red' or 'blue' at random (go Quakers!)
        res.json({ message: `Hello, ${name}!`, jersey_color: colors[lucky_color_index] })
    } else {
        // DONE: TASK 3: inspect for issues and correct
        res.json({ message: `Hello, ${name}, we like your jersey!` })
    }
}

// ********************************************
//               GENERAL ROUTES
// ********************************************


// Route 3 (handler)
async function all_matches(req, res) {

  

    // Convert all queries to lowercase without deleting the original one
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }

    // DONE: TASK 4: implement and test, potentially writing your own (ungraded) tests
    // We have partially implemented this function for you to 
    // parse in the league encoding - this is how you would use the ternary operator to set a variable to a default value
    // we didn't specify this default value for league, and you could change it if you want! 
    // in reality, league will never be undefined since URLs will need to match matches/:league for the request to be routed here... 
    const league = req.params.league ? req.params.league : 'D1'
    // use this league encoding in your query to furnish the correct results

    if (req.query.page && !isNaN(req.query.page)) {
        // This is the case where page is defined.
        // The SQL schema has the attribute OverallRating, but modify it to match spec! 
        // DONE: query and return results here:

        

        const pageSize = req.query.pagesize ? req.query.pagesize : 10
        const page = req.query.page
        
        connection.query(`SELECT MatchId, Date, Time, HomeTeam AS Home, AwayTeam AS Away, FullTimeGoalsH AS HomeGoals, FullTimeGoalsA AS AwayGoals  
        FROM Matches
        WHERE Division = '${league}' 
        ORDER BY HomeTeam, AwayTeam
        LIMIT ${(page - 1) * pageSize}, ${pageSize}`, function (error, results, fields) {

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                res.json({ results: results })
            }
        });

        
   
    } else {
        // we have implemented this for you to see how to return results by querying the database
        connection.query(`SELECT MatchId, Date, Time, HomeTeam AS Home, AwayTeam AS Away, FullTimeGoalsH AS HomeGoals, FullTimeGoalsA AS AwayGoals  
        FROM Matches 
        WHERE Division = '${league}'
        ORDER BY HomeTeam, AwayTeam`, function (error, results, fields) {

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                res.json({ results: results })
            }
        });
    }
}

// Route 4 (handler)
async function all_players(req, res) {
    // DONE: TASK 5: implement and test, potentially writing your own (ungraded) tests
    
    // Convert all queries to lowercase without deleting the original onesQ
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }

    if (req.query.page && !isNaN(req.query.page)) {
        // This is the case where page is defined.
        // The SQL schema has the attribute OverallRating, but modify it to match spec! 
        // DONE: query and return results here:

        const pageSize = req.query.pagesize ? req.query.pagesize : 10
        const page = req.query.page
        
        connection.query(`SELECT PlayerId, Name, Nationality, OverallRating AS Rating, Potential, Club, Value  
        FROM Players
        ORDER BY Name
        LIMIT ${(page - 1) * pageSize}, ${pageSize}`, 
        function (error, results, fields) {
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                res.json({ results: results })
            }
        });
   
    } else {
        
        connection.query(`SELECT PlayerId, Name, Nationality, OverallRating AS Rating, Potential, Club, Value  
        FROM Players
        ORDER BY Name`, 
        function (error, results, fields) {

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                res.json({ results: results })
            }
        });
    }
}


// ********************************************
//             MATCH-SPECIFIC ROUTES
// ********************************************

// Route 5 (handler)
async function match(req, res) {
    
    // Convert all queries to lowercase without deleting the original ones
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }

    id = req.query.id ? req.query.id : null
    
    if (id && !isNaN(id)) {
        connection.query(`SELECT MatchId, Date, Time, HomeTeam AS Home, AwayTeam AS Away, FullTimeGoalsH AS HomeGoals, FullTimeGoalsA AS AwayGoals, HalfTimeGoalsH AS HTHomeGoals, HalfTimeGoalsA AS HTAwayGoals, ShotsH AS ShotsHome, ShotsA AS ShotsAway, ShotsOnTargetH AS ShotsOnTargetHome, ShotsOnTargetA AS ShotsOnTargetAway, FoulsH AS FoulsHome, FoulsA AS FoulsAway, CornersH AS CornersHome, CornersA AS CornersAway, YellowCardsH AS YCHome, YellowCardsA AS YCAway, RedCardsH AS RCHome, RedCardsA AS RCAway
        FROM Matches
        WHERE MatchId = ${id}`, 
        function (error, results, fields) {

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
                
            }
        });
    } else {
        res.json({ results: 'No ID or invalid ID provided.' })
    }
    
}

// ********************************************
//            PLAYER-SPECIFIC ROUTES
// ********************************************

// Route 6 (handler)
async function player(req, res) {

    // Convert all queries to lowercase without deleting the original ones
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }
    
    id = req.query.id ? req.query.id : null
    
    if (id && !isNaN(id)) { 

        connection.query(`
        SELECT *
        FROM Players
        WHERE PlayerId = ${id}`, 
        function (error, results, fields) {

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    if (results[0].BestPosition === 'GK'){
                        delete results[0].NPassing
                        delete results[0].NBallControl
                        delete results[0].NAdjustedAgility
                        delete results[0].NStamina
                        delete results[0].NStrength
                        delete results[0].NPositioning

                    } else {

                        delete results[0].GKPenalties
                        delete results[0].GKDiving
                        delete results[0].GKHandling
                        delete results[0].GKKicking
                        delete results[0].GKPositioning
                        delete results[0].GKReflexes

                    }
                    results[0].Rating = results[0].OverallRating
                    delete results[0].OverallRating

                    res.json({ results: results })
                }
                
            }
        });

    } else {
        res.json({ results: 'No ID or invalid ID provided.' })
    }
}


// ********************************************
//             SEARCH ROUTES
// ********************************************

// Route 7 (handler)
async function search_matches(req, res) {
    // TODO: TASK 8: implement and test, potentially writing your own (ungraded) tests
    // IMPORTANT: in your SQL LIKE matching, use the %query% format to match the search query to substrings, not just the entire string
    
    // Convert all queries to lowercase without deleting the original ones
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }

    home = req.query.home ? req.query.home : ''
    away = req.query.away ? req.query.away : ''
    page = req.query.page && !isNaN(req.query.page) ? req.query.page : 1
    pageSize = req.query.pagesize && !isNaN(req.query.pagesize) ? req.query.pagesize : 10

    
        connection.query(`SELECT MatchId, Date, Time, HomeTeam AS Home, AwayTeam AS Away, FullTimeGoalsH AS HomeGoals, FullTimeGoalsA AS AwayGoals
        FROM Matches
        WHERE HomeTeam LIKE '%${home}%' AND AwayTeam LIKE '%${away}%'
        ORDER BY HomeTeam, AwayTeam
        LIMIT ${(page - 1) * pageSize}, ${pageSize}`, 
        function (error, results, fields) {

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
                
            }
        });
}

// Route 8 (handler)
async function search_players(req, res) {
    // TODO: TASK 9: implement and test, potentially writing your own (ungraded) tests
    // IMPORTANT: in your SQL LIKE matching, use the %query% format to match the search query to substrings, not just the entire string
    
    // Convert all queries to lowercase without deleting the original ones
    for (const [key, value] of Object.entries(req.query)) {
        req.query[key.toLocaleLowerCase()] = value
      }
      
    name_ = req.query.name ? req.query.name : ''
    nationality = req.query.nationality ? req.query.nationality : ''
    club = req.query.club ? req.query.club : ''
    ratingLow = req.query.ratinglow && !isNaN(req.query.ratinglow) ? req.query.ratinglow : 0
    ratingHigh = req.query.ratinghigh && !isNaN(req.query.ratinghigh) ? req.query.ratinghigh : 100
    potentialLow = req.query.potentiallow && !isNaN(req.query.potentiallow) ? req.query.potentiallow : 0
    potentialHigh = req.query.potentialhigh && !isNaN(req.query.potentialhigh) ? req.query.potentialhigh : 100
  
    page = req.query.page && !isNaN(req.query.page) ? req.query.page : 1
    pageSize = req.query.pagesize && !isNaN(req.query.pagesize) ? req.query.pagesize : 10

    connection.query(`SELECT PlayerId, Name, Nationality, OverallRating AS Rating, Potential, Club, Value  
        FROM Players
        WHERE Name LIKE '%${name_}%' AND Nationality LIKE '%${nationality}%' AND Club LIKE '%${club}%' AND OverallRating >= ${ratingLow} AND OverallRating <= ${ratingHigh} AND  Potential >= ${potentialLow} AND Potential <= ${potentialHigh}
        ORDER BY Name
        LIMIT ${(page - 1) * pageSize}, ${pageSize}`, 
        function (error, results, fields) {routes.js

            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
        });
}

////////////////////////////////////////////////////////////////////////////////////////////////

async function constructor_year(req, res) {
    query = `
        select cs.constructorStandingsId, cs.raceId, cs.constructorId, cs.position, cs.positionText, cs.wins,
        races.year, constructors.name, max(points) as points from constructorStandings cs
        left join races on cs.raceId = races.raceId
        left join constructors on cs.constructorId = constructors.constructorId
        group by races.year, constructors.name
        order by races.year, points desc;
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}

async function driver_year(req, res) {
    query = `
        select ds.driverStandingsId, ds.raceId, ds.driverId, max(ds.points) as points,
        ds.position, ds.positionText, ds.wins, races.year, CONCAT(forename,' ',surname) as fullName
        from driverStandings ds left join races
        on ds.raceId = races.raceId
        left join drivers on ds.driverId = drivers.driverId
        group by races.year, fullName
        order by races.year, points desc;
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}

async function performance_driver(req, res) {
    query = `
        select temp1.raceId, temp1.driverId, temp1.constructorId, grid, temp2.position as positionAfterLap
        from (select * from results where raceId >= 1074 and raceId <1085) as temp1
        left join (select * from lapTimes where raceId >= 1074 and raceId <1085 and lap =1) as temp2
        on temp1.raceId = temp2.raceId and temp1.driverId = temp2.driverId;
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}

async function top_ten(req, res) {
    query = `
        select CONCAT(forename,' ',surname) as driverName, count(races.raceId) as total from results join status on results.statusId = status.statusId
        join races on results.raceId = races.raceId
        join drivers on results.driverId = drivers.driverId
        join constructors on constructors.constructorId = results.constructorId
        join circuits on circuits.circuitId = races.circuitId
        group by driverName
        order by total desc
        limit 10;    
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}

async function battle(req, res) {
    query = `
        select * from results
        left join races on results.raceId = races.raceId
        left join (select driverId, CONCAT(forename,' ',surname) as fullName from drivers) as tmp
        on results.driverId = tmp.driverId;    
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}

async function most_points(req, res) {
    query = `
        select year, CONCAT(forename,' ',surname) as driverName, sum(points) as total from results join status on results.statusId = status.statusId
        join races on results.raceId = races.raceId
        join drivers on results.driverId = drivers.driverId
        join constructors on constructors.constructorId = results.constructorId
        join circuits on circuits.circuitId = races.circuitId
        group by year, driverName
        order by total desc
        limit 1;    
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}

async function top_ten_laps(req, res) {
    query = `
        select CONCAT(forename,' ',surname) as driverName, sum(laps) as total from results join status on results.statusId = status.statusId
        join races on results.raceId = races.raceId
        join drivers on results.driverId = drivers.driverId
        join constructors on constructors.constructorId = results.constructorId
        join circuits on circuits.circuitId = races.circuitId
        group by driverName
        order by total desc
        limit 10;    
    `;

    connection.query(query, 
        function (error, results, fields) {routes.js
            if (error) {
                console.log(error)
                res.json({ error: error })
            } else if (results) {
                if (results.length == 0) {
                    res.json({ results: [] })
                } else {
                    res.json({ results: results })
                }
            }
    });
}


////////////////////////////////////////////////////////////////////////////////////////////////

module.exports = {
    hello,
    jersey,
    all_matches,
    all_players,
    match,
    player,
    search_matches,
    search_players,
    top_ten,
    top_ten_laps,
    most_points,
    battle,
    performance_driver,
    driver_year,
    constructor_year
}