import pandas as pd
import random as rd

df = pd.read_csv('data_dsProject.csv')
# select name, roll, 
name = list(df['Name'])
rollno = list(df['RollNo'])
degree = list(df['Degree'])
age = list(df['Age'])
gender = list(df['Sex'])

data = [name, rollno, degree, age, gender]

# print(len(Year))

dataset = {'Name' : [],
           'RollNo' : [],
           'Degree' : [],
           'Age' : [],
           'Gender' : [],
           'Semester' : [],
           'Height' : [],
           'Weight' : [],
           'BMI' : [],
           'Gym/Badminton' : []
          }
dataset = pd.DataFrame(dataset)
# first add random 300 rows from data to dataset in order

rollnos = ["CS22M1007",
    "CS22M1001",
    "EC22M1002",
    "ME20B2018",
    "EC21B1044",
    "EC21B1022",
    "ME21B2009",
    "ME21B2008",
    "ME21B2012",
    "ME21B2007",
    "CS21B043",
    "CS21B1041",
    "MPD191004",
    "CS20B1057",
    "CS21B1052",
    "CS21B1034",
    "CS21B1075",
    "CS21B1033",
    "CS21B1025",
    "CS21B1015",
    "CS21B1003",
    "CS21B1086",
    "CS21B1082",
    "CS21B1088",
    "CS21B2042",
    "CS22B1018",
    ]

for _ in range(0, 300):
    i = rd.randint(0, 790)
    if data[1][i] != None:
        name = data[0][i]
        rollno = data[1][i]
        degree = data[2][i]
        age = data[3][i]
        gender = data[4][i]
        # change rollno to string
        rollno = str(rollno)

        # calculate semester from rollno
        if rollno[3] == '0':
            semester = 7
        elif rollno[3] == '1':
            semester = 5
        elif rollno[3] == '2':
            semester = 3
        elif rollno[3] == '3':
            semester = 1
        else:
            semester = rd.randint(1, 4)

        new_row = {'Name' : name,
                'RollNo' : rollno,
                    'Degree' : degree,
                    'Age' : age,
                    'Gender' : gender,
                    'Semester' : semester,
                    'Height' : None,
                    'Weight' : None,
                    'BMI' : None,
                    'Gym/Badminton' : None
                    }
        dataset = dataset._append(new_row, ignore_index=True)


dataset.to_csv('dataset.csv', index=False)