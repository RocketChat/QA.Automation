#! /bin/bash
echo Hello running all test files!
for i in *_test.py; do py.test "$i"
done
