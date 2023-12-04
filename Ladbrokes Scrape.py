from bs4 import BeautifulSoup

# Load your HTML file
with open('NBA.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with the class 'sports-event-subtitle__name-text'
games = soup.find_all('div', class_='sports-event-title')

for game in games:
    game_title = game.text.strip()
    print(f"Game: {game_title}")

    # Assuming the next sibling contains the teams and odds
    next_sibling = game.find_next_sibling()
    if next_sibling:
        teams_odds = next_sibling.text.strip()
        print(f"Details: {teams_odds}")