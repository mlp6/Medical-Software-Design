# Unit Testing + Continuous Integration

In this assignment you will write and test several python modules. You will also need to configure Continuous Integration (CI) to automatically run tests on push and pull request events. 

Go ahead and create a repository for your assignment using the [GitHub classroom assignment link here](https://classroom.github.com/a/NoN-yCNC).

When setting up Travis CI, ensure that your repository is "turned on" in the travis control panel for the BME organization [here](https://travis-ci.org/profile/Duke-BME-Design).

## Is Tachycardic?
Similar to the example seen in the [lecture notes](Lectures/UnitTestingCI.md), write a function called `is_tachycardic` in a file called `tachycardia.py`. This function takes one string input from an [optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition) scan of a patient medical report, and must return if that string represented that the patient was tachycardic. In this basic example you should expect to receive strings that contain only contains the word `tachycardic` **BUT there are no guarantees on spaces, capitalization, punctuation, etc** that may creep into the string. The only guarantee is that only one word representation of `tachycardic` will be present. Try to be as comprehensive as possible with your unit tests (e.g. testing for accidental case mismatches, etc). You must use `@pytest.mark.parametrize` for at least one test. 

**Small Bonus**: Make your `is_tachycardic` function more tolerant to close representations of the word `tachycardic`. For example if you get `tachycrdic` or other minor misspellings you should be able to tolerate and test those. 

