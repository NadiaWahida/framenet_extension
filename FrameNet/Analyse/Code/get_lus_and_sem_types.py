#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:02:47 2019

@author: Nadia Arslan
"""
from nltk.corpus import framenet as fn
import json

INPUT = '../Data/example_words.txt'
OUTPUT = '../Data/lus_of_example_words.json'
SEMTYPES = '../Data/sem_types_of_example_words.txt'

def open_file(filename):
    with open(filename,'r') as f:
        words = [el.strip() for el in f.readlines()]
    return words

def get_lus(word):
    """
    given a word 
    returns a list of it's Lexical Units in FrameNet
    """
    lus = fn.lu_ids_and_names(word)
    return lus

def get_lu_info(lu_id):
    """
    given a Lexical Unit ID
    returns a dictionary with information about frame and Semantic Type
    """
    info_dict = {}
    info_dict['lu'] = fn.lu(lu_id).name
    info_dict['lu_id'] = lu_id
    info_dict['frame'] = fn.lu(lu_id).frame.name
    info_dict['frame_id'] = fn.lu(lu_id).frame.ID
    semTypes = [semType.name for semType in fn.lu(lu_id).semTypes]
    info_dict['sem_types'] = semTypes
    return info_dict

def iterate_over(words):
    lus_list = []
    for word in words:
        lus = get_lus(word)
        for lu_id in lus.keys():
            info = get_lu_info(lu_id)
            lus_list.append(info)
    return lus_list

def get_sem_types_dict(lus_list):
    """
    given a list of Lexical Units
    returns a dictionary of Semantic Types and number of occurrence
    """
    sem_types_dict = {}
    for lu in lus_list:
        if len(lu['sem_types']) == 0:
            continue
        for semType in lu['sem_types']:
            if semType not in sem_types_dict.keys():
                sem_types_dict[semType] = 1
            else:
                sem_types_dict[semType] += 1
    return sem_types_dict

def dump(data, filename):
    with open(filename, 'w') as f:
        for line in data:
            json.dump(line, f)
            f.writelines('\n')
            
def print_dict(d, filename):
    with open(filename, 'w') as f:
        for key in d:
            f.writelines(key+'\t'+str(d[key])+'\n')
        
            
if __name__=='__main__':
    
    words = open_file(INPUT)
    lus_list = iterate_over(words)
    dump(lus_list, OUTPUT)
    sem_types_dict = get_sem_types_dict(lus_list)
    print_dict(sem_types_dict, SEMTYPES)
    #print(sem_types_dict)
    