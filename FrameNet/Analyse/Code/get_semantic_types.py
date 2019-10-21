#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:39:38 2019

@author: nadia
"""
from nltk.corpus import framenet as fn

OUTPUT = './all_sementic_types.txt'

frames = fn.frames()
sem_types = []

for frame in frames:
    for lu_id in frame.lexUnit.items():
        for sem_type in lu_id[1].semTypes:
            sem_types.append(sem_type.name)
            
sem_types = sorted(list(set(sem_types)))

with open(OUTPUT, 'w') as f:
    for sem_type in sem_types:
        f.writelines(sem_type+'\n')
        #print(type)
    