BEGIN TRANSACTION;
CREATE TABLE ice_cream_flavors (
        id INTEGER PRIMARY KEY,
        flavor TEXT,
        rating INTEGER
    );
INSERT INTO "ice_cream_flavors" VALUES(1,'choco',10);
INSERT INTO "ice_cream_flavors" VALUES(2,'straw',9);
INSERT INTO "ice_cream_flavors" VALUES(3,'pistachio',7.2);
INSERT INTO "ice_cream_flavors" VALUES(4,'hazelnut',6.3);
INSERT INTO "ice_cream_flavors" VALUES(5,'cherries',4.3);
INSERT INTO "ice_cream_flavors" VALUES(6,'banana',2.1);
INSERT INTO "ice_cream_flavors" VALUES(7,'fudge',6.7);
INSERT INTO "ice_cream_flavors" VALUES(8,'vanilla',4.5);
INSERT INTO "ice_cream_flavors" VALUES(9,'strawberry',9);
INSERT INTO "ice_cream_flavors" VALUES(10,'mint',3);
INSERT INTO "ice_cream_flavors" VALUES(11,'coffee',6);
INSERT INTO "ice_cream_flavors" VALUES(12,'caramel',8);
INSERT INTO "ice_cream_flavors" VALUES(13,'saltedcaramel',9.2);
INSERT INTO "ice_cream_flavors" VALUES(14,'mediterranean',6.7);
CREATE TABLE toppings (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
INSERT INTO "toppings" VALUES(1,'sprinkles');
INSERT INTO "toppings" VALUES(2,'choco sauce');
INSERT INTO "toppings" VALUES(3,'caramel sauce');
INSERT INTO "toppings" VALUES(4,'nuts');
COMMIT;
