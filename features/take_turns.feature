@wip
Feature: take_turns
    In order to rotate team members in a mob
    As a driver
    I want to be notified, when my turn is over

    Scenario: driver is notified when turn ends
        Given driver starts turn
        When turn ends
        Then a notification shows "rotate"
