USE awj8sf_db;
SELECT * FROM players1 
LEFT JOIN teams1 
ON players1.team = teams1.team_name
WHERE wins > 11;