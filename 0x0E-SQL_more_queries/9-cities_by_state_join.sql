-- script: list all cities in the database hbtn_0d_usa and the state they belong to
-- records are sorted in order of ascending cities.id.
SELECT
    c.id,
    c.name,
    s.name
FROM
    cities AS c
    INNER JOIN states AS s ON c.state_id = s.id
ORDER BY
    c.id;