#! /bin/bash
echo Hello running all test files!
for i in Test_RC/*_test.py; do py.test "$i"
done
