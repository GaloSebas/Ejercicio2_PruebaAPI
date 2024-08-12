Feature: Add pet to PetStore

  Background:
    * url "https://petstore.swagger.io/v2"
    * path "/pet"
    * def petInitialName = "Rupert"
    * def petInitialId = 345890
    * def var =
    """
    {
      "id": #(petInitialId),
      "category": { "id": 0, "name": "string" },
      "name": "#(petInitialName)",
      "photoUrls": ["string"],
      "tags": [{ "id": 0,"name": "string" }],
      "status": "available"
    }
    """

  @Create
  Scenario: Add a pet
    Given request var
    When method post
    Then status 200
    And match response contains { id: '#(petInitialId)', name: "#(petInitialName)", status: 'available' }
    And def petId = $.id
    And def petName = $.name
    And def petStatus = $.status