Feature: Board trello

  @acceptance
  Scenario: update a list
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a board with name TestBoard
    And I add list with TestList name
    And I update the list created to TestBoardUpdated