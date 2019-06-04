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



def test_dict_key(dict_key = 'PRSxxCC'):
    '''Tests for dict_key type'''
    
    if not isinstance(dict_key, str):
        raise TypeError()
        
        
        
def test_prs_code_book_search():
    '''Tests for the prs_code_book function and the prs_code_book'''
    
    assert type(prs_code_book_search()) is str
    
    assert type(prs_code_book) is dict
    
    assert callable (prs_code_book_search())
       
    

def test_country_info():
    '''Tests for the country_info function'''
    
    assert type(country_info(my_country = 'Albania')) is pd.core.frame.DataFrame
    
    assert callable (country_info(my_country = 'Albania'))


    
def test_year_info():
    '''Tests for the year_info function'''
    
    assert type(year_info(my_year = '2000', country_sub = country_info(my_country = 'Albania'))) is pd.core.frame.DataFrame
    
    assert callable (year_info(my_year = '2000', country_sub = country_info(my_country = 'Albania')))