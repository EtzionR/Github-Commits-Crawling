# Github-Commits-Crawling
Scraping all of the github-commits dates of given user

## Overview

``` sh
# import GiTime object
from gitime import GiTime

# using the object on "EtzionR" Github user
GiTime('EtzionR').plot()

# resulting plot:
```

![calendar](https://github.com/EtzionR/Github-Commits-Crawling/blob/main/outputs/calendar.png)

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

# application (on "EtzionR" user)
GiTime('EtzionR')
```

When the variables displayed are:

**user:** given github user you want to scrap all of it commits

**save:** save the commits to csv file (bool, defualt: True)

**slp:** sleep time between crawling sessions

## License
MIT © [Etzion Harari](https://github.com/EtzionData)
