import pandas as pd

#filename='testset_chinese.csv'
filename='testset_english.csv'

df=pd.read_csv(filename)

for row_num in range(len(df)):
    sentence=df.iloc[row_num]['sentence']
    word=df.iloc[row_num]['word']
    input='In the sentence \'{0}\', the word \'{1}\' is a homophone word, can you tell its true meaning?'.format(sentence,word)
    print()
    print(row_num)
    print(input)
    if filename=='testset_chinese.csv':
        print('answer:',df.iloc[row_num]['answer_english'])
        print('answer:',df.iloc[row_num]['answer_chinese'])
    elif filename=='testset_english.csv':
        print('answer:',df.iloc[row_num]['answer'])
    print()