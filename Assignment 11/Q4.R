Q4 Create a data frame in R for Students information
columns: RollNo, StudentsName, Age, Score
Write a R program to extract 3rd and 5th rows with 1st and 3rd columns from a given data frame.

Roll = c(7,8,9,10,11)
studName = c("Rahul","deepak","Harsh","Aditi","Pasha")
Age = c(20,22,21,20,20)
Score= c(17,20,20,15,16)

df = data.frame(
  roll_no = Roll,
  student_name = studName,
  age = Age,
  score = Score
)

print(df)
print(df[c(3,5),c(1,3)])
