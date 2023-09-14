CREATE TABLE "teams" (
  "team_id" integer PRIMARY KEY,
  "team_name" varchar(128)
);

CREATE TABLE "drivers" (
  "car_number" integer PRIMARY KEY,
  "name" varchar(128)

CREATE TABLE "races" (
  "race_id" integer PRIMARY KEY,
  "venue" varchar(128),
  "year" integer
);

CREATE TABLE "positions" (
  "race_id" integer,
  "position" integer,
  "car_number" integer,
  "total_time" integer,
  "fastest_lap" integer,
  "points_scored" float,
  "team_id" integer,

  PRIMARY KEY ("race_id", "position", "car_number"),
  FOREIGN KEY ("race_id") REFERENCES "races" ("race_id"),
  FOREIGN KEY ("car_number") REFERENCES "drivers" ("car_number")
);

