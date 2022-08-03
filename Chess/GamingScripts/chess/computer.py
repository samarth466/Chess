import json
import os
import numpy
import pandas as pd
import neurolab
import chess
from lichess.api import users_by_team, user


with open('data.json', 'w') as f:
    data = {}
    for username in users_by_team('lichess-swiss', auth='lip_TAUNLVwqjQK2v7ArdWsI'):
        print(data)
        data[username] = user(username, auth='lip_TAUNLVwqjQK2v7ArdWsI')
        print(data)
    json.dump(data, f)
