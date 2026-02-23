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

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Sam Darnold", "Seattle Seahawks", 25, 14);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Jared Goff", "Detroit Lions", 34, 8);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Dak Prescott", "Dallas Cowboys", 30, 10);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Trevor Lawrence", "Jacksonville Jaguars", 29, 12);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Bo Nix", "Denver Broncos", 25, 11);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Justin Herbert", "Los Angeles Chargers", 26, 13);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Matthew Stafford", "Los Angeles Rams", 46, 8);

INSERT INTO players (player_name, team, touchdowns, interceptions)
VALUES("Caleb Williams", "Chicago Bears", 27, 7);