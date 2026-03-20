import requests
from bs4 import BeautifulSoup

def fetch_unicode_grid_html(doc_url: str):
    """
    Fetch the published Google Doc HTML and extract (x, char, y) rows
    from the first table on the page.
    """
    resp = requests.get(doc_url)
    resp.raise_for_status()
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")

    # Find the first table on the page
    table = soup.find("table")
    if table is None:
        raise ValueError("No table found in document")

    rows = []

    # Skip header row, parse data rows
    for tr in table.find_all("tr")[1:]:
        tds = tr.find_all("td")
        if len(tds) < 3:
            continue

        x_text = tds[0].get_text(strip=True)
        char_text = tds[1].get_text(strip=True)
        y_text = tds[2].get_text(strip=True)

        if x_text.isdigit() and y_text.isdigit():
            rows.append((int(x_text), char_text, int(y_text)))

    return rows


def build_grid(rows):
    if not rows:
        return []

    max_x = max(r[0] for r in rows)
    max_y = max(r[2] for r in rows)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, char, y in rows:
        grid[y][x] = char

    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))


def render_google_doc_grid(doc_url: str):
    rows = fetch_unicode_grid_html(doc_url)
    grid = build_grid(rows)
    print_grid(grid)
# calling the function to print results
render_google_doc_grid(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)
