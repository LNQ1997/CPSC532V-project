
import pandas as pd

filenames=['testset_chinese.csv','testset_english.csv','testset_espanol.csv']

for filename in filenames:
    print()
    df=pd.read_csv(filename)
    print('********',filename,'********')
    print('GPT-3.5 Accuracy:\t',df['GPT-3.5'].value_counts()['Y'],'%')
    print('GPT-4 Accuracy:\t\t',df['GPT-4'].value_counts()['Y'],'%')
    print('Ernie-3.5 Accuracy:\t',df['Ernie-3.5'].value_counts()['Y'],'%')
    print('Ernie-4.0 Accuracy:\t',df['Ernie-4.0'].value_counts()['Y'],'%')
    print()