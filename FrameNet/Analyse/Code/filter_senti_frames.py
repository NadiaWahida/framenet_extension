#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:32:23 2020

@author: nadia
"""
from nltk.corpus import framenet as fn


INPUT = '../Data/Senti_Frames.txt'
FRAME_POLARITY = '../Data/Senti_Frames_mit_Framepolarity.txt'
OUTPUT = '../Data/Constraints/'

def check_if_senti_source(fe):
    sentients = ['Human','Sentient']
    subjects = ['Experiencer','Adressee','Speaker','Affected_party','Protagonist','Resource_controller','Cognizer','Assailant']
    if fe[1].definition:
        if fe[1].definition.split()[1] == 'individual':
            return True
    if fe[1].semType:
        if fe[1].semType.name in sentients:
            return True
    if fe[0] in subjects:
        return True
    return False

def check_if_senti_target(fe):
    objects = ['Evaluee','Event','Topic','Content','Message','Behavior','Entity']
    more_o = ['Undesirable_situation','Stimulus', 'Asset','Harmful_event','Dangerous_entity','Action','Patient','State_of_affairs']
    objects = objects + more_o
    if fe[0] in objects:
        return True
    return False

def check_fes(fes, frame_name):
    source = []
    target = []
    for fe in fes.items():
        if check_if_senti_source(fe):
            source.append(fe[0])
        if check_if_senti_target(fe):
            target.append(fe[0])
        #print('='*20)
        #print(fe[0])
        #if fe[1].definition:
            #print(fe[1].definition)
        #print('='*20)
    #print(source)
    #print(target)
    #print('+'*50)
    #print('+'*50)
    if len(source)==0 and len(target)==0:
        return False
    else:
        if frame_name in senti_frame_polarity:
            a=1
            write_constraints_frame_polarity(source, target, frame_name)
        else:
            a=1
            #write_constraints_no_polarity(source, target, frame_name)
        return True

def write_constraints_no_polarity(source, target, frame_name):
    polarity = 'Polarity=?_lu'
    constraints = []
    for s in source:
        for s2 in source:
            if s != s2:
                constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target='+frame_name+'.'+s2+'>'))
        for t in target:
            constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target='+frame_name+'.'+t+'>'))
        if len(target) == 0 and len(source) == 1:
            constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target=?_t>'))
    if len(source) == 0:
        for t in target:
            constraints.append(('<Source=?_s',' -- '+polarity+' -> ', 'Target='+frame_name+'.'+t+'>'))
    with open(OUTPUT+frame_name+'.txt','w') as f:
        for c in constraints:
            f.writelines(c[0]+c[1]+c[2]+'\n')
    
    
def write_constraints_frame_polarity(source, target, frame_name):
    polarity = 'Polarity='
    constraints = []
    for s in source:
        for s2 in source:
            if s != s2:
                constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target='+frame_name+'.'+s2+'>'))
        for t in target:
            constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target='+frame_name+'.'+t+'>'))
        if len(target) == 0 and len(source) == 1:
            constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target=?_t>'))
    if len(source) == 0:
        for t in target:
            constraints.append(('<Source=?_s',' -- '+polarity+' -> ', 'Target='+frame_name+'.'+t+'>'))
    constraints.append(('<Source=?_x',' -- '+polarity+' -> ', 'Target='+frame_name+'>'))
    
    with open(OUTPUT+frame_name+'.txt','w') as f:
        for c in constraints:
            f.writelines(c[0]+c[1]+c[2]+'\n')

def get_frames(senti_frames):
    frames_without_mapping = []
    for senti_frame in senti_frames:
        senti_frame = fn.frame(senti_frame)
        #print(senti_frame.name)
        fes = senti_frame.FE
        if not check_fes(fes, senti_frame.name):
            frames_without_mapping.append(senti_frame.name)
    print(len(senti_frames))
    print(frames_without_mapping)
            
if __name__ == '__main__':
    
    with open(INPUT,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    with open(FRAME_POLARITY, 'r') as f:
        senti_frame_polarity = [line.strip() for line in f.readlines()]
    
    get_frames(senti_frames)