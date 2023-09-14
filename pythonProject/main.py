import os
from typing import Optional
import typer

app = typer.Typer()


@app.command()
def examine_csv(file: str, line_number: int, col_number: int):
    with open(file, 'r') as file1:
        c
        col_count: int = 0


        for row in file1.readlines():
            row_count += 1
            if row_count == line_number:
                cols: [str] = row.split(',')
                print(cols[1])
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app()





