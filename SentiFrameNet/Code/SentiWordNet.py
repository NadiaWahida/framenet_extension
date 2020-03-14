#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:22:22 2020

@author: Nadia Arslan

This function looks up a word (and optional it's POS-Tag) in SentiWordNet
and returns the sentiment with the highest score
"""

from nltk.corpus import sentiwordnet as swn
        
def get_sentiment(word, POS='no'):
    """
    This function looks up a word (and optional it's POS-Tag) in SentiWordNet,
    adds up positive and negative Scores of the found synsets
    returns the sentiment with the highest score
    returns neutral if both scores are equal
    returns no_entry if no entry was found

    Parameters
    ----------
    word : str
        Word to be looked up in SentiWordNet.
    POS : str
        POS-Tag of the word.

    Returns
    -------
    str : pos, neg or neut

    """
    try:
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
        if pos>neg:
            return 'pos'
        elif neg>pos:
            return 'neg'
        else:
            return 'neut'
    except:
        return 'no_entry'
