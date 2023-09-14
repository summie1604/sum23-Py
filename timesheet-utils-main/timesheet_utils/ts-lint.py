import typer
import re
import csv
from typing import List, Optional
import logging

log = logging.getLogger("Timesheet-Lint")
app = typer.Typer()


@app.command()
def clean(infile: str, outfile: str):
    """
    Fixes the problem of timesheet app reports not properly escaping commas and quotes in generated CSV
    :param infile: Path to CSV generated by timesheet app
    :param outfile: Path for cleaned CSV file
    :return: None
    """
    with open(infile, 'r') as f, open(outfile, 'w', newline='') as g:
        writer = csv.writer(g)
        record: str = ""
        record_count: int = 0
        line_number: int = 0
        column_count: int = 0
        while True:
            line: str = f.readline()
            if len(line) == 0:
                break
            line_number += 1
            record += line
            if line_number == 1:
                columns: List[str] = record.rstrip().split(',')
                column_count = len(columns)
                log.info(f"Found {column_count} columns")
            log.debug(f"Checking if record number {record_count + 1} is complete on line {line_number}")
            pattern: str = '(,[^,]*){' + str(column_count-2) + '}$'
            match: re.Match = re.search(pattern, record)
            if match:
                tail: str = match.group(0).rstrip()[1:]
                head: str = record[0:match.start()]
                project, task = head.split(',', 1)
                row: List[str] = [project, task]
                row.extend(tail.split(','))
                writer.writerow(row)
                record_count += 1
                record = ""
    log.info(f"Found {record_count} records")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(lsevelname)s: %(message)s')
    log.info(f"testing")
    app()