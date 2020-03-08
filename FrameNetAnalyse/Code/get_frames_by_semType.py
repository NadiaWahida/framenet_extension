#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 17:09 2019

@author: sanaz
"""
from nltk.corpus import framenet as fn
import json

SEM_TYPES = './senti_semantic_types.txt'
OUTPUT = './frames_by_semtypes.json'

with open(SEM_TYPES,'r') as f:
    sem_types = [line.strip() for line in f.readlines()]
    
frames = fn.frames()
frame_dict = {sem_type:[] for sem_type in sem_types}
    
for frame in frames:
    for sem_type in frame.semTypes:
        if sem_type.name in sem_types:
            print(frame.name, frame.ID)
            frame_dict[sem_type.name].append({'frame_name': frame.name, 'frame_id': frame.ID})

with open(OUTPUT, 'w') as f:
    json.dump(frame_dict, f)
    
#print(frame_dict)
