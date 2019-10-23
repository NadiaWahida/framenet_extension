#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:46:13 2019

@author: nadia
"""

from nltk.corpus import sentiwordnet as swn
import json

INPUT = '../../FrameNet/Analyse/Data/jugement_type_lus_and_sr.json'
OUTPUT = '../data/judgement_dict.json'

def open_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def dump_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def add_senti_score(lu_dict):
    judgment_dict = {}
    for sem_type in lu_dict:
        judgment_dict[sem_type] = []
        for lu in lu_dict[sem_type]:
            lu_name = lu['lu_name'].split('.')
            if lu_name[1] not in ['a','v','n','r']:
                continue
            scores = []
            for synset in swn.senti_synsets(lu_name[0],lu_name[1]):
                scores.append((synset.pos_score(),synset.neg_score()))
            lu['senti_score'] = scores
            judgment_dict[sem_type].append(lu)
    return judgment_dict

if __name__ == '__main__':
    lu_dict = open_json(INPUT)
    judgement_dict = add_senti_score(lu_dict)
    dump_json(OUTPUT, judgement_dict)
