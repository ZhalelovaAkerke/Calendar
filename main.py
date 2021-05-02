import eel
import pandas as pd

eel.init("web")

df = pd.read_csv('df.csv')
df.Data = df.Data.apply(lambda x: str(x).strip()[:10])
df.drop('Unnamed: 0', axis=1, inplace=True)
df['Name - Surname/Holidays'] = df['Name - Surname/Holidays'].apply(lambda x: str(x).strip())
df['ID number'] = df['ID number'].apply(lambda x: str(x).strip())
df['History'] = df['History'].apply(lambda x: str(x).strip())
df['Speciality'] = df['Speciality'].apply(lambda x: str(x).strip())


@eel.expose
def get_info(date):
    global df
    string = str(df[df.Data == date].values)
    arr = []
    temp = string.split("'")[1:-1]

    for i in temp:
        if i == ' ':
            pass
        elif i == '\n  ':
            pass
        else:
            arr.append(i)

    arr2 = df.columns

    try:
        res = ''
        for i in range(len(arr)):
            res = res + str(arr2[i]) + ' - ' + str(arr[i]) + '; '
        return res
    except:
        return 'No info'


eel.start("main.html", size=(700, 700))
