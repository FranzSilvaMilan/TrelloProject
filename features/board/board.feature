Feature: Board trello

  @acceptance
  Scenario: Update a Board
    Given I login with user franzsilvasky91@hotmail.com and password 12345678 in the Trello page
    When I create a board with name TestBoard
    And I update the board created to TestBoardUpdated