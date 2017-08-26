# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:09:33 2017

@author: Administrator
"""
from datasets import dataset
from math import sqrt

def similarity_score(person1,person2):
    #Returns ratio Euclidean distance score of person1 and person2
    
    both_viewed={}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_viewed[item]=1
        
        #condations to check they both have an common rating items
        if len(both_viewed)==0:
            return 0
            
        sum_of_eclidean_distance=[]
        
        for item in dataset[person1]:
            if item in dataset[person2]:
                sum_of_eclidean_distance.append(pow(dataset[person1][item]-dataset[person2][item],2))
                
        sum_of_eclidean_distance=sum(sum_of_eclidean_distance)
        
        return 1/(1+sqrt(sum_of_eclidean_distance))
        
def person_correlation(person1,person2):
    both_rated={}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item]=1
    number_of_ratings=len(both_rated)
    
    if number_of_ratings==0:
        return 0
    
    person1_preferences_sum=sum([dataset[person1][item] for item in both_rated])
    person2_preferences_sum=sum([dataset[person2][item] for item in both_rated])
    
    person1_square_preferences_sum=sum([pow(dataset[person1][item],2)for item in both_rated])
    person2_square_preferences_sum=sum([pow(dataset[person2][item],2)for item in both_rated])
    
    #sum up the product value of both preferences for each item
    
    product_sum_of_both_users=sum([dataset[person1][item]*dataset[person2][item]for item in both_rated])
    
    numerator_value=product_sum_of_users-(person1_preferences_sum*person2_preferences_sum/number_of_ratings)
    
    denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))

    










































































