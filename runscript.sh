#! /bin/bash
function foo() {
   echo "Running all test files!"
   for i in Test_RC/*_test.py; do py.test "$i"
   done
}
foo

