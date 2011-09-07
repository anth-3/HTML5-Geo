CREATE DATABASE geolocations;

USE geolocations;

CREATE TABLE positions (
  pos_id           INT            NOT NULL AUTO_INCREMENT PRIMARY KEY,
  the_geom         POINT          NOT NULL,
  altitude         DECIMAL(8, 2)  NOT NULL,
  accuracy         DECIMAL(4, 0)  NOT NULL,
  altitudeAccuracy DECIMAL(4, 0)  NULL,
  heading          DECIMAL(9, 6)  NULL,
  speed            DECIMAL(7, 4)  NULL,
  timestamp        DATETIME       NOT NULL,
  name             VARCHAR(20)    NOT NULL,
  description      VARCHAR(80)    NULL
);