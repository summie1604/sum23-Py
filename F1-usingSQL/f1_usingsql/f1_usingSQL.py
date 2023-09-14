import typer
import csv
import sqlite3
from datetime import datetime, timedelta
from typing import Optional

app = typer.Typer()


@app.command()
def load(db_file: str = "f1.db"):
    load_teams(db_file)
    load_drivers(db_file)
    load_positions(db_file)
    load_races(db_file)


def load_drivers(db_file: str = "f1.db", csv_file: str = "drivers.csv"):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            car_number: int = int(row['driverId'])
            name: str = row['driverRef']
            query: str = f"""insert into drivers (car_number, name) 
                    values ({car_number}, "{name}") on conflict (car_number) do nothing;"""
            print(query)
            cur.execute(query)
        con.commit()
    pass


def load_teams(db_file: str = "f1.db", csv_file: str = "constructors.csv"):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            team_id: int = int(row['constructorId'])
            team_name: str = row['name']
            query: str = f"""insert into teams (team_id, team_name) 
                values ({team_id}, "{team_name}") on conflict (team_id) do nothing;"""
            print(query)
            cur.execute(query)
        con.commit()


def load_races(db_file: str = "f1.db", csv_file: str = "races.csv"):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raceid: str = row['raceid']
            venue: str = row['circuitId']
            year: int = int(row['year'])
            query: str = f"""insert into races (race_id, venue, year) 
                values ({raceid}, "{venue}", {year}) on conflict (race_id) do nothing;"""
            print(query)
            cur.execute(query)
        con.commit()


def time2ms(time: str) -> Optional[int]:
    if not time:
        return None
    fastest_lap: datetime = datetime.strptime(time, "%M:%S.%f")
    milliseconds: int = int(60000 * fastest_lap.minute + 1000*fastest_lap.second + fastest_lap.microsecond/1000)
    return milliseconds


def intOrNone(value: str) -> Optional[int]:
    return int(value) if value else None


def load_positions(db_file: str = "f1.db", csv_file: str = "results.csv"):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            raceid: str = row['raceId']
            position: Optional[int] = intOrNone(row.get('position', None))
            car_number: int = int(row['driverId'])
            total_time: Optional[int] = intOrNone(row.get('milliseconds', None))
            points_scored: float = float(row['points'])
            fastest_lap: int = time2ms(row.get('fastestLapTime', None))
            team_id: int = int(row['constructorId'])
            query: str = f"""insert into positions (race_id, position, car_number, total_time, points_scored, fastest_lap) 
                values ({raceid}, {position if position else "NULL"}, {car_number}, 
                    {total_time if total_time else "NULL"}, {points_scored}, {fastest_lap if fastest_lap else "NULL"}) 
                on conflict (race_id, position, car_number) do nothing;"""
            print(query)
            cur.execute(query)
        con.commit()


if __name__ == "__main__":
    app()
