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


USE awj8sf_db;
CREATE TABLE teams (
    team_name VARCHAR(50) PRIMARY KEY,
    team_abr VARCHAR(50),
    division VARCHAR(50),
    wins INT
);

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Buffalo Bills", "BUF", "AFC East", 12)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("New England Patriots", "NE", "AFC East", 14)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Seattle Seahawks", "SEA", "NFC West", 14)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Detriot Lions", "DET", "NFC North", 9)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Dallas Cowboys", "DAL", "AFC East", 7)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Jacksonville Jaguars", "JAX", "AFC South", 13)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Denver Broncos", "DEN", "AFC West", 14)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Los Angeles Chargers", "LAC", "AFC West", 11)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Los Angeles Rams", "LAR", "NFC West", 12)

INSERT INTO teams (team_name, team_abr, division, wins)
VALUES("Chicago Bears", "CHI", "NFC North", 11)