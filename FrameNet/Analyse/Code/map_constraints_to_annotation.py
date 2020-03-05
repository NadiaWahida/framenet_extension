#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:11:35 2020

@author: nadia
"""
import json
import re

FRAME_POLARITY = '../Data/Senti_Frames_mit_Framepolarity.txt'
CONSTRAINTS = '../Data/Constraints/Frameconstraints_with_Polarity.json'
ANNOTATIONS = '../Data/annotated_sents_from_FrameNet.txt'

pattern = re.compile('([a-zA-Z_]+)\.([a-zA-Z_]+)')

def map_constraints_to_annotation(annotation, constraints):
    #annotation = {'lu':lu, 'frame':frame, 'text':text, 'Target':target, 'FE':fes, 'FE_unexpr': unexpr}
    constraints = constraints[annotation['frame']]
    suitable = []
    for fe in annotation['FE']:
        for constraint in constraints:
            if fe in constraint:
                suitable.append(constraint)
    suitable = list(set(suitable))
    for constraint in suitable:
        original = constraint
        if constraint.count('.') == 1:   
            try:
                constraint = constraint.replace(re.search(pattern,constraint).group(), annotation['FE'][re.search(pattern,constraint).group(2)])
                constraint = constraint.replace('?_s','_SOMEONE')
                constraint = constraint.replace('?_t','_SOMETHING')
                constraint = constraint.replace('?_x','_GENERAL')
            except:
                continue
            #print(constraint)
        elif constraint.count('.') == 2:
            try:
                constraint = constraint.replace(re.search(pattern,constraint).group(), annotation['FE'][re.search(pattern,constraint).group(2)])
            except:
                continue
            try:
                constraint = constraint.replace(re.search(pattern,constraint).group(), annotation['FE'][re.search(pattern,constraint).group(2)])
            except: continue
            #print(constraint)
        #else:
        constraint = constraint.replace('neg','    -- negative ->   ')
        constraint = constraint.replace('pos','    -- positive ->    ')
        print(constraint)
        

if __name__ == '__main__':
    with open(CONSTRAINTS,'r') as f:
        constraints = json.load(f)
    with open(FRAME_POLARITY,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    with open(ANNOTATIONS,'r') as f:
        annotations = [eval(line.strip()) for line in f.readlines()]
    #annotation = annotations[0]
    i=0
    while i<10:
        for annotation in annotations:
            map_constraints_to_annotation(annotation, constraints)
            i+=1