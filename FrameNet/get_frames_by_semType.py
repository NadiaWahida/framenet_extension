#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 17:09 2019

@author: nadia, sanaz
"""
from nltk.corpus import framenet as fn


frames = fn.frames()
for frame in frames:
    # Hier Code um auf lexicalUnits


    if len(frame.semTypes) ==0: continue
    for type in frame.semTypes:
            if type.name == 'Positive_judgment' or type.name == 'End_of_scale':
                    print(frame.name)

