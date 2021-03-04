#! /bin/bash
function mytests() {
   echo "Running all test files!"
   for i in Tests/test_*; do py.test -v -s --alluredir="./reports/allure_reports" "$i"
   done
}

mytests