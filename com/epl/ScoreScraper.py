from bs4 import BeautifulSoup
from selenium import common
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from datetime import datetime
from datetime import date
import time
import globals
import re
from com.epl.Team import Team
from com.epl.Match import Match


def parse_scores(response):
    """

    :param response:
    :return:
    """
    print('-' * 150)
    print('-' * 150)
    soup = BeautifulSoup(response, "html.parser")
    fixtures = soup.find('section', attrs={'class': 'fixtures'})
    all_fixtures = fixtures.find_all('div', attrs={'class': 'fixtures__matches-list'})
    for af in all_fixtures:
        m = Match()
        m.date = datetime.strptime(af["data-competition-matches-list"], '%A %d %B %Y').date()
        fixtures_match_list = af.find_all('ul', attrs={'class': 'matchList'})
        for ml in fixtures_match_list:
            matches = ml.find_all('span', attrs={'class': 'teams'})
            venues = ml.find_all('li', attrs={'class': 'matchFixtureContainer'})
            venue_list = []
            for v in venues:
                venue_list.append(re.sub(re.compile('<.*?>'), '', v["data-venue"]))
            for i, match in enumerate(matches):
                opponents = match.find_all('span', attrs={'class': 'shortname'})
                score = match.find('span', attrs={'class': 'score'})
                venue = venue_list[i]  # Venue list will always match the matches
                for c, team in enumerate(opponents):
                    if c == 0:
                        home_team = Team(team.text, score.text[0:1], venue)
                        determine_result(score, home_team, True)
                        m.home = home_team
                    elif c == 1:
                        away_team = Team(team.text, score.text[2:])
                        determine_result(score, away_team, False)
                        m.away = away_team
                print(m)
        print('-' * 150)


def determine_result(score, team, is_home):
    if is_home:
        if int(score.text[0:1]) > int(score.text[2:]):
            team.result = 'W'
        elif int(score.text[0:1]) < int(score.text[2:]):
            team.result = 'L'
        else:
            team.result = 'D'
    else:
        if int(score.text[0:1]) > int(score.text[2:]):
            team.result = 'L'
        elif int(score.text[0:1]) < int(score.text[2:]):
            team.result = 'W'
        else:
            team.result = 'D'


class ScoreScraper:

    def __init__(self, total_years=None):
        if total_years is None:
            date_start = datetime(1992, 1, 1)
            td = datetime.now() - date_start
            self.total_years = int(td.days / 365.25)
        else:
            self.total_years = total_years
        self.driver = webdriver.Safari()

    def start(self):
        print(f'Total Years {self.total_years}')
        all_responses = {}
        for y in range(1, (self.total_years+1)):
            response = self.fetch_content(self.driver, y)
            all_responses[str(y)] = response
        for key, response in all_responses.items():
            parse_scores(response)

    def fetch_content(self, driver, page=None):
        """
        This method initializes the Safari Driver and programmatically gets all html content in case
        of infinite scrolling pages
        :param driver: webdriver.Safari() object
        :param page: str year
        :return: str page_source
        """
        if page is None:
            page = 1
        url = globals.url.format(page)
        self.driver.get(url)
        print(f'url - {url}')
        time.sleep(2)  # 2 second for the initial page to load
        scroll_pause_time = 1  # 1 second pause time between content loads
        screen_height = driver.execute_script("return window.screen.height;")
        try:
            driver.find_element(By.XPATH, '//button[text()="Accept All Cookies"]').click()
        except common.exceptions.ElementNotInteractableException:
            pass  # The element will only be found on first attempt
        i = 1
        while True:
            driver.execute_script(f'window.scrollTo(0 , {screen_height * i});')
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            if (screen_height * i) > scroll_height:
                break
        return self.driver.page_source


