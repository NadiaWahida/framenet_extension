#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:06:06 2019

@author: nadia
"""
import json

INPUT = '../Data/lus_by_semtypes.json'


with open(INPUT, 'r') as f:
    lu_dict = json.load(f)

frame_dict = {}
for t in lu_dict:
    frame_dict[t] = {}
    for lu in lu_dict[t]:
        if lu['frame'] not in frame_dict[t].keys():
            frame_dict[t][lu['frame']] = 1
        else:
            frame_dict[t][lu['frame']] += 1
            
def get_numbers(d):
    numbers_of_frames = sorted([(v,k) for (k,v) in d.items()])
    return numbers_of_frames

for t in frame_dict:
    print(t)
    for frame in get_numbers(frame_dict[t]):
        print((frame[1],frame[0]))
    print(len(get_numbers(frame_dict[t])))