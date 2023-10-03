Q3 create a data frame in R for Students information
# columns: RollNo, StudentsName, Age, Score
1.get number of columns
2. get number of rows
3. get columns
4. get first 3 rows
5. get last 3 rows
6. get general information
7. get statistical information


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

ncol(df)

nrow(df)

head(df,3)

tail(df, 3)

summary(df)

str(df)
