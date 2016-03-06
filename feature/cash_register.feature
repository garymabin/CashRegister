@wip @cash_register
Feature: Cash Register feature
    Background: a list of commodities exist
        Given the followig comodities exist
            | Commodity  | Price |
            | Cococola   | 3.00  | 
            | Badminton  | 1.00  |
            | Apple      | 5.50  |
            
    Scenario: As a Cashier, when all commodities are with no discount, I would like to provide proper price and discount.
        Given I receive <Amount> <Commodity> with <Discount>
            | Commodity | Amount | Discount |
            | Cococola  | 3      | none     |
            | Badminton | 5      | none     |
            | Apple     | 2      | none     |
        And I bring them to the Cash Register
        Then I should charge the customer with price <Total> and <Discount> discount 
            | Total | Discount |
            | 25    | 0        |
            
    Scenario: As a Cashier, when part of the commodities are with "three for two" discount, I would like to provide proper price and discount.
        Given I receive <Amount> <Commodity> with <Discount>
            | Commodity | Amount | Discount      |
            | Cococola  | 3      | three for two |
            | Badminton | 5      | three for two |
            | Apple     | 2      | None          |
        And I bring them to the Cash Register
        Then I should charge the customer with price <Total> and <Discount> discount 
            | Total | Discount |
            | 21    | 4        |
            
    Scenario: As a Cashier, when part of the commodities are with "95%" discount, I would like to provide proper price and discount.
        Given I receive <Amount> <Commodity> with <Discount>
            | Commodity | Amount | Discount |
            | Cococola  | 3      | None     |
            | Badminton | 5      | None     |
            | Apple     | 2      | 95%      |
        And I bring them to the Cash Register
        Then I should charge the customer with price <Total> and <Discount> discount 
            | Total | Discount |
            | 24.45 | 0.55     |
            
    Scenario: As a Cashier, when part of the commodities are with "95%" discount, part of them are with "three for two",
              I would like to provide proper price and discount.
        Given I receive <Amount> <Commodity> with <Discount>
            | Commodity | Amount | Discount      |
            | Cococola  | 3      | three for two |
            | Badminton | 6      | three for two |
            | Apple     | 2      | 95%           |
        And I bring them to the Cash Register
        Then I should charge the customer with price <Total> and <Discount> discount 
            | Total | Discount |
            | 20.45 | 5.55     |            
