#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:38:22 2020

@author: nadia

This module reshapes constraints of SentiFrames and stores them to a dictionary,
'../Data/Constraints/Frameconstraints_with_Polarity.json',
like: {frame:['constraint1','constraint2',...],...}
"""
import os
import json
INPUT = '../Data/Constraints/Frameconstraints_with_Polarity/'
OUT = '../Data/Constraints/Frameconstraints_with_Polarity.json'

constraint_dict = {}
for file in os.listdir(INPUT):
    frame = file.replace('.txt','')
    rules= []
    with open(INPUT+file,'r') as f:
        constraints = [line.strip() for line in f.readlines()[1:]]
    for c in constraints:
        s = c.split('--')[0].replace('<Source=','')
        t = c.split('->')[1].replace('Target=','').replace('>','')
        p = c.split(' -- ')[1].split(' -> ')[0].replace('Polarity=','')
        rules.append(s+p+t)
        print(s+p+t)
    constraint_dict[frame] = rules
print(constraint_dict)
with open(OUT,'w') as f:
    json.dump(constraint_dict,f)
