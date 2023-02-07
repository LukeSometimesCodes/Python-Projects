--assignment 7

	CREATE DATABASE movies;
USE movies;

CREATE TABLE Directors (
DirectorID int,
FirstName varchar(50),
LastName varchar(50),
Hometown varchar(50)
);

CREATE TABLE Actors (
ActorID int,
FirstName varchar(50),
LastName varchar(50),
Movie varchar(50),
DirectorID INT NOT NULL CONSTRAINT fk_DirectorID FOREIGN KEY REFERENCES Directors(DirectorID) ON UPDATE CASCADE ON DELETE CASCADE,
);



SELECT * FROM Actors;

SELECT * FROM Directors;

INSERT INTO Actors
(PersonID, FirstName, LastName, Movie)
VALUES
(1, 'Robert', 'Downey', 'Transformers'),
(2, 'Matt', 'Damon', 'Interstellar'),
(3, 'Brad', 'Pitt', 'Se7en'),
(4, 'Brendan', 'Fraser', 'Jurassic Park'),
(5, 'Chris', 'Evans', 'Avengers')
;

INSERT INTO Directors
(PersonID, FirstName, LastName, Directed)
VALUES
(1, 'Michael', 'Bay', 'Transformers'),
(2, 'Steven', 'Spielberg', 'Jurassic Park'),
(3, 'Christopher', 'Nolan', 'Interstellar'),
(4, 'Tim', 'Burton', 'idk'),
(5, 'Zack', 'Snyder', 'Justice League')
;


DROP TABLE Actors;
DROP TABLE Directors;

SELECT Movie
FROM Actors
INNER JOIN Directors
ON Actors.Movie = Directors.Directed;
