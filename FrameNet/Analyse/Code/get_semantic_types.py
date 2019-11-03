#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:39:38 2019

@author: nadia

Code gets all Semantic Types in FrameNet
writes them to a file
"""
from nltk.corpus import framenet as fn

SEMTYPES = '../Data/all_semantic_types.txt'
NUMBERS = '../Data/all_semantic_types_by_occurance.txt'

frames = fn.frames()
sem_types = []
sem_types_dict = {}

# iterates over frames and extract Semantic Types
for frame in frames:
    for lu_id in frame.lexUnit.items():
        for sem_type in lu_id[1].semTypes:
            sem_types.append(sem_type.name)

# counts number of occurence of Semantic Types
for sem_type in sem_types:
    if sem_type not in sem_types_dict.keys():
        sem_types_dict[sem_type] = 1
    else:
        sem_types_dict[sem_type] += 1
numbers_of_types = sorted([(v,k) for (k,v) in sem_types_dict.items()])
# sorts and removes duplicates        
sem_types = sorted(list(set(sem_types)))

# write to file
with open(SEMTYPES, 'w') as f:
    for sem_type in sem_types:
        f.writelines(sem_type+'\n')
        #print(type)
with open(NUMBERS, 'w') as f:
    for sem_type in numbers_of_types:
        f.writelines(str(sem_type[0])+'\t'+sem_type[1]+'\n')
