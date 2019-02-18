#!/bin/bash
./test_git.sh
git=$?

./test_python.sh
python=$?

if [[ "$git" -eq 0 && "$python" -eq 0 ]]
then
	echo "All Tests Passed!!"
fi

