#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:22:56 2020

@author: Nadia Arslan

This module gets annotated sentences for SentiFrames from FrameNet,
saves them in the file: '../Data/annotated_sents_from_FrameNet.txt',
one dictionary a line
dict like: {'lu':lu, 'frame':frame, 'text':text, 'Target':target, 'FE':fes}
"""
from nltk.corpus import framenet as fn
FRAME_POLARITY = '../Data/Senti_Frames_mit_Framepolarity.txt'
INPUT = '../Data/Senti_Frames.txt'
OUTPUT = '../Data/annotated_sents_from_FrameNet.txt'

def filter_annotation(lu, annotation):    
    """
    This function filters an annotated sentence from FrameNet 
    if sentence evokes a SentiFrame and sentence has at least three Frameelements,
    returns a reshaped form of that sentence like:
    {'text':text, 'Target':target, 'FE':fes, 'frame':frame}
    
    Parameters
    ----------
    lu : str
        Lexical Unit.
    annotation : nltk.corpus.reader.framenet.AttrDict
        annotated sentence from FrameNet.

    Returns
    -------
    dict
        information about annotated sentence.

    """
    lu_in_txt = ' '+lu.split('.')[0][:-1]
    if lu_in_txt not in annotation.text:
        return {}
    frame = annotation.frame.name
    if frame not in senti_frames:
        return {}
    fes = annotation.FE[0]
    if len(fes)<3:
        return {}
    text = annotation.text
    target = ''
    for el in annotation.Target:
        target += text[el[0]:el[1]]+' '
    fes = {}
    for el in annotation.FE[0]:
        fes[el[2]] = text[el[0]:el[1]]
    sent_info = {'lu':lu, 'frame':frame, 'text':text, 'Target':target, 'FE':fes}
    return sent_info
    
    
def get_annotations(lu):
    """
    This function gets the annotations of a LexicalUnit from FrameNet,
    writes them to a file, one sentence a line

    Parameters
    ----------
    lu : str
        Lexical Unit.

    Returns
    -------
    None.

    """
    
    annotations = fn.annotations(lu)
    for annotation in annotations:
        sent_info = filter_annotation(lu, annotation)
        if len(sent_info) == 0:
            continue
        with open(OUTPUT,'a') as f:
            f.writelines(str(sent_info)+'\n')    
    with open(OUTPUT,'r') as f:
        data = list(set([eval(line.strip()) for line in f.readlines()]))
    with open(OUTPUT,'w') as f:
        for line in data:
            f.writelines(str(line)+'\n')
            
if __name__ == '__main__':
    
    with open(INPUT,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    for senti_frame in senti_frames:
        frame = fn.frame(senti_frame)
        for lu in frame.lexUnit:
            try:
                get_annotations(lu)
            except:
                continue