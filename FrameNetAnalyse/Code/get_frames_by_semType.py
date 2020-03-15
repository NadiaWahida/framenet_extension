#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 17:09 2019

@author: sanaz
This Modul searches for the frames with semantic type ['Positive_judgment', 'End_of_scale', 'Negative', 'Negative_judgment'] in FrameNet. 
"""
from nltk.corpus import framenet as fn
import json

# input
SEM_TYPES = './senti_semantic_types.txt'
OUTPUT = './frames_by_semtypes.json'

with open(SEM_TYPES,'r') as f:
    sem_types = [line.strip() for line in f.readlines()]
# all frame in FrameNet   
frames = fn.frames()

frame_dict = {sem_type:[] for sem_type in sem_types}
# iterate over frames in FrameNet    
for frame in frames:
	# iterate over semantic type in frame with semantic type 
    for sem_type in frame.semTypes:
		# if this semantic type in frame.sem_types 
        if sem_type.name in sem_types:
			# print frame and frame ID  with semantic type from input into frame_dict  
            # print(frame.name, frame.ID)
            frame_dict[sem_type.name].append({'frame_name': frame.name, 'frame_id': frame.ID})
# write to the OUTPUT
with open(OUTPUT, 'w') as f:
    json.dump(frame_dict, f)
    
#print(frame_dict)

