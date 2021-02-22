#! /bin/bash
function mytests() {
   echo "Running all test files!"
   for i in Tests/test_*; do py.test "$i"
   done
}

mytests