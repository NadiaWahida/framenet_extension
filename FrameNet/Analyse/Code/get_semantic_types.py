#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:39:38 2019

@author: nadia

Code gets all Semantic Types in FrameNet
writes them to a file
"""
from nltk.corpus import framenet as fn

SEMTYPES = '../Data/all_semantic_types.txt'
NUMBERS = '../Data/all_semantic_types_by_occurance.txt'


def get_lus_sem_types(frames):
    sem_types = []
    # iterates over every LU in every frames and extract Semantic Types of LU's
    for frame in frames:
        for lu_id in frame.lexUnit.items():
            for sem_type in lu_id[1].semTypes:
                sem_types.append(sem_type.name)
    sem_type_dict = count_sem_type_occurence(sem_types)
    return sem_type_dict

def count_sem_type_occurence(sem_types): 
    # counts number of occurence of Semantic Types of LU's 
    sem_type_dict = {}
    for sem_type in sem_types:
        if sem_type not in sem_type_dict.keys():
            sem_type_dict[sem_type] = 1
        else:
            sem_type_dict[sem_type] += 1
    return sem_type_dict

def write_to_file(sem_type_dict, filename):
    numbers_of_types = sorted([(v,k) for (k,v) in sem_type_dict.items()])
    # sorts and removes duplicates            
    sem_types = list(sem_type_dict.keys())
    sem_types = sorted(list(set(sem_types)))
    
    # write to file
    with open(filename+'_alphabetic.txt', 'w') as f:
        for sem_type in sem_types:
            f.writelines(sem_type+'\n')
            #print(type)
    with open(filename+'_numbers.txt', 'w') as f:
        for sem_type in numbers_of_types:
            f.writelines(str(sem_type[0])+'\t'+sem_type[1]+'\n')

def get_fes_sem_types(fes):
    sem_types = []
    sem_types_dict = {}
    for fe in fes:
        if fe.semType != None:
            sem_types.append(fe.semType.name)
    sem_type_dict = count_sem_type_occurence(sem_types)
    print(sorted([(v,k) for (k,v) in sem_type_dict.items()]))
    return sem_type_dict

if __name__ == '__main__':
    frames = fn.frames()
    fes = fn.fes()
    lus_sem_type_dict = get_lus_sem_types(frames)
    fes_sem_type_dict = get_fes_sem_types(fes)