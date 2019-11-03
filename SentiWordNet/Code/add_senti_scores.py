#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:46:13 2019

@author: nadia
"""

from nltk.corpus import sentiwordnet as swn
import json

#INPUT = '../../FrameNet/Analyse/Data/jugement_type_lus_and_sr.json'
#OUTPUT = '../data/judgement_dict.json'

INPUT = '../../FrameNet/Analyse/Data/lus_by_semtypes_plus_FEs.json'
OUTPUT = '../Data/lus_with_senti_score.json'

def open_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def dump_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def add_senti_score(lu_dict):
    senti_dict = {}
    for sem_type in lu_dict:
        senti_dict[sem_type] = []
        for lu in lu_dict[sem_type]:
            lu_name = lu['lu'].split('.')
            print('#'*10)
            print(lu_name)
            print('-'*10)
            if lu_name[1] not in ['a','v','n','r']:
                continue
            scores = []
            for synset in swn.senti_synsets(lu_name[0],lu_name[1]):
                scores.append((synset.pos_score(),synset.neg_score()))
            if len(scores) == 0:
                lu['senti_score'] = None
                senti_dict[sem_type].append(lu)
            else:
                pos, neg = 0, 0
                for score in scores:
                    pos += score[0]
                    neg += score[1]
                pos = round((pos / len(scores)),4)
                neg = round(neg / len(scores),4)
                print(lu_name,lu['lu_id'], pos, neg)
                lu['senti_score'] = [pos,neg]
                senti_dict[sem_type].append(lu)
    return senti_dict

if __name__ == '__main__':
    lu_dict = open_json(INPUT)
    senti_dict = add_senti_score(lu_dict)
    dump_json(OUTPUT, senti_dict)
