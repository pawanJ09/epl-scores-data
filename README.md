# English Premier League Historical Scores

This is a utility app that returns the scores since inception of English Premier League in 1992-93. 
This app is fetching the historical data by using Web scraping. I have used BeautifulSoup 
library to achieve this as requests-html could not be used with Python version 3.9.

## Requirements

For building and running the application you need:

- [Python3](https://www.python.org/downloads/)

```shell
python3 -m pip install requests

python3 -m pip install bs4

python3 -m pip install lxml
```

## Running the application locally

You can run the main.py program to get started. This file has the __main__ method.

```shell
python main.py
```

## Build and Run using Docker

### Build image

```shell
docker build --tag <> .
```

### Run the container from built image

Here we use -it for interactive terminal since we have to input the city from user.

```shell
docker run --name <> -p 1001:1001 -it <>
```

### Start the container if re-executing the image

```shell
docker start <> -i
```

### Run using image from Docker hub

```shell
docker pull docker pull <>

docker run --name <> -p 1001:1001 -it <>
```

