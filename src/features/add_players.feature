Feature: Lägga till namn på spelare

  Scenario: Lägga till två spelare
    When spelaren klickar på knappen "Lägg till spelare"
    And spelaren skriver "David" i textfältet
    And spelaren klickar på knappen "Lägg till spelare"
    Then "David" dyker upp på sidan med texten "0:00.0"
    When spelaren skriver "Gerson" i textfältet
    And spelaren klickar på knappen "Lägg till spelare"
    Then "Gerson" dyker upp på sidan med texten "0:00.0"