CREATE DATABASE awj8sf_db;

USE awj8sf_db;
CREATE TABLE players (
    player_name VARCHAR(50) PRIMARY KEY,
    team VARCHAR(50),
    touchdowns INT,
    interceptions INT
);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Josh Allen", "Buffalo Bills", 25, 10);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Drake Maye", "New England Patriots", 31, 8);