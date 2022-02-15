# English Premier League Historical Scores

This is a utility app that returns the scores since inception of English Premier League in 1992-93. 
This app is fetching the historical data by using Web scraping. This project has dependency on 
Selenium as we need to fetch the HTML content for the EPL season's data being fetched using 
infinite scrolling. Another key dependency is on BeautifulSoup library to parse the HTML page 
source.

Note: This app is currently compatible with MacOS Safari driver hence cannot be run in 
containers or any other OS.

## Requirements

For building and running the application you need:

- [Python3](https://www.python.org/downloads/)

```shell
python3 -m pip install selenium

python3 -m pip install bs4
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

