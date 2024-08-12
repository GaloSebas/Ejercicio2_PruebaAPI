package pets;

import com.intuit.karate.junit5.Karate;

public class Runner {

    @Karate.Test
    Karate testGetPetByStatus() {
        return Karate.run("get/pet-get-by-status.feature").relativeTo(getClass());
    }

}