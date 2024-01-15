Feature: Teste de Formulário

  Scenario: Preencher o formulário com dados corretos
    Given the user is on the page form
    When the user fills out the form correctly
    And the user sends form
    Then the user see a message that indicates success in terminal

  Scenario: Preencher o formulário com email inválido
    Given the user is on the page form
    When the user fills out the form with an invalid email address
    And the user sends form
    Then the user see an error message indicating an invalid data "email" in terminal

  Scenario: Preencher o formulário com número de contato inválido
    Given the user is on the page form
    When the user fills out the form with an invalid contact number
    And the user sends form
    Then the user see an error message indicating an invalid data "contact number" in terminal

  Scenario: Preencher um formulário in blank
    Given the user is on the page form
    When the user sends form
    Then the user see an error message indicating an invalid data "blank form" in terminal

  Scenario: Recarregar o formulário
    Given the user is on the page form
    When the user fills out the form correctly
    And the user refreshes the page form
    Then the user see an error message indicating an invalid data "reloaded form" in terminal