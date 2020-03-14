#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:24:18 2020

@author: Nadia Arslan

Dieses Modul sucht die Frame-Relationen der Judgment*-Frames in FrameNet 
und gibt sie auf die Konsole aus

judgment_frames = ['Judgment', 'Judgment_communication','Judgment_direct_address','Judgment_of_intensity']
"""

from nltk.corpus import framenet as fn

frames = fn.frames()
frame_relations = []

for frame in frames:
    for relation in frame.frameRelations:
        if 'Judgment' in str(relation):
            if relation not in frame_relations:
                frame_relations.append(relation)
                
print("Die Judgment*-Frames haben ", len(frame_relations), " Relationen:\n\n")
          
for rel in frame_relations:
        print(rel)