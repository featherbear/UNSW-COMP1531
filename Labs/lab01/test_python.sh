#!/bin/bash
hello=`python3 hello.py`
success=0
if [ "$hello" != "Hello World" ]
then
	echo "hello.py did not print 'Hello World'"
	success=1
fi

twentyone=`python3 integer.py | sed -n 1p`
if [ "$twentyone" != "21" ]
then
	echo "integer.py did not get the right sum (21)"
	success=1
fi

sentence=`python3 strings.py | sed -n 1p`
if [ "$sentence" != "This list is now all together" ]
then
	echo "strings.py did not print the right sentence. Check trailing space?"
	success=1
fi

if [ "$success" -eq 0 ]
then
	echo "Python exercises passed"
fi
exit $success
