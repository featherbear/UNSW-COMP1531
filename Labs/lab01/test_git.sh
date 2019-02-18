#!/bin/bash
branches=`git branch | wc -l`
success=0
if [ "$branches" -eq 1 ]
then
	echo 'You did not create a branch'
	success=1
fi

merges=`git log --merges --format="%aE" | egrep -v 'matt.phillips121@hotmail.com' | egrep -v 'matthew.perry@unsw.edu.au' | wc -l`
if [ "$merges" -eq 0 ]
then
	echo 'You did not do a merge? :( (at least not on this branch)'
	success=1
fi

if [ "$success" -eq 0 ]
then
	echo "Git tests passed"
fi
echo
echo
exit $success
