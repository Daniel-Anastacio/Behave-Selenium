Feature: Teste de Formulário

  Scenario: Preencher o formulário com dados corretos
    Given que eu estou na página de formulário
    When eu preencho o formulário com dados corretos
    And eu envio o formulário
    Then eu vejo uma mensagem de sucesso no terminal

  Scenario: Preencher o formulário com email inválido
    Given que eu estou na página de formulário
    When eu preencho o formulário com um email inválido
    And eu envio o formulário
    Then eu vejo uma mensagem de erro informando "O envio do formulário não pôde ser efetuado, email inválido" no terminal

  Scenario: Preencher o formulário com número de contato inválido
    Given que eu estou na página de formulário
    When eu preencho o formulário com um número de contato inválido
    And eu envio o formulário
    Then eu vejo uma mensagem de erro informando "O envio do formulário não pôde ser efetuado, número de contato inválido" no terminal

  Scenario: Preencher um formulário em branco
    Given que eu estou na página de formulário
    When eu envio o formulário em branco
    Then eu vejo uma mensagem de erro informando "O envio do formulário não pôde ser efetuado, formulário em branco" no terminal

  Scenario: Recarregar o formulário
    Given que eu estou na página de formulário
    When eu recarrego a página
    Then eu vejo uma mensagem de erro informando "O envio do formulário não pôde ser efetuado, formulário recarregado" no terminal
