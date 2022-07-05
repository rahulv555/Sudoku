import requests


def getSudoku():
    response = requests.get(
        "https://sugoku.herokuapp.com/board?difficulty=easy")
    grid = response.json()['board']
    return grid
