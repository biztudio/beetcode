Feature: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    Scenario: [3,2,3]
        Given Input 3,2,3
        When Calculate
        Then Get Result 3    

    Scenario: [2,2,1,1,1,2,2]
        Given Input 2,2,1,1,1,2,2
        When Calculate
        Then Get Result 2
