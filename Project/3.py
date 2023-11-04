import pandas as pd
import random as rd

df = pd.read_csv('HouseList.csv')
name = list(df['Name'])
rollno = list(df['Roll No'])
degree = list(df['Degree'])
gender = list(df['Gender'])

rollno1 = pd.read_csv('RollNos.csv')

rollno_yes = list(rollno1['Roll No'])

# create new csv file with columns name, rollno_yes, degree, gender

dataset = {
    'Name': [],
    'Roll No': [],
    'Degree': [],
    'Gender': [],
    'Sem': [],
    'Age': [],
    'Gym/badminton': [],
}

count = 0
indices = []
for i in range(1700):
    if count == 460:
        break
    k = 0
    index = rd.randint(0, 1700)
    if index in indices:
        continue
    indices.append(index)
    
    for j in range(len(rollno_yes)):
        if rollno[i] == rollno_yes[j]:
            k = 1
            break
    if k == 1:
        continue
    if degree[i] != "B.Tech" and degree[i] != "M.Tech":
        continue
    else:
        if rollno[i] == "kul":
            continue
        if rollno[i][4] == 'B':
            if rollno[i][3] == '0':
                sem = '7'
                age = rd.randint(20,22)
            elif rollno[i][3] == '1':
                sem = '5'
                age = rd.randint(19,21)
            elif rollno[i][3] == '2':
                sem = '3'
                age = rd.randint(18,20)
            elif rollno[i][3] == '3':
                sem = '1'
                age = rd.randint(17,19)
        if rollno[i][4] == 'M':
            sem = '3'
            age = rd.randint(23,26)

        dataset['Name'].append(name[i])
        dataset['Roll No'].append(rollno[i])
        dataset['Degree'].append(degree[i])
        dataset['Gender'].append(gender[i])
        dataset['Sem'].append(sem)
        dataset['Age'].append(age)
        dataset['Gym/badminton'].append(0)
        count += 1

df = pd.DataFrame(dataset)
df.to_csv('Dataset_rol_1.csv', index=False)