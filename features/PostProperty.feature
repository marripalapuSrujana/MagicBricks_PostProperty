Feature: Post Property
  Background:
    Given MagicBricks website should open
    And User clicks POST PROPERTY Button


  Scenario: Verify user navigates to post property page
    Then User is redirected to the Post Property page



  Scenario: Verify user is able to select options in post property page as Owner
    When User is redirected to the Post Property page
    And User clicks Owner button
    And User clicks Sell button
    And User enters valid mobile number
    Then User clicks Start now button
    And User is redirected to Sell and Rent your property



  Scenario: Verify user is able to select options in post property page as Builder
    When User is redirected to the Post Property page
    And User clicks Builder button
    And User clicks List as PG button
    And User enters valid mobile number
    Then User clicks Start now button
    And User is redirected to Paying Guest page



  Scenario Outline: Verify user is able to select options in post property page as Owner with invalid number
    When User is redirected to the Post Property page
    And User clicks Owner button
    And User clicks Sell button
    And User enters invalid <number>
    Then User clicks Start now button
    And Website Displays error

    Examples:
    |number|
    |78939951|
    |94946789003|





















