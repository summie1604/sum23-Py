import typer
import requests
from bs4 import BeautifulSoup
app = typer.Typer()


@app.command()
def geturl(url: str):
    r = requests.get("https://google.com")
    assert r.status_code == 200, f"unexpected status code: {r.status_code}"
    for k, v in r.headers.items():
        print(f"{k}: {v}")
    print()

    # parse HTML
    if 'text/html' in r.headers.get("Content-type"):
        parsed_html = BeautifulSoup(r.text, 'html.parser')
        print(parsed_html.prettify())
    return


if __name__ == "__main__":
    app()



