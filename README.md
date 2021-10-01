# Github-Commits-Crawling
Scraping all of the github-commits dates of given user

## Overview
Many github users spend long hours to improve and upgrade their codes. Any changes made in particular repository are saved and documented as **"commits"**. These commits allow the user to track the changes he has made and document them in an orderly fashion. This repo also as commits page, and you can see it here: [**commits**](https://github.com/EtzionR/Github-Commits-Crawling/commits/main)

The idea behind this code is simple: use these commits not only as documentation, but as **Data**. this data allows the user to learn about himself and his behavior. Since all commits are attached to their execution date, you can learn about the user work schedule. Therefore, the user's calendar can be drawn using the user's commits throughout his activity on github. For this use, the code [**gitime.py**](https://github.com/EtzionR/Github-Commits-Crawling/blob/main/gitime.py) created.

The code is based on a number of key steps:
1. The code gets the name of the user's github profile and uses it to turn to a page that centralizes all its **repositories**.
2. All links to the various repo scraped using **bs4**.
3. Now, the code goes over each repo, and **crawls over its commits**.
4. The crawled commits are converted into a **summarized table**, which can be saved or converted to a calendar output.

During the work process, there are **one-second breaks** between each crawl request. This time period can be changed using the **"slp"** variable.

In addition, the code is built to deal with the difference between **main repo** and **master repo**. As you know, in 2020 it was decided to stop using the term "master" in github routings and use the term main instead (you can read more on this here: [renaming](# https://github.com/github/renaming)). Therefore, the code deals with the fact that some commits are kept under "**main**" routing and some are still under "**master**".

Also, the commits are saved so that **only 35 records** can be kept on each page. Therefore, to scrap all the commits of repo with more than 35 commits, the code uses the link of the scroll down button. By doing so, it be possible to reach the pages where the additional commits are stored.

After the code ended the Scraping proccess, it isolates only the dates of the commits and arranges them into a summary table. It keeps this table on the local computer of the user (by default, in the path where the user is working). An example of such a table can be seen here:

| repo | year | month | day | hour | minutes | seconds | dates | weekday |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| /EtzionR/Github-Commits-Crawling | 2021 | 10 | 01 | 10 | 59 | 43 | 2021-10-01 | Friday |
| /EtzionR/Github-Commits-Crawling | 2021 | 10 | 01 | 10 | 53 | 18 | 2021-10-01 | Friday |
| /EtzionR/Github-Commits-Crawling | 2021 | 10 | 01 | 10 | 52 | 52 | 2021-10-01 | Friday |
| /EtzionR/Github-Commits-Crawling | 2021 | 10 | 01 | 10 | 52 | 44 | 2021-10-01 | Friday |
| /EtzionR/Github-Commits-Crawling | 2021 | 10 | 01 | 10 | 51 | 43 | 2021-10-01 | Friday |

Also, the data is converted to a **Calendar Table**, which can also be accessed (**GiTime('user'**).clndr) and can also be plotted automatically:

``` sh
# import GiTime object
from gitime import GiTime

# using the object on "EtzionR" Github user
GiTime('EtzionR').plot()

# resulting plot:
```
![calendar](https://github.com/EtzionR/Github-Commits-Crawling/blob/main/outputs/calendar_.png)

This example is based on [my private github](https://github.com/EtzionR). As you can see, the calendar produced shows that I do not work at all between 1:00 and 7:00, and also refrains from working on weekends. Also, you can see that most of my work on github is concentrated in the middle of the week.

As you can see, this product can better teach the user how he divides his working hours throughout the week and allows him to become more efficient and learn about his own activities

**Note**: The code indicates at each stage which repo it scraping. If the user github contains a large amount of commits and repositorie, it will take the code some time to run

## Libraries
The code uses the following libraries in Python:

**BeautifulSoup** (bs4)

**matplotlib**

**requests**

**datetime**

**pandas**


## Application
An application of the code is attached to this page under the name: 

[**"implementation.py"**](https://github.com/EtzionR/Github-Commits-Crawling/blob/main/implementation.py)

the examples outputs are also attached here.


## Example for using the code
To use this code, you just need to import it as follows:
``` sh
# import GiTime object
from gitime import GiTime

# application 
GiTime('user')
```

When the variables displayed are:

**user:** given github user you want to scrap all of it commits

**save:** save the commits to csv file (bool, defualt: True)

**slp:** sleep time between crawling sessions

## License
MIT © [Etzion Harari](https://github.com/EtzionData)
