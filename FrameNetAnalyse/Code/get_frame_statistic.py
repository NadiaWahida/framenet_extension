#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:06:06 2019

@author: Nadia Arslan

This module iterates over all LUs from Semantic Type Positive_judgment, Negative_judgment, Negative and End_of_scale
to find the Frames they can evoke.
Prints information of SemType and corresponding frames and number of occurance of that frame.
It was written to make a diagram for the report
"""
import json

INPUT = '../Data/lus_by_semtypes.json'

with open(INPUT, 'r') as f:
    lu_dict = json.load(f)

# lu_dict: {Semantic_Type: [{"lu": "adorn.v", "lu_id": 1631, "frame": "Distributed_position", "frame_id": 76}, ...],...}

frame_dict = {}
for t in lu_dict:
    frame_dict[t] = {}
    for lu in lu_dict[t]:
        if lu['frame'] not in frame_dict[t].keys():
            frame_dict[t][lu['frame']] = 1
        else:
            frame_dict[t][lu['frame']] += 1
            
# frame_dict: {Semantic_Type: {Frame_name: occurance, ...}, ...}
        
def get_numbers(d):
    """
    This function returns the sorted (value, key) pair of a dictionary
    """
    numbers_of_frames = sorted([(v,k) for (k,v) in d.items()])
    return numbers_of_frames

# itearte over frame_dict
for t in frame_dict:
    # print semantic type
    print(t)
    # iterate over frames in frame_dict (pro semTyppe)
    for frame in get_numbers(frame_dict[t]):
        # print frame and number of occurance
        print((frame[1],frame[0]))
    # print number of evoked frames per semType
    print(len(get_numbers(frame_dict[t])))
