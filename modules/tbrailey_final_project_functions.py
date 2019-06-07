# Geopolitical Risk Interactive Database Functions



# Some modules are required for the script to run.
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Allows to import and manipulate data between the .py and .ipynb files.
os.chdir('../')
prs = pd.read_csv('prs.csv')

# If country names are standardized, it is easier for users to subset. 
prs['Country'].replace('Bahamas, The', 'Bahamas', inplace = True)
prs['Country'].replace('Brunei Darussalam', 'Brunei', inplace = True)
prs['Country'].replace('Congo, Rep.', 'Republic of the Congo', inplace = True)
prs['Country'].replace('Congo, Dem. Rep.', 'Democratic Republic of the Congo', inplace = True)
prs['Country'].replace('Egypt, Arab Rep.', 'Egypt', inplace = True)
prs['Country'].replace('Gambia, The', 'Gambia', inplace = True)
prs['Country'].replace('Hong Kong SAR, China', 'Hong Kong', inplace = True)
prs['Country'].replace('Iran, Islamic Rep.', 'Iran', inplace = True)
prs['Country'].replace('Korea, Dem. Rep.', 'North Korea', inplace = True)
prs['Country'].replace('Korea, Rep.', 'South Korea', inplace = True)
prs['Country'].replace('Russian Federation', 'Russia', inplace = True)
prs['Country'].replace('Taiwan, China', 'Taiwan', inplace = True)
prs['Country'].replace('Syrian Arab Republic', 'Syria', inplace = True)
prs['Country'].replace('Venezuela, RB', 'Venezuela', inplace = True)
prs['Country'].replace('Yemen, Rep.', 'Yemen', inplace = True)

os.chdir('modules')



# Code book to be called by prs_code_book_search()
prs_code_book = {'Country' : 'The name of each recognized country in the PRS dataset',
                'Code' : 'The country code for each recognized country in the PRS dataset',
                'PRSxxVA' : 'Voice and Accountability: Military in politics and democratic' + 
                 'accountability',
                'PRSxxPV' : 'Political Stability and Absence of Violence: Government' + 
                 'stability, internal conflict, external conflict, and ethnic tensions',
                'PRSxxGE' : 'Government Effectiveness: Bureaucratic quality',
                'PRSxxRQ' : 'Regulatory Quality: Investment profile', 
                'PRSxxRL' : 'Rule of Law: Law and order',
                'PRSxxCC' : 'Control of Corruption: Corruption'}



class MyColors:
    '''Allows to print strings with different aesthetics.
    Source: https://stackoverflow.com/questions/8924173/
            how-do-i-print-bold-text-in-python
            
    Parameters
    ----------
    Example: print color.bold + 'string' + color.reset
    
    Returns
    -------
    A visually altered string. 
    '''
    
    bold = '\033[1m'
    underline = '\033[4m'
    
    purple = '\033[95m'
    cyan = '\033[96m'
    dark_cyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    
    reset = '\033[0m'



def prs_code_book_search():
    '''Returns the value of a given key. 
    
    Parameters
    ----------
    No given inputs for the function itself. 
    Within the function, input() requires a key.
    input() turns given key into a string. 
    
    Returns
    -------
    Value of given key which is a string.  
    '''
    
    dict_key = input('What political risk metric would ' +
                     'you like to learn about? ')
    
    if dict_key in prs_code_book:
        print('Here is more information on ' + dict_key + ':')
    else:
        print('It doesn\'t look like that metric is in the dataset.') 
    
    print(MyColors.bold + MyColors.underline + prs_code_book[dict_key] + 
         MyColors.reset)
    
    return dict_key



def country_present(prs=prs):
    '''Returns a tuple of country names in the prs.csv dataset. 
    
    Parameters
    ----------
    No inputs required. Simply run the function. 
    
    Returns
    -------
    A tuple pulled from a DataFrame.  
    '''
    
    subset = prs[['Country']]
    tuples = [tuple(x) for x in subset.values]
    return tuples



def country_info(my_country, prs = prs):
    '''Returns the subset of a dataset based on a given row value. 
    
    Parameters
    ----------
    my_country : str. 
    prs : DataFrame.
    
    Returns
    -------
    country_sub : DataFrame.
        A subset of the original DataFrame.
    '''
    
    if any(prs.Country == my_country) == True:
        print('Thank you. Below is a table summarizing political risk ' +
              'scores for ' + my_country + '.')
    else:
        print('That country is not in the dataset. ' +
              'Check your spelling or refer to the country list.')
    
    country_sub = pd.DataFrame(prs.loc[prs['Country'] == my_country])
    
    return country_sub



yesses = ['yes', 'Yes', 'YES', 
          'yeah', 'Yeah', 'YEAH', 
          'please', 'Please', 'PLEASE']



def country_graph(my_country, country_sub):
    '''Returns a graph of a previously specified DataFrame subset. 
    
    Parameters
    ----------
    my_country : str. 
    country_sub : DataFrame.
    
    Returns
    -------
    Graph of subsetted DataFrame.
    '''
    
    country_graph = input('Would you like to graph your subset? ')
    
    if country_graph in yesses:
        dat = country_sub.transpose()
        dat = dat.drop(['Country', 'Code'])
        dat.plot(figsize = (15, 5), grid = True, legend = None)
        plt.title('Political Risk Rankings for ' + 
                  my_country + ' across time.')
    else:
        print('Please move on to the next section.')



def year_info(my_year, country_sub):
    '''Returns the subset of a dataset based on a given column value. 
    
    Parameters
    ----------
    my_year : str.
    country_sub : DataFrame.
    
    Returns
    -------
    year_sub : DataFrame.
        A subset of the original DataFrame.
    '''
    
    year_range = list(range(1996, 2018))
    year_range
    
    if int(my_year) in year_range:
        print('Here is information for ' + my_year)
    else:
        print('That number is not within the dataset"s range. ' + 
              'Please try a different year.')
    
    my_year_str = str(my_year)
    my_year_find = my_year_str[2:5]
    year_sub = country_sub.filter(like=my_year_find)
    
    return year_sub



def year_graph(my_year, my_country):
    '''Returns a graph of previously specified DataFrame subset. 
    
    Parameters
    ----------
    year_graph: str. 
    my_year : str.
    my_country : DataFrame.
    
    Returns
    -------
    Graph of subsetted DataFrame.  
    '''
    
    year_graph = input('Would you like to graph your subset? ')
    if year_graph in yesses:
        row = year_info(my_year, country_sub = country_info(my_country)).iloc[0]
        row.plot(kind = 'bar')
        plt.title('Political Risk Rankings for ' + my_country + ' in ' + my_year)
    else:
        print('Please return to either the country or year sections.')