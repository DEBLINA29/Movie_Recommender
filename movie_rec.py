# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:11:18 2023

@author: debli
"""

import numpy as np
import pandas as pd

Movies = pd.read_csv("tmdb_5000_movies.csv")
Credits = pd.read_csv("tmdb_5000_credits.csv")

Movies.head(1)