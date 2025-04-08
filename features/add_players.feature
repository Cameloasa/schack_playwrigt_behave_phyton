Feature: Adding players to the chess game
  As a user of the chess game application
  I want to add two players by entering their names
  So that the application can track their time while they play chess

  Scenario Outline: Adding multiple players and verifying timers
    Given I am on the chess game start page
    When I click the "Lägg till spelare" button
    And I enter "<player_name>" as a new player's name
    Then the timer for "<player_name>" should be visible

    Examples:
      | player_name |
      | Alice       |
      | Bob         |

  Scenario: Starting the game with two players
    Given I have added "Alice" and "Bob" as players
    When the game starts
    Then I should see timers running for both "Alice" and "Bob"