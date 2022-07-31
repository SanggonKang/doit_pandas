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

# DataFrame 만들 때 index 이름을 지정하기, column 순서를 지정하기
family = pd.DataFrame(data={'Occupation' : ['salary man', 'student', 'play therapist'],
                            'Birthday' : ['04-15', '02-13', '01-27'],
                            'City' : ['Seoul', 'Seoul', 'Seoul']
                           },
                      index=['Gon', 'Min', 'Yun'],
                      columns=['Occupation', 'City', 'Birthday'])
print(family)


# Data Load
scientists = pd.read_csv('https://raw.githubusercontent.com/SanggonKang/doit_pandas/main/data/scientists.csv')
print(scientists)

# 첫 번째 행 선택하여 시리즈 만들기
fst_row = scientists.loc[0]
print(fst_row)

# index 확인하기 - index 속성 또는 key 메서드
print(fst_row.index)      # index 속성
print(fst_row.keys())     # keys 메서드

# 첫 번째 index 값 추출하기 - 슬라이싱 활용
print(fst_row.index[0])   # index 속성
print(fst_row.keys()[0])  # keys 메서드

# value (데이터) 확인하기 - values 속성
print(fst_row.values)

# 기초 통계 - mean, min, max, std
ages = scientists.Age
print(ages)
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())

# Series 에서 특정 조건을 만족하는 값만 추출하기 - boolean 추출
# 평균보다 나이가 많은 경우만 추출하기
print(ages[ages > ages.mean()])
print(ages > ages.mean())
print(scientists.Age[scientists.Age > scientists.Age.mean()])

# manual boolean
manual_boolean = [True, True, False, False, True, True, False, True]
print(ages[manual_boolean])

# 벡터 연산 (시리즈 + 시리즈, 시리즈 * 시리즈)
print(ages + ages)
print(ages * ages)

# 벡터에 스칼라 연산 (시리즈 + 스칼라, 시리즈 * 스칼라)
print(ages + 100)
print(ages * 2)

# 같은 인덱스끼리만 연산
print(ages + pd.Series([1, 100]))

# DataFrame 에서 특정 조건을 만족하는 값만 추출하기 - boolean 추출
# 평균보다 나이가 많은 경우만 추출하기
print(scientists[scientists.Age > scientists.Age.mean()])

# 문자열로 저장된 날짜 데이터를 datetime 자료형으로 바꾸고 날짜 형식을 YYYY-MM-DD 로 지정하기
# pd.to_datetime( 날짜 형식으로 바꿀 열, 날짜 형식 )
born_datetime = pd.to_datetime(scientists.Born, format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists.Died, format='%Y-%m-%d')

# 새로운 열 추가하기
# 한 번에 2개의 열 추가하기
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.head())

# 날짜를 계산한 값을 'age_days_dt' 이라는 새로운 열에 추가하기
scientists['age_days_dt'] = (scientists.died_dt - scientists.born_dt)
print(scientists.head())
print(scientists.info())

# Age 열의 데이터를 무작위로 섞기 - random 라이브러리의 shuffle 메서드
import random

random.seed(42)
random.shuffle(scientists.Age)
print(scientists.Age)

# Age 열을 삭제하기
scientists_dropped = scientists.drop(['Age'], axis=1)
print(scientists_dropped.columns)