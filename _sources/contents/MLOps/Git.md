---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Regression."
  "keywords": "interview, data science, machine learning, GIT, Cheat Sheet, Version control"
  "property=og:locale": "en_US"
---


## GIT

```{figure} ../MLOps/images/image1.PNG
---
name: image1
scale: 40%
---
[XKCD](https://xkcd.com/1597/)
```

| **Command**                                               | **Function**                                                                                                                                              |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| git init                                                  | Create empty Git repo in specified directory. Run with no arguments to initialize the current directory as a git repository.                              |
| git clone                                                 | Clone repo located at onto local machine. Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH.                    |
| git config user. name                                     | Define author name to be used for all commits in current repo. Devs commonly use --global flag to set config options for current user.                    |
| git add                                                   | Stage all changes in for the next commit. Replace with a to change a specific file.                                                                       |
| git commit -m ""                                          | Commit the staged snapshot, but instead of launching a text editor, use as the commit message.                                                            |
| git status                                                | List which files are staged, unstaged, and untracked.                                                                                                     |
| git log                                                   | Display the entire commit history using the default format. For customization see additional options.                                                     |
| git diff                                                  | Show unstaged changes between your index and working directory.                                                                                           |
| git remote add                                            | Create a new connection to a remote repo. After adding a remote, you can use as a shortcut for in other commands.                                         |
| git fetch                                                 | Fetches a specific , from the repo. Leave off to fetch all remote refs.                                                                                   |
| git pull                                                  | Fetch the specified remote's copy of current branch and immediately merge it into the local copy.                                                         |
| git push                                                  | Push the branch to , along with necessary commits and objects. Creates named branch in the remote repo if it doesn't exist.                               |
| git revert                                                | Create new commit that undoes all of the changes made in , then apply it to the current branch.                                                           |
| git reset                                                 | Remove from the staging area, but leave the working directory unchanged. This unstages a file without overwriting any changes.                            |
| git clean -n                                              | Shows which files would be removed from working directory. Use the -f flag in place of the -n flag to execute the clean.                                  |
| git diff HEAD                                             | Show difference between working directory and last commit.                                                                                                |
| git diff --cached                                         | Show difference between staged changes and last commit                                                                                                    |
| **GIT RESET**                                             |                                                                                                                                                           |
| git reset                                                 | Reset staging area to match most recent commit, but leave the working directory unchanged.                                                                |
| git reset --hard                                          | Reset staging area and working directory to match most recent commit and overwrites all changes in the working directory.                                 |
| git reset                                                 | Move the current branch tip backward to , reset the staging area to match, but leave the working directory alone.                                         |
| git reset --hard                                          | Same as previous, but resets both the staging area & working directory to match. Deletes uncommitted changes, and all commits after .                     |
| **GIT REBASE**                                            |                                                                                                                                                           |
| git rebase -i                                             | Interactively rebase current branch onto . Launches editor to enter commands for how each commit will be transferred to the new base.                     |
| **GIT PULL**                                              |                                                                                                                                                           |
| git pull --rebase                                         | Fetch the remote's copy of current branch and rebases it into the local copy. Uses git rebase instead of merge to integrate the branches.                 |
| **GIT PUSH**                                              |                                                                                                                                                           |
| git push --force                                          | Forces the git push even if it results in a non-fast-forward merge. Do not use the --force flag unless you're absolutely sure you know what you're doing. |
| git push --all                                            | Push all of your local branches to the specified remote.                                                                                                  |
| git push --tags                                           | Tags aren't automatically pushed when you push a branch or use the --all flag. The --tags flag sends all of your local tags to the remote repo.           |
