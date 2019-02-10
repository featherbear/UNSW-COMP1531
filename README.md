# Lab 01


# Introduction to GitHub

## Aim

1.  To set up and become familiar with the course practices for lab/assignment release
2.  Get an introduction into how to use git effectively
3.  Learn some basic python syntax/practices

# Setup (Due: Prior to Wk 1 Lab)

## 1\. Sign up for GitHub

Github is a version control platform (like Bitbucket or GitLab) that uses git. It is a great way for developers to collaborate with one another. It will be the primary source of starter code distribution as well as where you will submit labs/assignments before being marked by your tutors. You will have to create an account here before you can start. Getting familiar with Github and how to use it is the aim of this lab.

**Instructions:**

-   I DON’T have an account on Github: Create an account at Github using either your student email ([zID@student.unsw.edu.au](mailto:zID@student.unsw.edu.au)) or your personal email.
    
    -   **Make sure to verify your email address. If you do not get an email straight away, go to [https://github.com/settings/emails](https://github.com/settings/emails) and click resend**

		![enter image description here](https://lh3.googleusercontent.com/dw7cyZjPlmwY0wgpdBkuDeGvX34GA2-kOjVJTAIgzk0_meqx6PXhcnWZGUX6X56ES8iAW_1-wSg)    

-   I ALREADY have an account on Github: Continue to the next step.
    


## 2\. CS1531 Github Organisation Membership

A Github organisation is a way that people can work together and have group ownership of repositories. You will be added to our organisation where we will release the starter code and solutions.

**Instructions:**

1. Follow the link and sign in. First with your cse credentials (if the _Authentication required_ alert box is shown), then click the **Sign in to Github** button and use your Github credentials [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login)
2. Go to https://github.com/orgs/cs1531/invitation to accept the invitation to join the organisation
3. Click "Join COMP1531" and you should now be part of the organisation :)

## 3\. Add your ssh key

There are two ways to authenticate with Github when you are working on your own machine:

1.  Use your username and password every time
2.  Authenticate using your SSH key which effectively links a certain machine to Github

Option 1 can get quite tedious when working consistently so we will be using the second option. Open up a terminal and run the following commands in terminal (*use the email you have used for GitHub*):

**Instructions:**

1.  `ssh-keygen -t rsa -C "github_email@example.com"`
2.  Hit Enter 3 times to accept default location and skip the password creation step. (You can **ignore** the output of this command)
3.  `cat ~/.ssh/id_rsa.pub`
4.  Copy the entire output of the above command, including the _ssh-rsa_ at the start
5.  Go to [https://github.com/settings/keys](https://github.com/settings/keys) and click **New SSH Key**
6.  Enter your name or your device's name as the title and paste the key (copied in the above step) into the text field. It should look something like below  
   ![enter image description here](https://lh3.googleusercontent.com/sKw2qrs9fNTKLYUFNMRlmOa14cSyLcSoafRL3A4G-bQuInPkL00BOht9FLiJIBwM7mYRoou8sx8)

**NOTE:** You will have to repeat this process if you change machines.

# Week 01 Lab Instructions

**This lab must be completed and solution must be uploaded to GitHub by Sunday, 11:59pm, end of week 01. Tutors will check the time-stamp, when the lab is marked in week 02 lab session. Tasks in this lab must be completed individually.**

## Github Exercises (5 marks)

## 0\. Install git

Throughout the course you will need to be comfortable with git. It comes pre-installed on most linux releases and is already installed on the CSE machines. To check if git is installed on your local machine use the command

```bash
git status
```

If it is installed you will see something like

> fatal: Not a git repository (or any of the parent directories):

If you do not have git installed, you will see something like

> bash: git: command not recognized

If this is the case, you will have to set it up using the following instructions

-   **Linux** \- Follow instructions at [https://git-scm.com/download/linux](https://git-scm.com/download/linux)
-   **Mac** \- `brew install git`


Once it has been installed, we also have to configure git.

**Instructions:**

1.  Try `git status` to check whether git is installed
    -   If not, follow one of the above instructions depending on your OS
2.  Configure git if you have not used it before with the following commands (including the quotes)

```bash
git config --global user.name "Your Name" 
git config --global user.email "github_email@example.com"
```

## 1\. Clone your first repo

Cloning a **repo** (a repo is just a directory that is linked with git) is how the codebase is linked from GitHub to your local computer so changes you make can be saved and shared with others. It is the final step before you can start making changes and contributing. A repo can be cloned at any time by someone who has access, so they can start working whenever they want. When a repo is cloned, all code that is uploaded on the server is copied to a desired location on your local machine.

In this course, starter code will be distributed through [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs). As labs get released, the dropdown menu will populate with starter code options. When you select one and the starter code will be imported to your local github account.

This is the process you will follow every lab to get your starter code.

**Instructions:**

1.  Go to [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs). 
	**NOTE:** You won't be able to access the page if you have not accepted the invitation to join the organisation.
2.  Select lab01 and click **Import**
3.  Follow the link that is shown in the green banner flashed at the top of the screen to go to the place where the repo has been imported
4.  Click on the Clone or download button.  
![enter image description here](https://lh3.googleusercontent.com/fRKmSGm0qTZZnPtE70T9AR0CmhgQL-Jj5U7N1etS407LDClwFeaWWo8Xa6b8HEMSanANCvR0lDE)
    
5.  If the title for the dropdown box is _Clone with HTTPS_ click on the **Use SSH** link on the right. The box should look like the below  
	![enter image description here](https://lh3.googleusercontent.com/8RM5PDX21n-QxcLDT0xWwLLNSfayAdpPrdU8K1JHIM6XQQX6brM3hXbUgcraUklT5G_AowslXOc)

6.  Copy the link in the text box
7.  Open a Terminal and navigate to the folder you want the lab to be in
8.  `git clone [link]` (Replace \[link\] with the copied link from above step)
9.  Type `ls` to ensure the folder has been copied correctly
10.  `cd [repo_name]` to navigate into the cloned repo
11.  Type `ls` again to see the copied files.

## 2\. Make your first commit

Now that you have cloned the repo, you are ready to work on the codebase locally.

A commit is an update of the remote (on the GitHub’s server) state of the repository. It saves changes that you have made and can be given a message to describe those changes. A good use of git involves a lot of commits with detailed messages.

Before you can commit, you have to do what is called staging your changes, which effectively tells git what changes you actually want to commit and what changes you don’t at the moment.

Commits are often followed by pushing which is how git actually uploads your commits to the remote server.

The command to commit and push are as follows:

```bash
git add [files_to_commit] # Stage
git commit -m "Detailed message describing the changes" # Commit
git push # Push
```

**Summary:**

1.  Add a new file called `first.txt` in the repo directory
2.  Add a line of text to the first.txt file using your favourite text editor and save.
3.  Go back to your terminal and enter the following commands:

```bash
git add first.txt`
git commit -m "Added a line to the first file"
git push
```

4.  MAKE SURE YOU UNDERSTAND THE PURPOSE OF EACH OF THE 3 ABOVE COMMANDS! If you are unsure about any of them, ask your tutor.
5.  Go back to GitHub and confirm that your changes have been pushed to the server.

## 3\. Do your first pull

Usually when you are using git, it is in a team. That means that you will not be the only one who is making the changes. If someone else makes a change and pushes it to the server, your local repo will not have the most up to date version of the files. Luckily, git makes it easy to update our local copy with the `git pull` command.

This command checks the remote server that your local repo is linked to and makes sure that all of your files are up to date. This ensures that you don’t accidentally do things like implement the same thing someone else has already done and also lets you use other peoples work (eg new functions) when developing.

Pulling regularly is one of the **most important** practices in git!

Unfortunately, at the moment you are just working individually. But GitHub still gives us a nice way to practice a `git pull`.

**Summary:**

1.  View your repo on GitHub. (The same link as step 1 in section 1 of the Laboratory activities)
2.  Click on the `first.txt` file
3.  Click the small ‘edit’ pencil icon in the top right
4.  Make any change you want to this file and click the ‘Commit Changes’ button at the bottom of the screen
5.  This will have changed the `first.txt` file on the server but not on your local environment. To fetch these changes use the `git pull` command from your terminal
6.  Confirm that your version of `first.txt` now has the changes you made on the web page

## 4\. Create your first branch

Branches are a vital part of git and are used so people can work on separate parts of the codebase and not interfere with one another or risk breaking a product that is visible to the client. Breaking something on one branch does not have an impact on any other.

Good use of git will involve separating parts of the project that can be worked on separately and having them in their own feature branch. These branches can then be merged when they are ready.

Useful commands for branches:

```bash
git checkout -b [new_branch_name] # Create a new branch and switch to it
git branch                        # List all current branches
git checkout [branch_name]        # Switch to an existing branch
```

**Summary:**

1.  Make your new branch with: `git checkout -b first_new_branch`
2.  List your branches to see that you have indeed swapped (use the above commands)
3.  Make another change to the `first.txt` file
4.  Try to push your changes to the server using the commands you learnt in the _Make your first commit_ section
5.  The above step should have given you the following error:  
    — `fatal: The current branch first_new_branch has no upstream branch.`  
    This means that the branch you tried to make a change on doesn’t exist on the server yet which makes sense because we only created it on our local machine.
6.  To fix this, we need to add a copy of our branch on the server and link them up so git knows that this new branch maps to a corresponding branch on the server
7.  `git push -u origin first_new_branch`

**NOTE:** The final step above must be run on the 1st push to every new branch that you have created on your local machine. After you have run this once, you should go back to simply using git push

## 5\. Merge your two branches

Merging branches is used to combine the work done on two different branches and is where gits magic really comes in. Git will compare the changes done on both branches and decide (based on what changes were done to what sections of the file and when) what to keep. Merges are most often done when a feature branch is complete and ready to be integrated with the master branch.

Since we have finished all that we are going to do (and think there are no bugs) on our _first\_new\_branch_ we can merge it back into master. It is a strong recommendation to have a version of the code that at least runs on master so people are not completely blocked. (DO NOT PUSH BROKEN CODE TO MASTER)

Another recommendation is to merge master into your branch before merging your branch into master as this will ensure that any merge into master will go smoothly.

**Commands for merging two branches**

```bash
git merge [target] # Merge the target branch into current
```

**NOTE:** A successful merge automatically uses the commits from the source branch. This means that the commits have already been made, you just need to push these to the server (`git push`)

**Summary:**

1.  Switch back to the master branch using one of the commands fom the above section
2.  Merge in the changes you made in the other branch  
    `git merge first_new_branch`
3.  Push the successful merge to the server to update the master branch on the server

## 6\. Engineer a merge conflict :(

Merge conflicts are the one necessary downside to git. Luckily, they can be avoided most of the time through good use of techniques like branches and regular commits, pushes and pulls. They happen when git cannot work out which particular change to a file you really want.

For this step we will engineer one so you can get a taste of what they are, how they occur and how to fix them. This will be the LAST time you will want one. The process may seem involved but it is quite common when multiple people are working at a time.

**Summary:** (All commands have been presented above)

1.  Add a line to the top of the `first.txt` file
2.  Add, commit and push your changes
3.  Switch to your _first\_new\_branch_
4.  Add a different line to the top of the `first.txt` file
5.  Add, commit and push your changes
6.  Merge master into your current branch
7.  This sequence of steps should made a merge conflict at the top of the `first.txt`

## 7\. Resolve your merge conflict :)

Resolving a merge conflict is as simple as editing the file normally, choosing what you want to have in the places git wasn’t sure.

This is a very simple example, but merge conflicts can be large and in many different places across a file/repo. If possible, avoid merge conflicts. This can be done by regularly pulling from the server to update your local copy and by making your branches in such a way that they handle only one feature/section of the code.

A merge conflict is physically shown in the file in which it occurs.  
`<<<<<<<` marks the beginning of the conflicting changes made on the **current** (merged into) branch.  
`=======` marks the beginning of the conflicting changes made on the **target** (merged) branch.  
`>>>>>>>` marks the end of the conflict zone.

Eg

```
This line could be merged automatically.
There was no change here either
<<<<<<< current:sample.txt
Merges are too hard. This change was on the 'merged into' branch
=======
Merges are easy. This change was made on the 'merged' branch
>>>>>>> target:sample.txt
This is another line that could be merged automatically
```

This above example could be solved in many ways, one way would be to just use the changes made on the target branch and delete those made on the current branch. Once we have decided on this we just need to remove the syntax. The resolved file would be as follows

```
This line could be merged automatically.
There was no change here either
Merges are easy. This change was made on the 'merged' branch
This is another line that could be merged automatically
```

We would then just commit the resolved file and the merge conflict is finished!

**Summary:**

1.  Open the `first.txt` file and decide which (or both) changes you want to keep
2.  Remove the merge conflict syntax
3.  Add, commit and push the resolved merge conflict

## Testing

You can run the `test_git.sh` file to check whether you have done most of the git exercises. Make sure you checkout the master branch before running this script.

# Python Introduction

Create a new branch called `python_exercises` to complete the following exercises. Remember to merge back into master when you are finished.

## 1\. Hello World (1 mark)

You have been introduced to python in week 1 so we will just get familiar with creating and running simple python programs. Python is an interpreted language so does not require and compilation like C does. That means executing python programs is as simple as one command.

**Summary:**

1.  Open the `hello.py` file.
2.  Complete the file so it prints “Hello World” on line 1
3.  Run it from the command line

```bash
python3 hello.py
```

4.  Commit your changes to git

## 2\. Integer addition (2 marks)

Python lists are probably the most used data structure that comes out of the box with python. They are somewhat similar to C arrays in the idea that they are a collection of data (hence data structure) but have a lot of extra functionality built in. One of the most useful things is their ability to grow dynamically. There is no need to declare the size of a list when creating it.

We will use a list to add up some integers in this exercise. (HINT: the python documentation is extensive and tells you how to use many of the in built functionality. [https://docs.python.org/3.6/tutorial/datastructures.html](https://docs.python.org/3.6/tutorial/datastructures.html) )

**Summary:**

1.  Open the `integer.py` file
2.  Line 1 has declared a list of integers. You are required to add the number 6 to the list (using the `append` function) and then add all of the numbers up using a `for` loop and print out the result
3.  Make the required edits to complete the above goal and run the `integer.py` in the same way you ran `hello.py`
4.  At the bottom of the file add the line

```python
print(sum(integers))
```

5.  Note that the answers should be the same. This is an example of one of python’s inbuilt functions. The lesson here is if you are doing something that you feel like is something that a lot of people would have wanted to do before you (like adding a list of numbers), python probably has a way to do it already. CHECK THE DOCS!

## 3\. List of Strings (2 marks)

Strings in python are far simpler than int C (char*) and can be used like any other variable (ie added to lists). They also have a lot of in built functionality like concatenation (appending one string to another) and making all characters lower case.

Strings can be indexed from with both positive indexes. Positive indexes work like you would expect, starting at 0 and ending at the length of the string. Negative indexes start at -1 and work their way from the back. Note that strings in python are not null terminated.

You can also get a range of characters from a string using the syntax `[begin:end]` (begin is included and end is excluded).

```python
test = "hey there you!"
print(test[0]) # Will print 'h'
print(test[1]) # Will print 'e'
print(test[-1]) # Will print '!'
print(test[-2]) # Will print 'u'

print(test[0:3]) # Will print 'hey'
print(test[:3]) # Will print 'hey' since an empty begin defaults to 0

print(test[:-1]) # Will print 'hey there you'
print(test[1:]) # Will print 'ey there you!' since empty end defaults to the end
```

**NOTE:** The same syntax can be used for elements in a list

The file `strings.py` has a list of strings that you will need to print out space separated. The **expected output** is:

> This list is now all together

Note that there is **NO** trailing space in the output.

**Summary:**

1.  Open the `strings.py` file
2.  Use a `for` loop to join all of the strings, separated by a space
3.  Print the new string such that the output matches the above (No trailing space in output)
4.  Now concatenating a list of strings seems like something that people would want to do often. So, as you may have been suspecting after the previous exercise, there is an in-built function to do this for you. Add the following line to the bottom of your `strings.py` file

```python
print(' '.join(strings))
```

5.  Commit your changes to GitHub
6.  Merge your `python_exercises` branch into `master`

## Testing

The `test_python.sh` file has some simple tests for testing the above python exercises. Run it using the following command:

```bash
./test_python.sh
```

The `test.sh` file is a combination of both the python and the git test scripts. To test the entire lab at once you can use

```bash
./test.sh
```

# Show your tutor and finish

That’s it for the first lab, please show your tutor your work and get them to mark you off.

# Optional Exercises for Bonus (Due: In Wk 1 Lab) (1 mark)

There are 2 optional exercises in the files

1.  `fib.py` \- you produce a list of fibannaci numbers of size n, where n is provided
2.  `commandLineCalc_easy.py` \- you use the Python3 `eval` function to calculate a basic mathematical expression containing addition/subtraction/multiplication/division/exponentiation. You have to filter invalid input to prevent cross-side scripting

For each of these files, run it as a program in the following fashion

```
python3 fib.py
```

If nothing shows up and the program finishes, then all the tests have passed! Otherwise, test failure output will appear, and you should read through this test output to understand where you went wrong.

These exercises are bonuses intended for those of you who have some previous programming experience.
