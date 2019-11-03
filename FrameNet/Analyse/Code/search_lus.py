#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 8 16:29 2019

@author: nadia, sanaz
"""
from nltk.corpus import framenet as fn

INPUT = '../Data/beispielwörter.txt'
OUTPUT = 'lexUnits.txt'

def open_file(filename):
    with open(filename,'r') as f:
        words = [el.strip() for el in f.readlines()]
    return words

def write_file(filename, data):
    if data != None:
        with open(filename,'a') as f:
                f.writelines(data)
                f.writelines('\n\n')

def get_frames(lu):
    frames = fn.frames_by_lemma(lu)
    return frames

def get_lus(word):
    lus = fn.lu_ids_and_names(word)
    return lus

def get_lu_info(lu_id, sem_types_dict):
    name = fn.lu(lu_id).name + '\t' + str(lu_id)
    frame = fn.lu(lu_id).frame.name + '\t' + str(fn.lu(lu_id).frame.ID)
    semTypes = fn.lu(lu_id).semTypes
    #semTypes = '\n'.join(semTypes)
    semTypes = str(semTypes)
    info = name + '\n' + frame + '\n' + semTypes
    return info

if __name__=='__main__':
    
    words = open_file(INPUT)

    sem_types_dict = {}
    for word in words:
        print(word)
        lus = get_lus(word)
        for lu_id in lus.keys():
            print(lu_id)
            info = get_lu_info(lu_id, sem_types_dict)
            print(info)
            #write_file(OUTPUT, info)



