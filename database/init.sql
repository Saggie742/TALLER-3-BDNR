CREATE DATABASE IF NOT EXISTS taller3_analitica;

USE taller3_analitica;

DROP TABLE IF EXISTS compras;

CREATE TABLE compras (
	fecha DATE NOT NULL,
	ciudad VARCHAR(50) NOT NULL,
	categoria VARCHAR(50) NOT NULL,
	metodopago VARCHAR (50) NOT NULL,
	usuarioid BIGINT NOT NULL,
	edad INT NOT NULL,
	producto VARCHAR(100) NOT NULL,
	precio BIGINT NOT NULL,
	hora VARCHAR (20) NOT NULL,
)
DUPLICATE KEY (fecha, ciudad, categoria, metodopago)
DISTRIBUTED BY HASH(ciudad) BUCKETS 10
PROPERTIES (
	"replication_num" ="1"
);
