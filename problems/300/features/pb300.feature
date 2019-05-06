Feature: Given an unsorted array of integers, find the length of longest increasing subsequence.
       
    Scenario: 4,10,4,3,8,9
        Given Input 4,10,4,3,8,9
        When Calculate
        Then Get Result 3    

    Scenario: 10,2,5,3,7,101,18
        Given Input 10,2,5,3,7,101,18
        When Calculate
        Then Get Result 4  

    Scenario: 1,2,3
        Given Input 1,2,3
        When Calculate
        Then Get Result 3 

    Scenario: 3,2,1
        Given Input 3,2,1
        When Calculate
        Then Get Result 1 

    Scenario: 10,9,2,5,3,7,101,18
        Given Input 10,9,2,5,3,7,101,18
        When Calculate
        Then Get Result 4          