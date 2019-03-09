---
title: "Git Cheatsheet"
date: 2019-02-12T18:09:43+11:00
description: "An unextensive list of commands for using Git"

categories: ["Info"]

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---
# Git Keywords
* HEAD - Dynamic pointer to the latest comment of a branch
* Tracking
* Stage
* Commit
* Fast forward - move the pointer   / vs   recursive

# Git Basic
## Basic Workflow
* `git add ...`
* `git commit -m "your message here"`

## Check Git status
`$ git status`

## Clone a repository
`$ git clone <repoURL>`

## Create a new repository
`$ git init`  
`$ git init <repoName>`

## Stage files for the next commit
`$ git add <file1> <file2> <...>`  
`$ git add .`

## Commit staged files
`$ git commit -m <message>`  
`$ git commit -a -m <message>` # Add and commit all modified  
`$ git commit --amend`

## View all commits
`$ git log`

---

# Git Branches
Branches could be considered as pointers to commits
## Checkout a branch
`$ git checkout <branch>`

## Checkout into a new branch
`$ git checkout -b <branch>`  
_Same as `git branch <branch>`, then `git checkout <branch>`_

## Create a new branch but don&apos;t checkout
`$ git branch <branch>`

## Delte a branch
`$ git branch -d <branch>`

---

# Git Merging
_From the branch you want merge into_  
`git merge <branch>`

Resolving commits  
1)  
`cd {master}`  
`git merge <branch>` # Creates conflict file  
\<Manually modify>  
`git commit`

2)  
`cd {branch}`  
`git merge <master>`  

# Remote
`$ git remote add <remoteName> <remoteURL>`

`$ git push <remoteName> <branch>`

# Other Stuff

## Merge unrelated respositories
> Useful for me to merge the private lab repositories from this course to my own repo.

**At the end of each lab...**  
```
# cd <lab_folder>
mkdir Labs/lab<n> -p
git mv !(Labs) Labs/lab<n>
git commit -a -m "Move lab into correct repo folder"
```  

```
# cd <UNSW-COMP1531>
git remote add lab<n> <lab_folder>
git fetch lab<n>
git merge -S --allow-unrelated-histories lab<n>/master
git remote rm lab<n>
```


## Set up your SSH Keypair
`$ ssh-keygen -t rsa -b 4096 -C "<comment>"`

{{<admonition abstract Example>}}
{{< typedjs >}}
[
"ssh-keygen -t rsa -b 4096 -C \"Andrew's home computer\"\n\
`Generating public/private rsa key pair.`\
^1500\
\n`Enter file in which to save the key (/home/andrew/.ssh/id_rsa): `\
^500↵\
\n`Enter passphrase (empty for no passphrase): `\
^500↵\
\n`Enter same passphrase again: `\
^500↵\
\n`Your identification has been saved in /home/andrew/.ssh/id_rsa.`\
\n`Your public key has been saved in /home/andrew/.ssh/id_rsa.pub.`\
\n`The key fingerprint is:`\
\n`SHA256:hSU0bJT2bfVsXl8eKrOc32bfeE/3RfZxGg1KzOl9U3k Andrew's home computer`\
\n`The key's randomart image is:`\
\n`+---[RSA 4096]----+\
\n|       +=..      |\
\n|        == o .  .|\
\n|       o.o. = ..E|\
\n|         .=ooo ++|\
\n|        S+ +o.+=B|\
\n|          +o ..**|\
\n|         .  + . =|\
\n|           .. .=*|\
\n|          .o..+oB|\
\n+----[SHA256]-----+`"
]
{{< /typedjs >}}
{{</admonition>}}