# Heart Rate Monitor

Create a new repository--`bme590hrm`--in your individual space on GitHub, and make sure to add all instructors and teaching assistants as [CODEOWNERS](https://help.github.com/articles/about-codeowners/).

## Heart Rate Monitor: Functional Specifications
  + Read ECG data from a CSV file that will have lines with `time, voltage`.  Example data can be found in the `test_data/` directory in this assignment directory.  
  + The following data should be calculated and saved as keys in a Python dictionary called `metrics`:
    - `mean_hr_bpm`: estimated average heart rate over a user-specified number
      of minutes (can choose a default interval)
    - `voltage_extremes`: tuple containing minimum and maximum lead voltages
    - `duration`: time duration of the ECG strip
    - `num_beats`: number of detected beats in the strip
    - `beats`: numpy array of times when a beat occurred
  + Your `metrics` dictionary should be output as a [JSON](https://json.org/) file should be saved with the same name as the input CSV file that contains the values of all of your object attributes.  Note that there is a [json module](https://docs.python.org/3.6/library/json.html) that will make your life easier.

## Git Version Control Practices
  + Frequent and meaningful commits!  
    - Branches should be used for specific feature implementations, bug fixes, etc.  
    - Do not delete your branches after merging them into master. 
    - If you locally merge, use the `-no-ff` option so that we can audit your commit logs to see the merge operations.  (This will lead to a "messy" commit history, but something that we want to see for grading purposes.)
  + Project management Milestones \& Issues (with associated git commits), along with descriptive Labels.
  + Write a single function for each functional element of your code, and all function must have associated unit tests with complete coverage.
  + Feature branches merged into master (after passing unit tests with Travis CI).
  + Make sure that your project has a `README.md` file that describes how to run it, and also make sure that you associate a software license with your project (http://choosealicense.com/).  
  + Bonus - integrate a Travis [status badge](https://docs.travis-ci.com/user/status-images/) in your README that displays the status of test passage.
  + Create an annotated tag titled `v1.0.0` when your assignment is completed and ready to be graded.  Check out details on semantic versioning here: http://semver.org

## Python Code Expectations
* Utilize a virtual environment.
* Have Sphinx-friendly (https://pythonhosted.org/an_example_pypi_project/sphinx.html) docstrings for all methods.  
* Unit tests should exist in a separate file or directory of test files. 
* Achieve the functional specifications with passing unit tests.  Make sure that you include a test for writing the output JSON file.
* All methods should have well-defined input-action-output (as the unit tests will demand).
* There should be no "hard-coded" values in your methods.
* Adhere to [PEP8](https://www.python.org/dev/peps/pep-0008/) style. 
* Implement exception handling
* Gracefully terminate when the input file ends
* Create meaningful logs (e.g., `INFO` for assigning values to attributes, `WARNING` or `ERROR` for exceptions)

## Grading Criteria
* Effective version control usage
* Adequate unit test coverage and functional modularity
* Python style and docstrings
* Achieves functional specifications
* Works with all of the provided test data
* Extra features = bonuses!
