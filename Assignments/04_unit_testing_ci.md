# Unit Testing and Continuous Integration with Travis CI

## Learning Objectives
* Use git feature branch development workflow with your team.
* Write unit tests.
* Execute unit tests using `py.test` (or framework of your choice).
* Utilize Travis CI integration with GitHub to verify testing compliance before
  merging pull request.

## Exercise
* Create a new repository in [GitHub:Duke-BME-Design](https://github.com/Duke-BME-Design/) with the name: `$TEAMNAME_testing'
* Make sure that all team members are Collaborators for the repository, along
  with with the instructors and TAs.  One way to expedite this process for this
  and future project repositories would be to create a `CODEOWNERS` file:
  https://help.github.com/articles/about-codeowners/
* Write a single module that has three functions for an input list of numbers:
  + Return the sum of all the numbers in the list.
  + Return a tuple of the min and max from the list.
  + Return the maximum difference between two adjacent numbers in the list.
* Each function above should be developed on its own git feature branch.
* Each function should have an associated unit test that explicitly tests its function.
* Your repository should contain a `.travis.yml` file to automatically run your unit tests when a branch is pushed to your GitHub origin.
* Generate Pull Requests to merge your three feature branches into your `master` branch *only once Travis CI reports a passing status*.
* Merge each passing Pull Request into your `master` branch.  Do not delete any of the merged feature branches.
* Create an annotated git tag called `v1.0.0` when your module is complete.
