from requests.exceptions import HTTPError
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import sys
import requests

## Task 1: create a function called print_hello_contributors() that prints "Hello contributors". 
## The function takes nothing as input, and returns None

## Task 2: add a docstring to the following function. See sample_function to help
def perform_query(url):
    # Time query
    start_time = time.time()
    
    # Using GET command 
    response = requests.get(url)
    total_time = time.time() - start_time
    
    # Raise issues if response is different from 200
    response.raise_for_status()
    
    # access JSOn content
    jsonResponse = response.json()
    
    return [jsonResponse,total_time]

def sample_function(integer1: int, integer2: int):
    """
        This function takes as input two integers (integer1 and integer2) and returns 
        integer1 raised to the power of integer2
        
        Parameters:
        -----------
        integer1 (int) a number greater than or equal to zero
        integer2 (int) a number greater than or equal to zero
        
        Returns:
        --------
        iter_sum (int) the result of integer1 raised to the power of integer2 via an iterative sum approach
        total_time (float) total time in seconds it took to complete the computation
    """
    
    # Time operation
    start_time = time.time()
    
    # Initialize sum
    iter_sum = 0
    
    # Iterate over integers in a nested for loop
    for i in range(integer1):
        for j in range(integer2):
            # Perform sum
            iter_sum = iter_sum + i + j
    # Time how long it took
    total_time = time.time() - start_time
            
    return [iter_sum, total_time]


if __name__ == '__main__':
    
    #print_hello_contributors()
    
    int1 = 5
    int2 = 2
    
    # Power method
    # Time operation
    start_time = time.time()
    power_method = int1**int2
    # Time how long it took
    power_time = time.time() - start_time
    
    # Sum method
    
    [iter_sum, sum_time] = sample_function(int1, int2)
    
    print(f'{int1} raised to the power of {int2} is {power_method}. This method took {power_time} seconds')
    print(f'{int1} raised to the power of {int2} is {iter_sum}. This method took {sum_time} seconds')