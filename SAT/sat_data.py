#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:46:22 2018

@author: edss
"""

import pandas as pd
import numpy as np

files = ["ap_2010.csv","class_size.csv","demographics.csv","graduation.csv","math_test_results.csv","sat_results.csv"]

data = {}
for f in files:
    d = pd.read_csv("".format(f))
    data[f.replace(".csv","")] = d