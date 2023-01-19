import requests
import os
from decouple import config


# session to attact headers for each request
def mysession() : 
    session = requests.session()
    session.headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token ' + config('TOKEN'),
        'User-Agent': 'GithubEmailHarvest',
    }
    return session