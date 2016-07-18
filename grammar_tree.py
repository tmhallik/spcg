#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

def GrammarTree():
  return collections.defaultdict(GrammarTree)


# Initializes the grammar tree and creating the grammar nodes for parsing
grammar = GrammarTree()

# Set up the grammar hierarchy and the dict reference for the template
grammar['PRINT'] = grammar['PRINT']['PARAM']
grammar['PRINT']['PARAM'] = grammar['PRINT']['PARAM']['end']
grammar['PRINT']['PARAM']['end'] = 'PRINT'


grammar['READ'] = grammar['READ']['PARAM']
grammar['READ']['PARAM'] = grammar['READ']['PARAM']['end']
grammar['READ']['PARAM']['end'] = "READ"

