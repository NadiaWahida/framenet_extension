#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:52:04 2020

@author: nadia
"""
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import framenet as fn
import networkx as nx
#import re
#import json
INPUT = '../Data/Senti_Frames.txt'
OUTPUT = '../Data/Senti_Frame_Neighbour.txt'
        
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

def get_fes_relations(senti_frames):
    """
    This function gets FrameElementRelations between SentiFrames,
    if Relation is Inheritance or See_also and FEs have a different name,
    returns them in a list of triples.

    Parameters
    ----------
    senti_frames : list
        List of SentiFrames.

    Returns
    -------
    frame_rel : list of tripples
        [(SuperFrame.FE, Relation, SubFrame.FE),...]

    """
    fes_rel = []
    for senti_frame in senti_frames:
        senti_frame = fn.frame(senti_frame)
        frame_relations = senti_frame.frameRelations
        for rel in frame_relations:
            for fe_rel in rel.feRelations:
                """
                fe_rel.keys() =
                dict_keys(['subID', 'supID', 'subFEName', 'superFEName', 'ID', '_type', 
                'frameRelation', 'type', 'superFrame', 'subFrame', 'superFE', 'subFE'])
                """
                if fe_rel.superFrame.name in senti_frames and fe_rel.subFrame.name in senti_frames:
                    fe_rel_name = str(fe_rel).split('-- ')[1].split(' ->')[0]
                    if fe_rel_name == 'See_also' or fe_rel_name == 'Inheritance': #'ReFraming_Mapping'
                        if fe_rel.superFEName != fe_rel.subFEName:
                            sup = fe_rel.superFrame.name+'.'+fe_rel.superFEName
                            sub = fe_rel.subFrame.name+'.'+fe_rel.subFEName
                            fes_rel.append((sup, fe_rel_name, sub))
                            #print((sup, fe_rel_name, sub))
    fes_rel = list(set(fes_rel))
    return fes_rel                       
                            
def get_frame_relations(senti_frames):
    """
    This function gets all FrameRelations between SentiFrames,
    returns them in a list of triples.

    Parameters
    ----------
    senti_frames : list
        List of SentiFrames.

    Returns
    -------
    frame_rel : list of tripples
        [(SuperFrame, Relation, SubFrame),...]

    """
    frame_rel = []  
    for senti_frame in senti_frames:
        senti_frame = fn.frame(senti_frame)
        frame_relations = senti_frame.frameRelations
        for rel in frame_relations:
            """ 
            print(rel) = <Parent=Telling -- Inheritance -> Child=Warning>
            rel.keys() =
            dict_keys(['subID', 'supID', 'subFrameName', 'superFrameName', 'ID', '_type', 
                       'feRelations', 'type', 'superFrame', 'Parent', 'subFrame', 'Child'])
            """
            if rel.superFrameName in senti_frames and rel.subFrameName in senti_frames:
                rel_name = str(rel).split('-- ')[1].split(' ->')[0]
                frame_rel.append((rel.superFrameName, rel_name, rel.subFrameName))
    frame_rel = list(set(frame_rel))
    return frame_rel

def write_to_file(data, path):
    with open(path,'w') as f:
        for line in data:
            f.writelines(line[0]+'\t'+line[1]+'\t'+line[2]+'\n')

def mk_senti_graph(senti_frames, frame_relations):
    
    senti_graph = nx.Graph()
    for senti_frame in senti_frames:
        senti_graph.add_node(senti_frame)
    for frame_relation in frame_relations:
        sup = frame_relation[0]
        sub = frame_relation[2]
        rel = frame_relation[1]
        if (sup,sub) in senti_graph.edges():
            senti_graph[sup][sub]['relation'].append(rel)
        else:
            senti_graph.add_edge(sup,sub, relation=[rel])
    print(senti_graph.number_of_nodes())
    print(senti_graph.nodes())
    print('-'*20)
    print(senti_graph.number_of_edges())
    print(senti_graph.edges())
    print('-'*20)
    print(list(nx.connected_components(senti_graph)))

if __name__ == '__main__':
    
    with open(INPUT,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    frame_relations = get_frame_relations(senti_frames)
    fes_relations = get_fes_relations(senti_frames)
    mk_senti_graph(senti_frames, frame_relations)
    """
    for frame in senti_frames:
        print(frame)
        print('='*5+'\n')
        print(fn.frame(frame).definition)
        print('='*5+'\n')
        print(fn.frame(frame).FE)
        print('-'*50+'\n')
    """
    





"""
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
"""