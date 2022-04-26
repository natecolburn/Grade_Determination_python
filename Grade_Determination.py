#   PROGRAMMER:     Nathan Colburn
#   PROGRAM NAME:   Calculating Test Averages and determining the
#                   letter grade using nested IF statements
#   DATE WRITTEN:   7/26/20


#   PURPOSE:
''' This program calculates the average of five test scores,
    sums, and calculates the average of the test scores.
    The program then determines the letter grade using IF statements.
    It displays the original data with with labels along with
    the processed results. '''

#=======================================================================================
# Initialize variables
letterGrade = "";
sumTest = 0.00;
testAverage = 0.00;

#=======================================================================================

# Input statements
studentName = str(input("<Enter the student's full name> "));
test1 = float(input("<Enter test score #1 of " + studentName + "> "));
test2 = float(input("<Enter test score #2 of " + studentName + "> "));
test3 = float(input("<Enter test score #3 of " + studentName + "> "));
test4 = float(input("<Enter test score #4 of " + studentName + "> "));
test5 = float(input("<Enter test score #5 of " + studentName + "> "));


#=======================================================================================
#Calculations / processing
sumTest = (test1 + test2 + test3 + test4 + test5);
testAvg = sumTest / 5;

#=======================================================================================
'''nested if statements to determine a letter grade based on the calculated
    test average; Compound statements are used with the "and" logical operator in order
    to simplify the IF statements. '''

if (testAvg >= 90) and (testAvg <= 100):
    letterGrade = "A. Excellent work!";
else:
    if (testAvg >= 87) and (testAvg <= 89.99):
        letterGrade = "B+. Very good job.";
    else:
        if (testAvg <= 86.99) and (testAvg >= 80):
            letterGrade = "B. Good work."
        else:
            if (testAvg <= 79.99) and (testAvg >= 77):
                letterGrade = "C+. Pretty good but study some more.";
            else:
                if (testAvg <= 76.99) and (testAvg >= 70):
                    letterGrade = "C. Ok but need to buckle down!";
                else:
                    if (testAvg <= 69.99) and (testAvg >= 67):
                        letterGrade = "D+. You need to see the tutor.";
                    else:
                        if (testAvg <= 66.99) and (testAvg >= 60):
                            letterGrade = "D. Ok talk with Professor";
                        else:
                            if (testAvg <= 59.99) and (testAvg >= 0):
                                letterGrade = "F. See you next semester!";
                            else:
                                print(end= "");


#=======================================================================================
# Output Statements
print();
print("TEST RESULTS FOR " + studentName + ":");
print("-" * 85);

print("Test #1 = " + format(test1, "6.2f") + "%");
print("Test #2 = " + format(test2, "6.2f") + "%");
print("Test #3 = " + format(test3, "6.2f") + "%" );
print("Test #4 = " + format(test4, "6.2f") + "%");
print("Test #5 = " + format(test5, "6.2f") + "%");
print("-" * 85);
print("The sum of all the test scores = " + format(sumTest, "7.2f"));
print("The average of the test scores = " + format(testAvg, "7.2f") + "%");
print("-" * 85);
print();print();


#=======================================================================================
# Print letter grade
print("-" * 85);
print(studentName + " Earned a letter grade of an/a " + letterGrade);
print("=" * 85);
#=======================================================================================
# End Program
