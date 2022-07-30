import pandas as pd

# Series 만들기
s = pd.Series(['banana', 42])
print(s)

s = pd.Series(['Wes Mckinney', 'Creator of Pandas'])
print(s)

# Series 에서 index 이름을 지정하기 - index = [ list ]
s = pd.Series(['Wes Mckinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

# DataFrame 만들기 - dictionary 로 만들어야 한다.
family = pd.DataFrame({'Name': ['Gon', 'Min', 'Yun'],
                       'Occupation' : ['salary man', 'student', 'play therapist'],
                       'Birthday' : ['04-15', '02-13', '01-27'],
                       'City' : ['Seoul', 'Seoul', 'Seoul']
                      })
print(family)
