#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:52:04 2020

@author: Nadia Arslan

This module was written to find SentiFrames in FrameNet 
It uses FrameNet's Frame Relations to expand the List of SentiFrames
This module also models a SentiGraph of the SentiFrames
It was writen for research and therefore edited a few times
"""
from nltk.corpus import framenet as fn
import networkx as nx
INPUT = '../Data/Senti_Frames.txt'
OUTPUT = '../Data/Senti_Frame_Neighbour.txt'

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
    """
    This function uses the module networkx to model a graph of SentiFrames
    and prints it's nodes, edges and connected components

    Parameters
    ----------
    senti_frames : list
        List of SentiFrames.
    frame_relations : list of tripples
        [(SuperFrame, Relation, SubFrame),...]

    Returns
    -------
    None.

    """  
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
    print('Number of nodes: ', senti_graph.number_of_nodes())
    print(senti_graph.nodes())
    print('-'*20)
    print('Number of edges: ', senti_graph.number_of_edges())
    print(senti_graph.edges())
    print('-'*20)
    print('Connected Graph Components: \n')
    for g in list(nx.connected_components(senti_graph)):
        print(g,'\n')

if __name__ == '__main__':
    
    with open(INPUT,'r') as f:
        senti_frames = [line.strip() for line in f.readlines()]
    frame_relations = get_frame_relations(senti_frames)
    fes_relations = get_fes_relations(senti_frames)
    mk_senti_graph(senti_frames, frame_relations)