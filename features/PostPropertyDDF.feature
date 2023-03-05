Feature: Agent
    Background:
        Given MagicBricks website should open
        And User clicks POST PROPERTY Button


    Scenario: Verify user is able to select options in post property page as Agent
        When User is redirected to the Post Property page
        And User clicks Agent button
        And User clicks Rent/Lease button
        And User enter <mobilenumber> with first valid data
        Then User clicks Start now button
        And User is redirected to Sell and Rent your property

    Scenario: Verify user is able to select options in Post property page as Agent
        When User is redirected to the Post Property page
        And User clicks Agent button
        And User clicks Rent/Lease button
        And User enter <mobilenumber> with second valid data
        Then User clicks Start now button
        And User is redirected to Sell and Rent your property