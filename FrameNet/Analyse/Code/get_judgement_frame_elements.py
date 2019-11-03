#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:29:53 2019

@author: Nadia Arslan
"""
from nltk.corpus import framenet as fn
import json

INPUT = '../Data/lus_by_semtypes.json'
OUTPUT = '../Data/jugement_type_lus_and_sr.json'

with open(INPUT, 'r') as f:
    lu_dict = json.load(f)
    
frames = fn.frames()
sem_types = ['Positive_judgment', 'Negative_judgment']
judgement_type_lu_dict = {'Positive_judgment':[],'Negative_judgment':[]}

fes = []

for sem_type in sem_types:
    for lu in lu_dict[sem_type]:
        frame = fn.frame(lu['frame_id'])
        frame_elements = list(frame.FE.keys())
        #if frame_elements not in fes:
            #fes.append(frame_elements)
        fes += frame_elements
        lu['FE'] = frame_elements #list(frame.FE.keys())
        judgement_type_lu_dict[sem_type].append(lu)
       
with open(OUTPUT, 'w') as f:
    json.dump(judgement_type_lu_dict, f)
    
#print(judgement_type_lu_dict)

print(list(set(fes)))