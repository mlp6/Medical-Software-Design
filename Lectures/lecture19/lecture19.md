# Lecture 19 
Today's agenda:
* Exceptions and error handling in a web service
* Assignment clarifications on data formatting
* GIT submodules
* Did everyone get VM setup and working from last class?

## GIT Submodules:
Git submodules are used to pull in an external repository into your current repository (as a sort of dependency). It's essentially like having another repository be a sub-repository to your current repository where you're writing your code. To get this setup, follow the steps below.

* Inside the current directory of your repository where you are writing code, go ahead and execute the below the add the repository:
  ```sh
  git submodule add git@github.com:mlp6/Medical-Software-Design.git
  ```
* Now `git add` the new files and commit them to your repository.
* Everytime you clone your main code repository from now on, be sure to use `git clone --recursive` to ensure you fetch and clone the git submodule repository. If you already have a repository cloned and need to pull down new submodules, simply run `git submodule init` and then `git submodule update`.
