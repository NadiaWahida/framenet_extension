#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 16:29 2019

@author: Sanaz Safdel
"""
from nltk.corpus import framenet as fn
import json

OUTPUT = '../Data/lus_by_semtypes.txt'
SEM_TYPES = '../Data/senti_semantic_types.txt'

with open(SEM_TYPES,'r') as f:
    words = [line.strip() for line in f.readlines()]
#words = ['Positive_judgment', 'End_of_scale', 'Negative', 'Negative_judgment']
i=0
lu_dict = dict()
frames = fn.frames()
for word in words:
    lu_dict[word] = []
    for frame in frames:
        #print(frame)
        lus = frame.lexUnit
        for lu_id in lus.items():
            semtype = lu_id[1].semTypes
            #print(lu_id) 
            for type in semtype:
                #print(type)
                if type.name == word:
                    i+=1
                    lu_dict[word].append({'lu': lu_id[0], 'lu_id': lu_id[1].ID, 'frame': frame.name, 'frame_id': frame.ID})
                    with open(OUTPUT,'a') as f:
                        f.writelines(lu_id[0] + '\n' +  str(lu_id[1].ID) + '\n' + frame.name+'\n' + str(frame.ID) + '\n' + word)
                        f.writelines('\n\n')  
                        
print(i,' Lexical Units gefunden')
with open('../Data/lus_by_semtypes.json', 'w') as f:
    json.dump(lu_dict, f)
