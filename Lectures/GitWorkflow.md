# Git Workflow

## Feature Branch Development
* Use branches to develop new features, fix bugs, try out new things without affecting your `master` branch.
* A useful branch naming convention: `$USER/$FEATURE`
* `master` should ideally hold only "functional" code.
* When you want to presrve a snapshot of the `master` branch state, you can create an annotated tag:
```
git tag -a 'v0.0.1' -m 'first semantically-versioned tag'
```

### Collaboration on Single Repository
* Settings -> Collaborators
* Everyone clones the same repository and submits Pull Requests from feature branches.

### Forking Repository
* If you don't have Collaborator access to a repository, you can still create a Pull Request from a *fork* of that repository.
* You *must* commit your changes on a branch of your forked-repository; trying
  to issue a Pull Request from your `master` branch will cause headaches.

### Pull Requests 
* A GitHub feature to merge a branch into another branch (commonly a feature
  branch into `master`, but can be any branch into another branch).
* Can use commit / file change review features and/or perform an actual code
  review before accepting changes.
* Merge strategies:
  + Merge (creates a commit reflecting the merged content, in addition to the
    individual commits on the branch being merged)
  + Squash-n-Merge (create a merge commit, but "squash" all of the commits of
    the feature branch into one)
  + Rebase (integrate the commits of the feature branch into your target branch
    by "replaying" them into the history)

### CLI Merging
* Merging can also be be done using the CLI, without a GitHub Pull Request.
* `git merge [--squash]`

### In-Class Mission
For everything below, `$netid` refers to your Duke Net ID (e.g., `mlp6`), not your GitHub username.
* Fork this repository: https://github.com/mlp6/bme590s18_lecture03
* Clone your forked repository to your local computer
* Create a new branch called `$netid/myinfo`
* In your new branch, create a new file called `$netid.csv`
* Add a line to that file that contains:
```
# Firstname, Lastname, Net ID, GitHub Name, Teamname
# For example:
Mark, Palmeri, mlp6, mlp6, MetalRules
```
Your Teamname should:
  + Contain no spaces
  + Use CamelCase
* Push your working branch to your GitHub fork
* Using GitHub, submit a Pull Request to merge your branch on your forked
  repository back into `mlp6/bme590s18_lecture03`
