import unittest
import requests
import os

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = None
LOG_FILE_PATH = "Reports/test_responses.log"

class api_example_petstore(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.headers = {"Content-Type": "application/json"}
        if not os.path.exists("Reports"):
            os.makedirs("Reports")

    '''Frequently Used'''
    def log_response(self, response, test_name):
        with open(LOG_FILE_PATH, "a") as log_file:
            log_file.write(f"\n\n--- {test_name} ---\n")
            log_file.write(f"Status Code: {response.status_code}\n")
            log_file.write(f"Response JSON: {response.json()}\n")

    '''
    Test 1: Add pet to the store
    Test Description: This test is focused on adding a pet to the store.
    '''           
    def test_add_pet(self):
        global PET_ID
        pet_data = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Garfield",
            "photoUrls": ["string"],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.post(f"{BASE_URL}/pet", json=pet_data, headers=self.headers)
        self.log_response(response, "test_add_pet")
        self.assertEqual(response.status_code, 200)
        pet = response.json()
        PET_ID = pet['id']
        self.assertEqual(pet['name'], "Garfield")
        self.assertEqual(pet['status'], "available")
        #Test Ready? NO

    '''
    Test 2: Get Pet by ID
    Test Description: This test is focused on consulting the pet by id search.
    '''
    def test_get_pet_by_id(self):
        response = requests.get(f"{BASE_URL}/pet/{PET_ID}", headers=self.headers)
        self.log_response(response, "test_get_pet_by_id")
        self.assertEqual(response.status_code, 200)
        pet = response.json()
        self.assertEqual(pet['id'], PET_ID)
        self.assertEqual(pet['name'], "Garfield")
        #Test Ready? NO   

    '''
    Test 3: Update Pet Name/Status
    Test Description: This test is focused on updating the pet name and status.
    '''
    def test_update_pet(self):
        update_data = {
            "id": PET_ID,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "FattyGarfield",
            "photoUrls": ["string"],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "sold"
        }
        response = requests.put(f"{BASE_URL}/pet", json=update_data, headers=self.headers)
        self.log_response(response, "test_update_pet")
        self.assertEqual(response.status_code, 200)
        pet = response.json()
        self.assertEqual(pet['name'], "FattyGarfield")
        self.assertEqual(pet['status'], "sold")
        #Test Ready? NO   

    '''
    Test 4: Search pet by status
    Test Description: This test is focused on searching the pet by status.
    '''
    def test_get_pet_by_status(self):
        response = requests.get(f"{BASE_URL}/pet/findByStatus?status=sold", headers=self.headers)
        self.log_response(response, "test_get_pet_by_status")
        self.assertEqual(response.status_code, 200)
        pets = response.json()
        self.assertTrue(any(pet['id'] == PET_ID for pet in pets))
        #Test Ready? YES   
    
if __name__=='__main__':
    unittest.main(verbosity = 2)
