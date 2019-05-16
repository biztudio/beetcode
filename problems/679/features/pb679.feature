Feature: You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24. 

    Scenario: [1,3,4,6] => true: 6 / (1 - 3/4) = 24
        Given Input 1,3,4,6
        When Calculate
        Then Get Result True


    Scenario: [1, 4, 7, 8] => true: (8-4) * (7-1) = 24
        Given Input 1, 4, 7, 8
        When Calculate
        Then Get Result True


    Scenario: [1, 5, 7, 9] => true: (9-5) * (7-1) = 24
        Given Input 1, 5, 7, 9
        When Calculate
        Then Get Result True


    Scenario: [1, 4, 5, 9] => true: (4-1) * 5 + 9 = 24
        Given Input 1, 4, 5, 9
        When Calculate
        Then Get Result True


    Scenario: [1, 2, 1, 2] => false
        Given Input 1, 2, 1, 2
        When Calculate
        Then Get Result False


    Scenario: [1,2,3,4] => true: 1*2*3*4 = 24
        Given Input 1,2,3,4
        When Calculate
        Then Get Result True


    Scenario: [1,9,1,2] => true: (9-1) * (1+2) = 24
        Given Input 1,9,1,2
        When Calculate
        Then Get Result True


    Scenario: [3,3,8,8] => true: 8/(3-(8/3)) = 24
        Given Input 3,3,8,8
        When Calculate
        Then Get Result True


    Scenario: [3,8] => true: 3 * 8 = 24
        Given Input 3,8
        When Calculate
        Then Get Result True


    Scenario: [1,2,3,4,4] => true: (4+4)*3*(2-1) = 24
        Given Input 1,2,3,4,4
        When Calculate
        Then Get Result True

    Scenario: [24] => true 
        Given Input 24
        When Calculate
        Then Get Result True
    
    Scenario: [14] => false 
        Given Input 14
        When Calculate
        Then Get Result False     