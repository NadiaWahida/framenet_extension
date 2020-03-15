#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 16:29 2019

@author: Sanaz Safdel

This Modul searches for the LUs with semantic type ['Positive_judgment', 'End_of_scale', 'Negative', 'Negative_judgment'] in FrameNet 
"""
from nltk.corpus import framenet as fn
import json

OUTPUT = '../Data/lus_by_semtypes.txt'
SEM_TYPES = '../Data/senti_semantic_types.txt'
# input
with open(SEM_TYPES,'r') as f:
    words = [line.strip() for line in f.readlines()]
#words = ['Positive_judgment', 'End_of_scale', 'Negative', 'Negative_judgment']
i=0
lu_dict = dict()
frames = fn.frames()
#iterate over Semantic types in Words (semTypes from Input)
for word in words:
    lu_dict[word] = []
    #iterate over frames in FrameNet
    for frame in frames:
        #print(frame)
        lus = frame.lexUnit
        # iterate over LUs ID in all lexical units
        for lu_id in lus.items():
            semtype = lu_id[1].semTypes
            #print(lu_id) 
            # iterate over types in semtype
            for type in semtype:
                #print(type)
                if type.name == word:
                    i+=1
                    # print Lexical Units, LU ID, frame and frame ID into lu_dict 
                    lu_dict[word].append({'lu': lu_id[0], 'lu_id': lu_id[1].ID, 'frame': frame.name, 'frame_id': frame.ID})
                    # write to the OUTPUT
                    with open(OUTPUT,'a') as f:
                        f.writelines(lu_id[0] + '\n' +  str(lu_id[1].ID) + '\n' + frame.name+'\n' + str(frame.ID) + '\n' + word)
                        f.writelines('\n\n')  
                        
print(i,' Lexical Units gefunden')
# write to file
with open('../Data/lus_by_semtypes.json', 'w') as f:
    json.dump(lu_dict, f)

