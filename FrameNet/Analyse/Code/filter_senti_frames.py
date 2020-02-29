#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:32:23 2020

@author: nadia
"""
from nltk.corpus import framenet as fn


INPUT = '../Data/Senti_Frames.txt'


def check_fes(fes):
    
    source_fes = ['Experiencer','Speaker','Cognizer','Affected_party','Protagonist','Resource_controller'] 
    target_fes = ['Evaluee','Event','Topic','Content','Message','Behavior']
    #source = False
    #target = False
    source = []
    target = []
    for fe in fes:
        if fe in source_fes: 
            #source = True
            source.append(fe)
        elif fe in target_fes: 
            #target = True
            target.append(fe)
    #if source==True and target==True:
        #return True
    if len(source)>0 and len(target)>0:
        return(source, target)
    else: return False

def get_frames(senti_frames):
    frames = fn.frames()
    for frame in frames:
        if frame.name in senti_frames:
            fes = frame.FE
            fe_check = check_fes(fes)
            if fe_check!=False:
                print(frame.name)
                print('source:\n', fe_check[0])
                print('\ntarget:\n', fe_check[1])
                print('-'*20)
            
if __name__ == '__main__':
    
    with open(INPUT,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    
    get_frames(senti_frames)