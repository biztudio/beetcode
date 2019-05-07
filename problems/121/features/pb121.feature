Feature: Best Time to Buy and Sell Stock
       
    Scenario: 7,1,5,3,6,4
        Given Input 7,1,5,3,6,4
        When Calculate
        Then Get Result 5    

    Scenario: 7,6,4,3,1
        Given Input 7,6,4,3,1
        When Calculate
        Then Get Result 0  
 