Feature: Get pet from PetStore

  Background:
    * call read("../post/pet-post.feature")
    * url "https://petstore.swagger.io/v2/pet"

  Scenario: Get pet by ID
    Given path petId
    When method get
    Then status 200
    And match response contains { id: '#(petId)', name: "#(petName)", status: '#(petStatus)' }
    And def petId = $.id
    And def petName = $.name
    And def petStatus = $.status