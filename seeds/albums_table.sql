
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);


INSERT INTO albums (title, release_year, artist_id) VALUES ('Imagine', 1978, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Thriller', 1982, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Dark Side of the Moon', 1973, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Abbey Road', 1969, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Sgt. Pepper''s Lonely Hearts Club Band', 1967, 5);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Hotel California', 1976, 6);
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Wall', 1979, 7);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Back in Black', 1980, 8);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Led Zeppelin IV', 1971, 9);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Rumours', 1977, 10);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Cotton Eyed Joe', 1994, 11);