# Git Fundamentals
## Markdown Formatting
\*.md files indicate markdown formatting on render of content: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## Completing Tasks with Git
* How do I clone a repository created / existing on GitHub on my local computer?
```
git clone git@github.com/$USERNAME/$REPONAME.git [$LOCALREPONAME]
```
This command will clone the most recent files and complete history of the
repository to a local directory (can specify a name different than the
repository name with `$LOCALREPONAME`.

* How do I figure out what files in my local repository have changed or their status in the git commit process?
```
git status
```
This will show files that are untracked (not under git version control),
modified (changed since last committed version), and files that are queued for
commit.
* How do I see what has changed in a file since it was last committed?
```
git diff
```
Can I look at a diff for a local file compared to a remote file (e.g.,
something on `origin`)?
```
# yes!
git diff $REMOTE/$BRANCH:$REMOTE/PATH/FILE LOCALPATH/FILE
```

* How do I queue files to be added / removed in the next commit?
```
git add $FILENAME
git rm $FILENAME
```
* How do I commit changes to the repository version history on my local computer?
```
git commit
```

:sparkles: Shortcut :sparkles: If you want to commit changes for all modified
files that have been previously added to the repository, you can add an commit
using the following command: `git commit -am 'commit message'`.

* How do I send or get committed changes from GitHub (your default remote `origin`)?
```
git push
git pull
```
* How do I figure out what remote version of my repository are linked to my local repository?
```
git remote
```
You can add, remove and modify remote URLs with this same command.

## Bug Fix / Feature Branch Development
How do I create a new branch to fix a bug / develop a new feature?
```
git branch $BRANCHNAME

# then need to change onto that branch to work
git checkout $BRANCHNAME

# can do both of those steps at once
git checkout -b $BRANCHNAME
```
I want to push a new branch to GitHUb; what do I have to do?
```
# the very first time you go to push content to a new branch on the origin, you
# need to tell the origin to create that branch
git push --set-origin origin $BRANCHNAME

# once that branch is created, git push will automatically push to the branch
# that you have specified
```

## GitHub Issues
* Issues are used to report bugs, request features, etc.
* Commits related to issues can automatically trigger action (e.g., closing,
  fixing) using GitHub keywords:
  https://help.github.com/articles/closing-issues-using-keywords/

## Pull Requests
* One way that branches can be merged into `master` is using Pull Requests on GitHub

## Ignoring local files from git control
Text editors and IDEs can create a lot of temporary files in your repository
that you do not want to share with collaborators.  Additionally, you may have
test data and scripts that you also don't want to share.  Instead of having
these files constantly show up in your `git status` output, you can tell git to
ignore these files by creating a `.gitignore` files that contains file and
directory name patterns that you want to ignore.  If there are files that you
very commonly need to ignore in your repositories, you can add them to a file
in your home directory: `$HOME/.gitignore_global`.
