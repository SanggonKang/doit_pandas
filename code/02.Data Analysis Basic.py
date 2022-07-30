import pandas as pd
# Load data
df = pd.read_csv('https://raw.githubusercontent.com/SanggonKang/doit_pandas/main/data/gapminder.tsv', sep='\t')

# 불러온 파일 살펴보기
print(df.head())
print(type(df))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

# 하나의 열 추출하기
country_df = df.country
print(type(country_df))
print(country_df.head())
print(country_df.tail())

# 3개의 열 추출하기
subset = df[['country', 'continent', 'year']]
print(type(subset))
print(subset.head())
print(subset.tail())

# 첫 번째 행 추출하기
print(df.loc[0])

# 마지막 행 추출하기
number_of_rows = df.shape[0]
print(number_of_rows)
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

# 3개의 행 추출하기
print(df.loc[[0, 99, 999]])

# 첫 번째 행 추출하기
print(df.iloc[0])

# 마지막 행 추출하기
print(df.iloc[-1])

# 3개의 행 추출하기
print(df.iloc[[0, 99, 999]])

# 마지막 행 추출하기
print(df.tail(n=1))
print(df.iloc[-1])

# 모든 행의 데이터에 대한 year, pop 열을 추출하기
print(df.loc[:, ['year', 'pop']])
print(df.iloc[:, [2, 4]])
range_set2_4 = list(range(2, 5, 2))
print(df.iloc[:, range_set2_4])

# 모든 행의 데이터에 대한 첫 번째 열부터 다섯 번째 열까지 추출하기
print(df.iloc[:, :5])
range_set0_4 = list(range(5))
print(df.iloc[:, range_set0_4])

# range 메서드를 이용하여 모든 행의 데이터에 대한 네 번째 열부터 여섯 번째 열까지 추출하기
print(df.iloc[:, 3:6])
range_set3_5 = list(range(3,6))
print(df.iloc[:, range_set3_5])

# range 메서드를 이용하여 모든 행의 데이터에 대한 첫 번째 열, 세번 째 열, 다섯 번째 열 추출하기 (한 열씩 건너뛰기)
print(df.iloc[:, 0:6:2])
range_set0_2_4 = list(range(0, 6, 2))
print(df.iloc[:, range_set0_2_4])

# 3개의 행과 3개의 열 추출하기
print(df.loc[[9, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

# year 로 그룹핑한 후 lifeExp 이 평균값 계산하기
print(df.groupby(['year']).lifeExp.mean())
print(df.groupby('year')['lifeExp'].mean())

# 1단계: year 로 그룹핑하여 그룹화된 DataFrame 을 만든다.
grp_year = df.groupby('year')
print(type(grp_year))
print(grp_year)

# 2단계: year 로 그룹화된 DataFrame 에서 lifeExp 열만 추출하여 그룹화된 시리즈를 얻는다.
grp_year_life = grp_year.lifeExp
print(type(grp_year_life))
print(grp_year_life)

# 3단계: 그룹화된 시리즈에서 평균을 계산한다.
print(grp_year_life.mean())

# 2개의 열을 그룹화하고 2개의 열의 평균값을 구한다.
print(df.groupby(['year', 'continent'])['lifeExp', 'gdpPercap'].mean())

# continent 별 unique 한 country 개수를 구한다.
print(df.groupby(['continent']).country.nunique())

# continent 별 country 개수를 구한다. (중복 count)
print(df.groupby(['continent']).country.count())

# year 별 lifeExp 평균값을 그래프로 그린다.
import matplotlib.pyplot as plt
df.groupby(['year']).lifeExp.mean().plot()
plt.show()


