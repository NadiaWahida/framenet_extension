#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:52:04 2020

@author: nadia
"""
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import framenet as fn
#import json
        
def get_senti_score(word, POS='no'):
    """
    This function looks up a word (and optional it's POS-Tag) in SentiWordNet,
    adds up positive and negative Scores of the found synsets
    returns sum positive / negative scores

    Parameters
    ----------
    word : str
        Word to be looked up in SentiWordNet.
    POS : str
        POS-Tag of the word.

    Returns
    -------
    (pos,neg) : (float,float)

    """
    if POS == 'no':
        synsets = swn.senti_synsets(word)
    else:
        synsets = swn.senti_synsets(word,POS)
    scores = []
    pos, neg = 0, 0
    for synset in synsets:
        scores.append((synset.pos_score(),synset.neg_score()))
        pos += synset.pos_score()
        neg += synset.neg_score()
    #pos, neg = pos/len(scores), neg/len(scores)
    return(pos,neg)

def some():
    frames = fn.frames()
    #frames_of_interesed = ['Bragging']
    frames_of_interesed = ['Judgment', 'Judgment_communication','Judgment_direct_address','Regard', 'Labeling']#'Judgment_of_intensity'
    verbs_of_frames = {}
    for frame in frames:
        if frame.name in frames_of_interesed:
            lus = frame.lexUnit
            
            #for lu in lus.items():
                #if lu[0].endswith('.v'):
                    #print(lu)
                    #print(lu[1].definition)
                
            lus = [lu[0] for lu in lus.items() if lu[0].endswith('.v')]
            
            
            
            #print(len(lus))
            for lu in lus: 
                lu = lu.split('.')
                #print(lu)
                print(lu[0],lu[1])
                #print(type(lu[0]),type(lu[1]))
                print(get_senti_score(lu[0],lu[1]))
                print('-'*20)
#some()

def same():
    frames = fn.frames()
    for frame in frames:
        if frame.name.endswith('ing'):
            print(frame.name)
same()
#for s in swn.senti_synsets('like'):
    #print(s)
    #print(type(s.pos_score()))