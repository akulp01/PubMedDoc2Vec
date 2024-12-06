You will be running the final.py file, however this file makes a call to a function
in lateralCount.py so both files must be in the same directory. Make sure to adjust the file path to
the model file.

The only additional files you will need are all three of the SNOMED files you shared with us.
(reminder to change the file paths)

The program will print the conceptIds of all the comparisons it has evaluated, and then at the end 
print an array of 3 numbers. The first number is the number of comparisons failed at the 90% similarity
check. The second number is the number of pairs that are 90% similar and dont have the same parent count.
The third number is the amount of pairs above 90% similarity and have the same parent count but dont
have the same lateral relationships.

The function will also write all of the pairs that pass all tests to a csv file called resultFinalSpecimen
(reminder to change the file path)
