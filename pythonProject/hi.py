import typer

app = typer.Typer()


@app.command()
def csv(file: str, line_number: int):
    with open(file, 'r') as f:
        row_number: int = 0
        for row in f.readlines():
            row_number += 1
            if row_number == line_number:
                col: [str] = row.split(',')
                print(col[-1])

                break


if __name__ == '__main__':
    app()
