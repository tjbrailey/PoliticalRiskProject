# Geopolitical Risk Interactive Database Test Functions



# Note: Many of the functions for the GRID include test functions 
# which return errors if the user inputs incorrect information. 
# Below are some additional test functions for the purpose of the
# COGS 18 project guidelines. 



# Some modules are required for the test script to run.
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tbrailey_final_project_functions import *



def test_dict_key(dict_key):
    '''Tests for dict_key type'''
    
    if not isinstance(dict_key, str):
        raise TypeError('dict_key should be a string.')

        
        
def test_prs_code_book_search():
    '''Tests for the prs_code_book function and the prs_code_book'''
    
    assert type(prs_code_book_search()) == str
    
    assert type(prs_code_book) == dict
    
    

def test_country_info():
    '''Tests for the country_info function'''
    
    assert type(country_info(my_country)) == pandas.core.frame.DataFrame

    
    
def test_year_info():
    '''Tests for the year_info function'''
    
    assert type(year_info(my_year, country_sub = country_info(my_country))) == pandas.core.frame.DataFrame