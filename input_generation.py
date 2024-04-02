import pandas as pd

filename='testset_chinese.csv'

df=pd.read_csv(filename)

for row_num in range(len(df)):
    sentence=df.iloc[row_num]['sentence']
    word=df.iloc[row_num]['word']
    input='In the sentence \'{0}\', the word \'{1}\' is a homophone word, can you tell its true meaning?'.format(sentence,word)
    print()
    print(row_num)
    print(input)
    print('answer:',df.iloc[row_num]['answer_english'])
    if filename=='testset_chinese.csv':
        print('answer:',df.iloc[row_num]['answer_chinese'])
    print()