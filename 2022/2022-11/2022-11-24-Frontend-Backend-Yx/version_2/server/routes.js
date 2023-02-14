const config = require('./config.json')
const mysql = require('mysql');
const e = require('express');
const { connect } = require('./server');

// TODO: fill in your connection details here
const connection = mysql.createConnection({
    host: config.rds_host,
    user: config.rds_user,
    password: config.rds_password,
    port: config.rds_port,
    database: config.rds_db
});
connection.connect();


// Route 1 (Player Info)
async function player(req, res) {
    connection.query(`SELECT * from Players where PLAYER_ID = ${req.query.id}`, function (error, results) {
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

// Route 2 (Top Team Win/Lose Against)
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

module.exports = {
    player,
    playerCompare,
    teamWinLoseMost
}