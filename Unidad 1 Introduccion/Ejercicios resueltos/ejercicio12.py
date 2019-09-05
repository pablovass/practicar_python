#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:52:27 2019

@author: fernandopuricelli
"""

"""
S=n(n+1)/2
"""

""" definir la función """
def numeroTriangular(n):
    return(n*(n+1)/2)


""" usar la función para varios números """

for i in range(10):
    print(i+1,'\t',numeroTriangular(i+1))