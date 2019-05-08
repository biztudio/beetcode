Feature: Best Time to Buy and Sell Stock
       
    Scenario: 7,1,5,3,6,4
        Given Input 7,1,5,3,6,4
        When Calculate
        Then Get Result 5    

    Scenario: 7,6,4,3,1
        Given Input 7,6,4,3,1
        When Calculate
        Then Get Result 0  

    Scenario: 2,4,1
        Given Input 2,4,1
        When Calculate
        Then Get Result 2    

    Scenario: 2,1,2,1,0,1,2
        Given Input 2,1,2,1,0,1,2
        When Calculate
        Then Get Result 2      
 