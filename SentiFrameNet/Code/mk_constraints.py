#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:32:23 2020

@author: Nadia Arslan

This module makes Constraints for SentiFrames.

"""
from nltk.corpus import framenet as fn


INPUT = '../Data/Senti_Frames.txt'
FRAME_POLARITY = '../Data/Senti_Frames_mit_Framepolarity.txt'
SOURCE = '../Data/source_elements.txt'
TARGET ='../Data/target_elements.txt'
OUTPUT = '../Data/Constraints/'


def map_fes(senti_frame):
    """
    This function iterates over the Frame Elements of a SentiFrame
    and mapps them to source or target of opinion then
    calls the function write_constraints()

    Parameters
    ----------
    senti_frame : class 'nltk.corpus.reader.framenet.AttrDict'
        A FrameNet Frame.

    Returns
    -------
    bool
        True for Mapping completed,
        False for Fail.
    """
    fes = senti_frame.FE
    frame_name = senti_frame.name
    source = []
    target = []
    for fe in fes.items():
        if fe[0] in source_elements:
            source.append(fe[0])
        if fe[0] in target_elements:
            target.append(fe[0])
    if len(source)==0 and len(target)==0:
        return False
    else:
        write_constraints(source, target, frame_name)
        return True
    
def write_constraints(source, target, frame_name):
    """
    This function writes SentiConstraints for a given SentiFrame

    Parameters
    ----------
    source : list
        List of possible Source Elements of SentiFrame.
    target : list
        List of possible Target Elements of SentiFrame.
    frame_name : str
        Name of SentiFrame.
    """
    constraints = []
    if frame_name in senti_frame_polarity:
        polarity = 'Polarity='
        constraints.append(('<Source=?_x',' -- '+polarity+' -> ', 'Target='+frame_name+'>'))
        path = OUTPUT+'Frameconstraints_with_Polarity/'+frame_name+'.txt'
    else:
        polarity = 'Polarity=?_p'
        constraints.append(('<Source=?_x',' -- '+polarity+' -> ', 'Target='+frame_name+'.?_lu>'))
        path = OUTPUT+'Frameconstraints_without_Polarity/'+frame_name+'.txt'
    for s in source:
        for s2 in source:
            if s != s2:
                constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target='+frame_name+'.'+s2+'>'))
        for t in target:
            constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target='+frame_name+'.'+t+'>'))    
        constraints.append(('<Source='+frame_name+'.'+s,' -- '+polarity+' -> ', 'Target=?_t>'))
    if len(source)>1:
        for s in source:
            constraints.append(('<Source=?_s',' -- '+polarity+' -> ', 'Target='+frame_name+'.'+s+'>'))
    for t in target:
        constraints.append(('<Source=?_s',' -- '+polarity+' -> ', 'Target='+frame_name+'.'+t+'>'))
        
    #with open(path,'w') as f:
        #f.writelines(frame_name+'\t'+ '\t'.join(source)+'\t'+ '\t'.join(target)+'\n')
        #for c in constraints:
            #f.writelines(c[0]+c[1]+c[2]+'\n')
    
            
if __name__ == '__main__':
    
    with open(INPUT,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    with open(FRAME_POLARITY, 'r') as f:
        senti_frame_polarity = [line.strip() for line in f.readlines()]
    with open(SOURCE, 'r') as f:
        source_elements = [line.strip() for line in f.readlines()]
    with open(TARGET, 'r') as f:
        target_elements = [line.strip() for line in f.readlines()]
        
    frames_without_mapping = []
    for senti_frame in senti_frames:
        senti_frame = fn.frame(senti_frame)
        if not map_fes(senti_frame):
            frames_without_mapping.append(senti_frame.name)      
    print('\n Constructed Constraints for ',len(senti_frames),' SentiFrames \n')
    print('Frames without mapping: ',frames_without_mapping)
