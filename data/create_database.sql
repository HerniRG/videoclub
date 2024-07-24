BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "directores" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "peliculas" (
	"id"	INTEGER,
	"titulo"	TEXT NOT NULL,
	"director_id"	INTEGER NOT NULL,
	"sinopsis"	TEXT,
	"id_genero"	INTEGER,
	FOREIGN KEY("director_id") REFERENCES "directores"("id"),
	FOREIGN KEY("id_genero") REFERENCES "generos"("id"),
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "generos" (
	"id"	INTEGER,
	"genero"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "copias" (
	"id"	INTEGER,
	"id_pelicula"	INTEGER NOT NULL,
	FOREIGN KEY("id_pelicula") REFERENCES "peliculas"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Insertar datos iniciales en la tabla directores
INSERT INTO "directores" ("id","nombre") VALUES (1,'Aditya Chopra');
INSERT INTO "directores" ("id","nombre") VALUES (2,'Akira Kurosawa');
INSERT INTO "directores" ("id","nombre") VALUES (3,'Alfred Hitchcock');
INSERT INTO "directores" ("id","nombre") VALUES (4,'Bang Woo-ri');
INSERT INTO "directores" ("id","nombre") VALUES (5,'Billy Wilder');
INSERT INTO "directores" ("id","nombre") VALUES (6,'Bob Persichetti');
INSERT INTO "directores" ("id","nombre") VALUES (7,'Bong Joon-ho');
INSERT INTO "directores" ("id","nombre") VALUES (8,'Charlie Chaplin');
INSERT INTO "directores" ("id","nombre") VALUES (9,'Charlie Mackesy');
INSERT INTO "directores" ("id","nombre") VALUES (10,'Christina Sotta');
INSERT INTO "directores" ("id","nombre") VALUES (11,'Christopher Nolan');
INSERT INTO "directores" ("id","nombre") VALUES (12,'Damien Chazelle');
INSERT INTO "directores" ("id","nombre") VALUES (13,'David Fincher');
INSERT INTO "directores" ("id","nombre") VALUES (14,'Elem Klimov');
INSERT INTO "directores" ("id","nombre") VALUES (15,'Ernesto Contreras');
INSERT INTO "directores" ("id","nombre") VALUES (16,'Ernst Lubitsch');
INSERT INTO "directores" ("id","nombre") VALUES (17,'Ettore Scola');
INSERT INTO "directores" ("id","nombre") VALUES (18,'Fernando Meirelles');
INSERT INTO "directores" ("id","nombre") VALUES (19,'Francis Ford Coppola');
INSERT INTO "directores" ("id","nombre") VALUES (20,'Frank Capra');
INSERT INTO "directores" ("id","nombre") VALUES (21,'Frank Darabont');
INSERT INTO "directores" ("id","nombre") VALUES (22,'Giuseppe Tornatore');
INSERT INTO "directores" ("id","nombre") VALUES (23,'Guel Arraes');
INSERT INTO "directores" ("id","nombre") VALUES (24,'Haruo Sotozaki');
INSERT INTO "directores" ("id","nombre") VALUES (25,'Hayao Miyazaki');
INSERT INTO "directores" ("id","nombre") VALUES (26,'Hikaru Yamaguchi');
INSERT INTO "directores" ("id","nombre") VALUES (27,'Hiroshi Teshigahara');
INSERT INTO "directores" ("id","nombre") VALUES (28,'Irvin Kershner');
INSERT INTO "directores" ("id","nombre") VALUES (29,'Isao Takahata');
INSERT INTO "directores" ("id","nombre") VALUES (30,'Jacques Becker');
INSERT INTO "directores" ("id","nombre") VALUES (31,'Joe Russo');
INSERT INTO "directores" ("id","nombre") VALUES (32,'Joel Crawford');
INSERT INTO "directores" ("id","nombre") VALUES (33,'Jonathan Demme');
INSERT INTO "directores" ("id","nombre") VALUES (34,'Jorge Ulloa');
INSERT INTO "directores" ("id","nombre") VALUES (35,'Justin Baldoni');
INSERT INTO "directores" ("id","nombre") VALUES (36,'Katsuichi Nakayama');
INSERT INTO "directores" ("id","nombre") VALUES (37,'Kazuya Tsurumaki');
INSERT INTO "directores" ("id","nombre") VALUES (38,'Kemp Powers');
INSERT INTO "directores" ("id","nombre") VALUES (39,'Kotaro Tamura');
INSERT INTO "directores" ("id","nombre") VALUES (40,'Kou Matsuo');
INSERT INTO "directores" ("id","nombre") VALUES (41,'Lee Joon-ik');
INSERT INTO "directores" ("id","nombre") VALUES (42,'Luc Besson');
INSERT INTO "directores" ("id","nombre") VALUES (43,'Makoto Shinkai');
INSERT INTO "directores" ("id","nombre") VALUES (44,'Martin Scorsese');
INSERT INTO "directores" ("id","nombre") VALUES (45,'Masaki Kobayashi');
INSERT INTO "directores" ("id","nombre") VALUES (46,'Masato Jimbo');
INSERT INTO "directores" ("id","nombre") VALUES (47,'Mehmet Ada Öztekin');
INSERT INTO "directores" ("id","nombre") VALUES (48,'Miloš Forman');
INSERT INTO "directores" ("id","nombre") VALUES (49,'Mitja Okorn');
INSERT INTO "directores" ("id","nombre") VALUES (50,'MTJJ');
INSERT INTO "directores" ("id","nombre") VALUES (51,'Naoko Yamada');
INSERT INTO "directores" ("id","nombre") VALUES (52,'Olivier Nakache');
INSERT INTO "directores" ("id","nombre") VALUES (53,'Paola Cortellesi');
INSERT INTO "directores" ("id","nombre") VALUES (54,'Park Chan-wook');
INSERT INTO "directores" ("id","nombre") VALUES (55,'Paul Dugdale');
INSERT INTO "directores" ("id","nombre") VALUES (56,'Peter Farrelly');
INSERT INTO "directores" ("id","nombre") VALUES (57,'Peter Jackson');
INSERT INTO "directores" ("id","nombre") VALUES (58,'Peter Weir');
INSERT INTO "directores" ("id","nombre") VALUES (59,'Quentin Tarantino');
INSERT INTO "directores" ("id","nombre") VALUES (60,'Rob Minkoff');
INSERT INTO "directores" ("id","nombre") VALUES (61,'Robert Zemeckis');
INSERT INTO "directores" ("id","nombre") VALUES (62,'Roberto Benigni');
INSERT INTO "directores" ("id","nombre") VALUES (63,'Roman Polanski');
INSERT INTO "directores" ("id","nombre") VALUES (64,'Sergio Leone');
INSERT INTO "directores" ("id","nombre") VALUES (65,'Sergio Pablos');
INSERT INTO "directores" ("id","nombre") VALUES (66,'Shinichiro Ushijima');
INSERT INTO "directores" ("id","nombre") VALUES (67,'Shouko Nakamura');
INSERT INTO "directores" ("id","nombre") VALUES (68,'Sidney Lumet');
INSERT INTO "directores" ("id","nombre") VALUES (69,'Souichi Masui');
INSERT INTO "directores" ("id","nombre") VALUES (70,'Stanley Kubrick');
INSERT INTO "directores" ("id","nombre") VALUES (71,'Steven Spielberg');
INSERT INTO "directores" ("id","nombre") VALUES (72,'Taichi Ishidate');
INSERT INTO "directores" ("id","nombre") VALUES (73,'Takahiro Omori');
INSERT INTO "directores" ("id","nombre") VALUES (74,'Tony Kaye');
INSERT INTO "directores" ("id","nombre") VALUES (75,'Tosca Musk');
INSERT INTO "directores" ("id","nombre") VALUES (76,'Xavier Dolan');

-- Insertar datos iniciales en la tabla generos
INSERT INTO "generos" ("id","genero") VALUES (1,'Accion');
INSERT INTO "generos" ("id","genero") VALUES (2,'Aventura');
INSERT INTO "generos" ("id","genero") VALUES (3,'Comedia');
INSERT INTO "generos" ("id","genero") VALUES (4,'Drama');
INSERT INTO "generos" ("id","genero") VALUES (5,'Fantasia');
INSERT INTO "generos" ("id","genero") VALUES (6,'Terror');
INSERT INTO "generos" ("id","genero") VALUES (7,'Misterio');
INSERT INTO "generos" ("id","genero") VALUES (8,'Romance');
INSERT INTO "generos" ("id","genero") VALUES (9,'Ciencia Ficcion');
INSERT INTO "generos" ("id","genero") VALUES (10,'Suspense');
INSERT INTO "generos" ("id","genero") VALUES (11,'Western');
INSERT INTO "generos" ("id","genero") VALUES (12,'Animacion');
INSERT INTO "generos" ("id","genero") VALUES (13,'Documental');
INSERT INTO "generos" ("id","genero") VALUES (14,'Musical');

-- Insertar datos iniciales en la tabla peliculas
INSERT INTO "peliculas" ("id", "titulo", "director_id", "sinopsis", "id_genero") VALUES (1, 'El señor de los anillos', 57, 'Sauron es muy malo', 9);
INSERT INTO "peliculas" ("id", "titulo", "director_id", "sinopsis", "id_genero") VALUES (2, 'Los siete samuráis', 2, 'Una banda de forajidos atemorizan a los habitantes de un pequeño pueblo, saqueándolos periódicamente sin piedad. Para repeler estos ataques, los aldeanos deciden contratar a mercenarios. Finalmente, consiguen los servicios de 7 guerreros, 7 samurais dispuestos a defenderlos a cambio, tan solo, de cobijo y comida.', 1);
INSERT INTO "peliculas" ("id", "titulo", "director_id", "sinopsis", "id_genero") VALUES (3, 'El infierno del odio', 2, 'Gondo, un hombre de negocios, recibe la noticia de que su hijo ha sido secuestrado, y el rescate exigido es una cantidad de dinero similar a la que necesita para cerrar una importante negociación. Gondo está dispuesto a pagar el rescate hasta que comprende que los secuestradores se han equivocado y se han llevado al hijo del chófer. Ahora deberá decidir si el dinero es más importante que la vida del niño.', 10);
INSERT INTO "peliculas" ("id", "titulo", "director_id", "sinopsis", "id_genero") VALUES (4, 'Un amor contra viento y marea', 1, 'Una historia de amor épica en tiempos difíciles.', 8);
INSERT INTO "peliculas" ("id", "titulo", "director_id", "sinopsis", "id_genero") VALUES (5, 'El viaje de Chihiro', 25, 'Una niña atraviesa un mundo mágico en busca de sus padres.', 5);

-- Insertar datos iniciales en la tabla copias
INSERT INTO "copias" ("id", "id_pelicula") VALUES (1, 1);
INSERT INTO "copias" ("id", "id_pelicula") VALUES (2, 2);
INSERT INTO "copias" ("id", "id_pelicula") VALUES (3, 3);
INSERT INTO "copias" ("id", "id_pelicula") VALUES (4, 4);
INSERT INTO "copias" ("id", "id_pelicula") VALUES (5, 5);

COMMIT;
