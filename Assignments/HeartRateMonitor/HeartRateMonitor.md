# Heart Rate Monitor

You will be working on this assignment **individually**.  Create a new
repository--`bme590hrm`--in your individual space on GitHub, and make sure to
add all instructors and teaching assistants as `CODEOWNERS`.

## Heart Rate Monitor: Functional Specifications
  + Use an object-oriented approach for this assignment
  + Read ECG data from a CSV file that will have lines with `time, voltage`.
    Example data can be found in the `test_data/` directory in this assignment
    directory.  *Note that in future assignments building on this project, the
    input data format will change, so makes this a truly modular input
    component!*
  + Your class should have, at minimum, the following calculated attributes:
    - `mean_hr_bpm`: estimated average heart rate over a user-specified number
      of minutes (can choose a default interval)
    - `voltage_extremes`: tuple containing minimum and maximum lead voltages
    - `duration`: time duration of the ECG strip
    - `num_beats`: number of detected beats in the strip
    - `beats`: numpy array of times when a beat occurred
  + An output JSON file should be saved with the same name as the input CSV
    file that contains the values of all of your object attributes.

## Git Version Control Practices
  + Frequent and meaningful commits!  Branches should be used for specific
    feature implementations, bug fixes, etc.  Do not delete your branches after
    merging them into master.
  + Project management Milestones \& Issues (with associated git commits),
    along with descriptive Labels.
  + Unit tests for all algorithmic functions written _before_ your
    actual code.  These should also be associated with related Issue comments.
  + Feature branches merged into master (after passing unit tests with Travis CI).
  + Make sure that your project has a `README.md` file that describes how
    to run it, and also make sure that you associate a software license with
    your project (http://choosealicense.com/).  
  + Bonus - integrate a Travis badge in your README that displays the status of test passage.
  + Create an annotated tag titled ``v1.0.0'' when your assignment is
    completed and ready to be graded.  Check out details on semantic versioning
    here: http://semver.org
  + Travis CI should be active.

## Python Code Expectations
* Utilize a virtual environment.
* Have Sphinx-friendly
  (https://pythonhosted.org/an_example_pypi_project/sphinx.html) docstrings for
  all methods.  
* Unit tests should exist in a separate file or directory of test files. 
* Achieve the functional specifications with passing unit tests.  Make sure
  that you include a test for writing the output JSON file.
* All methods should have well-defined input-action-output (as the unit tests will demand).
* There should be no ``hard-coded'' values in your methods.
* Follow PEP8 style standards (https://www.python.org/dev/peps/pep-0008/).  *Note that manually trying to impose compliance will be very challenging; use
  an IDE or text editor with a PEP8 linter plugin.*
* Exception handling
* Gracefully terminate when the input file ends
* Create meaningful logs (e.g., `INFO` for assigning values to attributes,
  `WARNING` or `ERROR` for exceptions)

## Grading Criteria
* Effective version control usage
* Adequate unit test coverage and method modularity
* Python style and docstrings
* Achieves functional specifications
* Works with all of the provided test data
* Extra features = bonuses!
