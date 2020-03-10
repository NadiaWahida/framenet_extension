#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:11:35 2020

@author: nadia
"""
import json
import re
import SentiWordNet

CONSTRAINTS = '../Data/Constraints/Frameconstraints.json'
ANNOTATIONS = '../Data/annotated_sents_from_FrameNet.txt'
OUTPUT = '../Data/Opinion_mapping/'

fe_pattern = re.compile('([a-zA-Z_]+)\.([a-zA-Z_]+)')

def map_constraints_to_annotation(annotation, constraints):
    """
    This function takes an annotated sentence from FrameNet 
    and a dict with all SentiConstraints
    returns all possible Opinion-Mappings for that annotation
    in a tuple: ([solutions_with_bounded_frameelements],[solutions_with_unbounded_variable])

    Parameters
    ----------
    annotation : dict
        {'lu':lu, 'frame':frame, 'text':text, 'Target':target, 'FE':fes}.
    constraints : dict
        dictionary of SentiConstraints.

    Returns
    -------
    solutions : list of tuples (general_constraint, specific_constraint)
        solutions_with_bounded_frameelements.
    solutions_with_vars : list of tuples (general_constraint, specific_constraint)
        solutions_with_unbounded_variable.

    """
    #annotation = {'lu':lu, 'frame':frame, 'text':text, 'Target':target, 'FE':fes, 'FE_unexpr': unexpr}
    constraints = constraints[annotation['frame']]
    suitable = []
    for fe in annotation['FE']:
        for constraint in constraints:
            if fe in constraint:
                suitable.append(constraint)
            elif '?_x' in constraint:
               suitable.insert(0,constraint) 
    suitable = list(set(suitable))
    solutions = []
    solutions_with_vars = []
    for constraint in suitable:
        original = constraint
        if '?_lu' in constraint:
            constraint = constraint.replace('?_lu', annotation['lu'])
        elif constraint.count('.') == 1:   
            try:
                constraint = constraint.replace(re.search(fe_pattern,constraint).group(), annotation['FE'][re.search(fe_pattern,constraint).group(2)])
                constraint = constraint.replace('?_s','_SOMEONE')
                constraint = constraint.replace('?_t','_SOMETHING')
            except:
                continue
        elif constraint.count('.') == 2:
            try:
                constraint = constraint.replace(re.search(fe_pattern,constraint).group(), annotation['FE'][re.search(fe_pattern,constraint).group(2)])
            except:
                continue
            try:
                constraint = constraint.replace(re.search(fe_pattern,constraint).group(), annotation['FE'][re.search(fe_pattern,constraint).group(2)])
            except: continue
            #print(constraint)
        
        if '?_x' in constraint:
            constraint = constraint.replace('?_x','_GENERAL')
        if '?_p' in constraint:
            p = SentiWordNet.get_sentiment(annotation['lu'].split('.')[0], annotation['lu'].split('.')[1])
            if p=='no_entry':
                continue
            if p=='neut':
                continue
            constraint = constraint.replace('?_p', p)
        constraint = constraint.replace('neg','    -- negative ->   ')
        constraint = constraint.replace('pos','    -- positive ->    ')
        if '_SOME' in constraint:# or '_GEN' in constraint
            solutions_with_vars.append((original,constraint))
        else:
            if '_GEN' in constraint:
                solutions.insert(0,(original,constraint))
            else:
                solutions.append((original,constraint))
    if len(solutions)!= 0 or len(solutions_with_vars)!=0:
        return (solutions, solutions_with_vars)
    else: return ()

def write_to_file(annotation, solutions, solutions_with_vars):
    """
    Pretty Prints annotation and solved opinion mapping
    """
    with open(OUTPUT+annotation['frame']+'.txt','a') as f:
        f.writelines('#'*120+'\n\n')
        for el in annotation.items():
            f.writelines(el[0]+':    '+str(el[1])+'\n')
        f.writelines('\n'+'='*100+'\n\n')
        for el in solutions:
            f.writelines(el[0]+'\n'+el[1]+'\n\n')
            f.writelines('-'*100+'\n\n')
        for el in solutions_with_vars:
            f.writelines(el[0]+'\n'+el[1]+'\n\n')
            f.writelines('-'*100+'\n\n')
            

if __name__ == '__main__':
    with open(CONSTRAINTS,'r') as f:
        constraints = json.load(f)
    with open(ANNOTATIONS,'r') as f:
        annotations = [eval(line.strip()) for line in f.readlines()]
    #annotation = annotations[0]
    for i, annotation in enumerate(annotations):
        if i%1000==0:
            print(i,' of ',len(annotations),' processed')
            #break
        if annotation['frame'] not in constraints.keys():
            print(annotation['frame'])
            continue
        else:
            mapping = map_constraints_to_annotation(annotation, constraints)
            if len(mapping)!=0:
                (solutions, solutions_with_vars) = mapping
                print(solutions)
                write_to_file(annotation, solutions, solutions_with_vars)