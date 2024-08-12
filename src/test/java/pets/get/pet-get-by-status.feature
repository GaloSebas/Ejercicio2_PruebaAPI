Feature: Get pet from PetStore

  Background:
    * call read("../put/pet-put.feature")
    * url "https://petstore.swagger.io/v2"
    * path "/pet/findByStatus"

  Scenario: Get pet by Status = Sold
    Given param status = petStatusUpdated
    When method get
    Then status 200
    And match response contains deep { id: '#(petId)', name: "#(petNameUpdated)", status: '#(petStatusUpdated)' }