# Create by Etzion Harari
# https://github.com/EtzionR

# Load libraries:
from matplotlib.colors import LinearSegmentedColormap as colormap
from bs4 import BeautifulSoup as bs
from datetime import date as dt
import matplotlib.pyplot as plt
from time import sleep
import pandas as pd
import requests

# Define useful variables
LINK = 'href'
OLD = 'Older'
CMP = colormap.from_list('', ['w', 'darkgreen', 'green', 'gold', 'orangered', 'red'])
WDAYS= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Define useful functions
wday = lambda day: WDAYS[day.weekday()]
page = lambda user: f'https://github.com/{user}?tab=repositories'
main = lambda name: f'https://github.com{name}/commits/main'
master = lambda name: f'https://github.com{name}/commits/master'
crawl = lambda url: bs(requests.get(url).text, 'html.parser')
status = lambda url: print(f'Scarping {url} repository')
scroll_down = lambda button: True if button and OLD == button.text else False
date = lambda text, url: {'repo': url, 'year': text[:4], 'month': text[5:7], 'day': text[8:10],
                          'hour': text[11:13], 'minutes': text[14:16], 'seconds': text[17:19]}

# Define Gitime Object
class GiTime:
    """
    GitTime object

    crawling github commits of choosen user
    """
    def __init__(self, user, save=True, slp=1):
        """
        initialize GiTime object
        :param user: choosen user github name
        :param save: saving the commits to csv file (bool ,defualt: True)
        :param slp: sleep time between crawling sessions
        """
        self.slp = slp
        self.save = save
        self.user = user
        self.page = page(user)
        self.repos = self.get_repos()
        self.dates = self.dates_crawler()
        self.table = self.create_table()
        self.clndr = self.calendar()

    def dates_crawler(self):
        """
        main crawling function
        gets the commits dates from every user repos
        :return: user dates logs
        """
        dates = []
        for url in self.repos:
            repo_page = crawl(master(url))
            repo_page = self.invalid_branch(repo_page, url)

            status(url)
            dates += self.get_dates(repo_page, url)
            button = self.get_button(repo_page)
            while scroll_down(button):
                sleep(self.slp)
                repo_page = crawl(button.attrs[LINK])
                dates += self.get_dates(repo_page, url)
                button = self.get_button(repo_page)
        return dates

    def create_table(self):
        """
        creating pandas df from dates list
        :return:
        """
        tbl = pd.DataFrame(self.dates)
        tbl['dates'] = [dt(int(y), int(m), int(d)) for y, m, d in tbl[['year', 'month', 'day']].values]
        tbl['weekday'] = [wday(d) for d in tbl['dates']]
        if self.save: tbl.to_csv(f'GiTime_{self.user}.csv')
        return tbl

    def calendar(self):
        """
        calculating the user calendar from the commits logs
        :return: user calendar table
        """
        tbl = {d: {h: 0 for h in range(24)} for d in DAYS}
        for d, h in self.table[['weekday', 'hour']].values:
            tbl[d][int(h)] += 1
        return pd.DataFrame(tbl)

    def invalid_branch(self, repo_page, repo_name):
        """
        dealing with main/master branch variance
        if repo_page invalid (404 error), the functions identify it, and crawl it propertly
        :param repo_page: repo crawled page (bs4 object)
        :param repo_name: repo name
        :return: fixed repo_page
        """
        if len(repo_page.find_all('img', class_='js-plaxify position-absolute')):
            sleep(self.slp)
            return crawl(main(repo_name))
        else:
            return repo_page

    def get_button(self, repo_page):
        """
        get scroll down link
        :param repo_page: repo crawled page (bs4 object)
        :return: link to next commits (if their is)
        """
        button = repo_page.find_all('a', class_='btn btn-outline BtnGroup-item')
        return button[-1] if len(button) else False

    def get_repos(self):
        """
        get repos links of given github user
        :return: all user repositories
        """
        elements = crawl(self.page).find_all('h3', class_='wb-break-all')
        return [h3.find('a').attrs[LINK] for h3 in elements]

    def get_dates(self, repo_page, repo_name):
        """
        find all commits from given bs4 object
        :param repo_page: repo crawled page (bs4 object)
        :param repo_name: url of the repo page
        :return: all dates from the given repo_page
        """
        dates = repo_page.find_all('relative-time', class_='no-wrap')
        return [date(d.attrs['datetime'], repo_name) for d in dates]

    def plot(self, size=8):
        """
        plot the user calculated calendar
        :param size: plot size
        """
        x_tp = size / self.clndr.shape[1]
        y_tp = (size * .75) / self.clndr.shape[0]

        plt.figure(figsize=(size, size * .75))
        plt.title(f'Calendar of {self.user} Github\n{len(self.dates)} commits in total', fontsize=14)
        plt.imshow(self.clndr ** .5, extent=[0, size, -size * .75, 0], cmap=CMP)
        plt.xticks([i * (x_tp) + (x_tp / 2) for i in range(self.clndr.shape[1])],
                   DAYS, fontsize=13, rotation=90)
        plt.yticks([-(y_tp) * i for i in range(self.clndr.shape[0] + 1)],
                   [f'{i}:00' for i in range(self.clndr.shape[0] + 1)])
        plt.colorbar().set_label(label='sqrt of commit number', size=12)
        plt.show()




