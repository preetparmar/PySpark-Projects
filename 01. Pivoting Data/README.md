# Pivoting Data

## Project Requirement

- We have multiple CSV files with Date and Stock values
- We are only interested in some columns
- We need to merge all the files and then later pivot the file

## Process Steps

- Create a function for selecting the desired columns and renaming the column depending on the file.
- Join all the files into one DataFrame.
- Unpivot the data.

### Additional Notes

- I have used python list comprehensions for creating lists of DataFrames.
- I have used the "reduce" function to iterate over a list, resulting in one DataFrame in the end.

## Original Data

Preview of Apple Stock File:
| Date | Open | High | Low | Close | Adj Close | Volume |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | -------- |
| 2018-08-27 | 217.149994 | 218.740005 | 216.330002 | 217.940002 | 214.609741 | 20525100 |
| 2018-08-28 | 219.009995 | 220.539993 | 218.919998 | 219.699997 | 216.34285 | 22776800 |
| 2018-08-29 | 220.149994 | 223.490005 | 219.410004 | 222.979996 | 219.572723 | 27254800 |
| 2018-08-30 | 223.25 | 228.259995 | 222.399994 | 225.029999 | 221.591385 | 48793800 |
| 2018-08-31 | 226.509995 | 228.869995 | 226.0 | 227.630005 | 224.151657 | 43340100 |

## Final Data

| Date       | Company   | Price       |
| ---------- | --------- | ----------- |
| 2018-08-27 | apple     | 214.609741  |
| 2018-08-27 | bmw       | 79.018585   |
| 2018-08-27 | tm        | 124.692833  |
| 2018-08-27 | google    | 1241.819946 |
| 2018-08-27 | microsoft | 107.904411  |
| 2018-08-28 | apple     | 216.34285   |
| 2018-08-28 | bmw       | 80.158409   |
| 2018-08-28 | tm        | 124.298454  |
| 2018-08-28 | google    | 1231.150024 |
| 2018-08-28 | microsoft | 108.554207  |
