@smoke
Feature: Smoke trello


  Scenario: Create Board
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a board with name TestBoard
    Then The Board TestBoard should be created

  Scenario: Create a Card
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a board with name TestBoard
    And I add list with TestList name
    And I add to card in the list created with CardTest name
    Then The card CardTest should be created in the list

  Scenario: Create a List
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a board with name TestBoard
    And I add list with TestList name
    Then The TestList list should be created in the board

  Scenario: Get Member info
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a board with name TestBoardMember
    And I get info of Team member
    Then The name should be franz silva with rol (Administrador)

  Scenario: Create a team
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a team with TeamTest name
