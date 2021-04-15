# open correct database
# mysql
# use krs028




# clear and reset database
SET FOREIGN_KEY_CHECKS = 0;
drop tables PLAYER;
drop tables TEAM;
drop tables GAME;
drop tables RESULT;

SET FOREIGN_KEY_CHECKS = 1;

show tables;





# create tables

create table TEAM(
   ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   NAME VARCHAR(50) NOT NULL,
   MASCOT VARCHAR(50) NOT NULL,
   TOURNAMENT_SEED INT NOT NULL
);

create table PLAYER(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    POSITION VARCHAR(50) NOT NULL,

   TEAM_ID INT NOT NULL,
   FOREIGN KEY (TEAM_ID)
        REFERENCES TEAM(ID)
        ON DELETE RESTRICT
);

create table GAME(
   ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   COURT_NUM INT NOT NULL,

   HOME_TEAM_ID INT NOT NULL,
   FOREIGN KEY (HOME_TEAM_ID)
        REFERENCES TEAM(ID)
        ON DELETE RESTRICT,

   AWAY_TEAM_ID INT NOT NULL,
   FOREIGN KEY (AWAY_TEAM_ID)
        REFERENCES TEAM(ID)
        ON DELETE RESTRICT,

    DATE DATE NOT NULL

);

create table RESULT(
    GAME_ID INT NOT NULL,
    FOREIGN KEY (GAME_ID)
        REFERENCES GAME(ID)
        ON DELETE RESTRICT,

    PRIMARY KEY (GAME_ID),

    HOME_TEAM_SCORE INT NOT NULL,
    AWAY_TEAM_SCORE INT NOT NULL
);








# insert data

INSERT INTO TEAM
VALUES 
(1,'ARKANSAS','RAZORBACKS',1),
(2,'KENTUCKY','WILDCATS',2),
(3,'HARLEM','GLOBETROTTERS',3),
(4,'LSU','TIGERS',4);



INSERT INTO PLAYER
VALUES 
(1,'JD Notae','F',1),
(2,'Desi Sills','G',1),
(3,'Moses Moody','G',1),
(4,'Jalen Tate','G',1),
(5,'Justin Smith','F',1),
(6,'Jacob Toppin','F',2),
(7,'Devin Askew','G',2),
(8,'Brandon Boston Jr.','G',2),
(9,'Terrence Clarke','G',2),
(10,'Big Easy Lofton','F',3),
(11,'Hammer Harrison','F',3),
(12,'Hi-Lite Bruton','F',3),
(13,'Moose Weekes','G',3),
(14,'Mwani Wilkinson','F',4),
(15,'Javonte Smart','G',4),
(16,'Trendon Watford','F',4);


INSERT INTO GAME
VALUES 
(1,1,1,2,STR_TO_DATE('4/25/21','%m/%d/%Y')),
(2,2,3,4,STR_TO_DATE('4/25/21','%m/%d/%Y')),
(3,3,2,4,STR_TO_DATE('4/27/21','%m/%d/%Y')),
(4,1,1,3,STR_TO_DATE('4/27/21','%m/%d/%Y')),
(5,3,1,4,STR_TO_DATE('4/29/21','%m/%d/%Y')),
(6,2,2,3,STR_TO_DATE('4/29/21','%m/%d/%Y'));



INSERT INTO RESULT
VALUES 
(1,86,72),
(2,94,79),
(3,77,82);
