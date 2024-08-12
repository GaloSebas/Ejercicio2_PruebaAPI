Feature: Update pet from PetStore

  Background:
    * call read("../get/pet-get-by-id.feature")
    * url "https://petstore.swagger.io/v2"
    * path "/pet"
    * def petNameEdited = "FattyGarfield"
    * def statusEdited = "sold"
    * def var =
    """
    {
      "id": "#(petId)",
      "category": { "id": 0, "name": "string" },
      "name": "#(petNameEdited)",
      "photoUrls": ["string"],
      "tags": [{ "id": 0,"name": "string" }],
      "status": "#(statusEdited)"
    }
    """

  Scenario: Update pet
    Given request var
    When method put
    Then status 200
    And match response contains { id: '#(petId)', name: "#(petNameEdited)", status: '#(statusEdited)' }
    And def petId = $.id
    And def petNameUpdated = $.name
    And def petStatusUpdated = $.status