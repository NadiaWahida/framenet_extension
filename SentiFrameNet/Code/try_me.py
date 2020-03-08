#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:15:07 2020

@author: nadia
"""
import json
import SentiWordNet
import map_constraints_to_annotation as c2a
import random
from nltk.corpus import framenet as fn
from nltk.corpus import sentiwordnet as swn

CONSTRAINTS = '../Data/Constraints/Frameconstraints.json'
ANNOTATIONS = '../Data/annotated_sents_from_FrameNet.txt'
SF_WITH_P = '../Data/Senti_Frames_mit_Framepolarity.txt'
SF_WITHOUT_P = '../Data/Senti_Frames_ohne_Framepolarity.txt'
FE_SOURCE = '../Data/source_elements.txt'
FE_TARGET = '../Data/target_elements.txt'
HELP = '../Data/print_help.txt'

def print_annotation_opinions(word, n=3):
    correct = True
    if '.' in word:
        try:
            annotations = annotations_by_lu[word]
        except:
            correct = False
            #print('Invalid Input')
    else:
        try:
            annotations = annotations_by_frame[word]
        except:
            correct = False
            #print('Invalid Input')
    if correct==False:
        print('\n ------------------------------INVALID INPUT------------------------------\n')
        ask_for_word()
    else:
        if len(annotations) < n:
            print('\n Only ', len(annotations), ' annotation(s) for ', word, ' were found: \n')
        else:
            annotations = random.choices(annotations, k=n)
            
        for annotation in annotations:
            mapping = c2a.map_constraints_to_annotation(annotation, constraints)
            (solutions, solutions_with_vars) = mapping
            for el in annotation.items():
                print(el[0]+':  '+str(el[1]))
            print('='*100)
            for el in solutions:    
                print(el[0])
                print(el[1])
                print('-'*100)
            for el in solutions_with_vars:    
                print(el[0])
                print(el[1])
                print('-'*100)
            print('#'*100)
    ask_for_instruction()
            
def welcome():
    print('\n Hi!\n')
    print('Type "help" for help \n')

def print_help():
    with open(HELP,'r') as f:
        for line in f.readlines():
            print(line)
    ask_for_instruction()
    
def ask_for_word(instruction=''):
    if instruction=='':
        word = input('Please enter a word: ')
    else:
        word = instruction
    n = int(input('How many examples you like to see? '))
    if type(n) == int:
        print_annotation_opinions(word, n)
    else:
        print_annotation_opinions(word)

def get_info(instruction):
    if instruction.lower() == '#sentiframes' or instruction.lower() == '#sf' or instruction.lower() == '#frames':
        name = ' all SentiFrames in my Database: '
        printer = sorted(list(annotations_by_frame.keys()))
    elif instruction.lower() == '#sentiframes_with_polarity' or instruction.lower() == '#sf_with':
        with open(SF_WITH_P,'r') as f:
            printer = sorted([line.strip() for line in f.readlines()])
        name = ' all SentiFrames with Polarity in my Database: '
    elif instruction.lower() == '#sentiframes_without_polarity' or instruction.lower() == '#sf_without':
        with open(SF_WITHOUT_P,'r') as f:
            printer = sorted([line.strip() for line in f.readlines()])
        name = ' all SentiFrames without Polarity in my Database: '
    elif instruction.lower() == '#source_elements':
        with open(FE_SOURCE,'r') as f:
            printer = sorted([line.strip() for line in f.readlines()])
        name = ' all Frame Elements that can function as a Source of an Opinion: '
    elif instruction.lower() == '#target_elements':
        with open(FE_TARGET,'r') as f:
            printer = sorted([line.strip() for line in f.readlines()])
        name = ' all Frame Elements that can function as a Target of an Opinion: '
    elif instruction.lower() == '#lus':
        printer = sorted(list(annotations_by_lu.keys()))
        name = ' all Senti Lexical Units in my Database: '
        
    else:
        print('Sorry I did not understand your instruction \n')
        ask_for_instruction()
        
    print('\n Here is a list of'+name)
    print('='*len('\n Here is a list of'+name))
    print(printer)
    ask_for_instruction()

def get_senti_score(instruction):
    
    try:
        if len(instruction.split('.'))==2:
            sentiment = SentiWordNet.get_sentiment(instruction.split('.')[0],instruction.split('.')[1])
            synsets = swn.senti_synsets(instruction.split('.')[0],instruction.split('.')[1])
        else:
            sentiment = SentiWordNet.get_sentiment(instruction)
            synsets = swn.senti_synsets(instruction)
        print('\n','-'*50,'\n')
        print('\nSentiment of the added score evaluation: ', sentiment)
        print('Synsets from SentiWordNet: \n')
        for el in synsets: print(el)
        print('\n','-'*50,'\n')
        ask_for_instruction()
    except:
        print('\n Sorry, word not in Database of SentiWordNet\n')
        ask_for_instruction()

def look_up_fn(instruction):
    try:
        print('\n','-'*100,'\n')
        print('Frame information from FrameNet is: ')
        print('\n','-'*100,'\n')
        print(fn.frame(instruction))
        print('\n','-'*100,'\n')
    except:
        print('\n Sorry, Frame not in Database of FrameNet\n')
    ask_for_instruction()
           
      
def ask_for_instruction():
    instruction = input('What would you like to know? ')
    if instruction in annotations_by_frame.keys() or instruction in annotations_by_lu.keys():
        ask_for_word(instruction)
    elif instruction == 'help':
        print_help()
    elif instruction.startswith('#'):
        get_info(instruction)
    elif instruction == 'exit':
        print('\n Goodbye :) ')
    elif instruction.startswith('-swn '):
        get_senti_score(instruction.replace('-swn ',''))
    elif instruction.startswith('-fn'):
        look_up_fn(instruction.replace('-fn ',''))
    else:
        print('Sorry I did not understand. ')
        ask_for_instruction()
    
if __name__ == '__main__':
    #print('\n Loading Frames into Memory...')
    with open(CONSTRAINTS,'r') as f:
        constraints = json.load(f)
    with open(ANNOTATIONS,'r') as f:
        annotations = [eval(line.strip()) for line in f.readlines()]
    
    annotations_by_frame = {}
    annotations_by_lu = {}
    for a in annotations:
        #print(a['frame'])
        if a['frame'] not in annotations_by_frame.keys():
            annotations_by_frame[a['frame']] = [a]
        else:
            annotations_by_frame[a['frame']].append(a)
        if a['lu'] not in annotations_by_lu.keys():
            annotations_by_lu[a['lu']] = [a]
        else:
            annotations_by_lu[a['lu']].append(a)
    welcome()
    ask_for_instruction()
    #ask_for_word()
    #print_annotation_opinions('brag.v')
    