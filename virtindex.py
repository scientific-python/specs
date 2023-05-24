# using requests get the html from https://pypi.anaconda.org/scipy-wheels-nightly/simple/matplotlib/


import requests
from bs4 import BeautifulSoup

indexes = [
    (
        "https://pypi.anaconda.org/scientific-python-nightly-wheels/",
        "https://pypi.anaconda.org/",
    ),
    ("https://pypi.org/", "https://pypi.org/"),
]


def get_index(index, package):
    url, root = index
    root = root.strip("/")

    if not url.endswith("/"):
        url = url + "/"
    url = url + "simple/" + package + "/"

    print("get_index", url)
    html = requests.get(url).text

    # get the content of html/body after parsing the html

    soup = BeautifulSoup(html, "html.parser")

    body = soup.find("body")
    # get all the `a` from body

    links = body.find_all("a")
    print("found, ", len(links), " links")

    # for all the links, update all theh hrefs, and if they start with / prepend `https://pypi.anaconda.org`

    for link in links:
        href = link.get("href")
        if href.startswith("/"):
            link["href"] = root + href
    return soup, links


# make a flask app

from flask import Flask

app = Flask(__name__)


@app.route("/simple/<project>")
def simple(project):
    ixes = [get_index(index, project) for index in indexes]
    res = """
    <html>
        <head>
        <body>
    """
    for ix, lks in ixes:
        for lk in lks:
            res += f'\n<href="{lk.get("href")}">{lk.get("href").split("/")[-1]}</href>'

    res += """
        </body>
        </head>
    </html>
    """
    return res


app.run()
