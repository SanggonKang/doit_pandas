# 앤스콤 데이터 집합 불러오기
import seaborn as sns

anscombe = sns.load_dataset("anscombe")
print(anscombe)
print(type(anscombe))

# matplotlib 라이브러리 불러오기
import matplotlib.pyplot as plt

# data 값이 I인 것만 추출하기
dataset_I = anscombe[anscombe.dataset == 'I']
plt.plot(dataset_I['x'], dataset_I['y'], 'o')   # 'o' 는 점그래프
plt.show()

# matplotlib 라이브러리로 그래프 그리기
# 1) 전체 그래프가 위치할 기본 틀을 만든다.
# 2) 그래프를 그려 넣을 그래프 격자를 만든다.
# 3) 격자에 그래프를 하나씩 추가한다. 왼쪽에서 오른쪽 방향
# 4) 첫 번째 행이 꽉 차면 두 번째 행에 넣는다.
# dataset 열의 값이 I, II, III, IV 인 것을 boolean 추출한다.
dataset_II = anscombe[anscombe.dataset == 'II']
dataset_III = anscombe[anscombe.dataset == 'III']
dataset_IV = anscombe[anscombe.dataset == 'IV']

# 그래프가 위치할 기본 틀을 만든다.
fig = plt.figure()

# 그래프 격자를 그린다. add_subplot (행 크기, 열 크기)
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

# 그래프를 그린다. plot 메서드
axes1.plot(dataset_I['x'], dataset_I['y'], 'o')
axes2.plot(dataset_II['x'], dataset_II['y'], 'o')
axes3.plot(dataset_III['x'], dataset_III['y'], 'o')
axes4.plot(dataset_IV['x'], dataset_IV['y'], 'o')

# 그래프에 제목 넣기. set_title
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

# 기본틀(fig)에 제목 넣기. suptitle
fig.suptitle("Anscombe Data")

# 레이아웃 조정. tight_layout()
fig.tight_layout()

fig
plt.show()

# seaborn 라이브러리에서 tips 데이터 집합 불러오기
tips = sns.load_dataset('tips')
print(tips.head())
print(type(tips))

# 그래프가 위치할 기본 틀을 만든다.
fig = plt.figure()
axes01 = fig.add_subplot(1, 1, 1)

# total_bill 에 대한 히스토그램을 그린다. hist(열, bins)
axes01.hist(tips['total_bill'], bins=10)
axes01.set_title('Histogram of Total Bill')
axes01.set_xlabel('Frequency')
axes01.set_ylabel('Total Bill')

fig
plt.show()

# total_bill 과 tip 의 산점도 그래프를 그린다. scatter(열1, 열2)
scatter_plot = plt.figure()
axes02 = scatter_plot.add_subplot(1, 1, 1)

axes02.scatter(tips.total_bill, tips.tip)
axes02.set_title('Scatterplot of Total Bill vs Tip')
axes02.set_xlabel('Total Bill')
axes02.set_ylabel('Tip')

plt.show()

# Sex 를 기준으로 tip 에 대해 boxplot 을 그린다. boxplot([열1의 값, 열2의 값], 라벨)
boxplot = plt.figure()
axes03 = boxplot.add_subplot(1, 1, 1)

female = tips[tips.sex == 'Female']['tip']
male = tips[tips.sex == 'Male']['tip']

axes03.boxplot([female, male], labels=['Female', 'Male'])

axes03.set_xlabel('Sex')
axes03.set_ylabel('Tip')
axes03.set_title('Boxplot of Tips by Sex')

plt.show()

# 4가지 변수를 이용하여 산점도 그래프를 만든다.
# 문자열을 정수로 치환하는 함수를 만든다.
# Female이면 0, Male 이면 1
def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1

# sex_color 열을 추가하여 record_sex 메서드가 반환한 값을 데이터프레임에 추가한다.
tips['sex_color'] = tips.sex.apply(recode_sex)
print(tips.head())

# 산점도 그래프를 그린다.
scat_plot = plt.figure()
axes04 = scat_plot.add_subplot(1, 1, 1)
axes04.scatter(x=tips.total_bill,
               y=tips.tip,
               s=tips['size'] * 10,
               c=tips.sex_color,
               alpha=0.5)

axes04.set_title('Total Bill vs Tip Colored by Sex and Sized by Size')
axes04.set_xlabel('Total Bill')
axes04.set_ylabel('Tip')

plt.show()

# seaborn 라이브러리로 히스토그램을 그린다. distplot
# 1. subplots 메서드로 기본 틀을 만든다.
ax = plt.subplots()
# 2-1. distplot 으로 히스토그램을 그린다.
ax = sns.distplot(tips.total_bill)
# 3. 제목을 붙인다.
ax.set_title('Total Bill Histogram with Density Plot')
# 4. 그래프 출력
plt.show()
# 2-2. 밀집도 그래프를 제외한다. kde = False
ax = sns.distplot(tips.total_bill, kde=False)
# 3. 제목을 붙인다.
ax.set_title('Total Bill Histogram')
# 4. 그래프 출력
plt.show()
# 2-3. 밀집도 그래프만. hist = False
ax = sns.distplot(tips.total_bill, hist=False)
# 3. 제목을 붙인다.
ax.set_title('Total Bill Density')
# 4. x 축과 y 축 이름을 붙인다.
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
# 5. 그래프 출력
plt.show()
# 2-4. 양탄자 그래프 추가. rug=True
ax = sns.distplot(tips.total_bill, rug=True)
# 3. 제목을 붙인다.
ax.set_title('Total Bill Histogram with Density and Rug Plot')
# 4. x 축 이름을 붙인다.
ax.set_xlabel('Total Bill')
# 5. 그래프 출력
plt.show()

# Count 그래프 - countplot
axcount = plt.subplots()
axcount = sns.countplot('day', data=tips)
axcount.set_title('Count of days')
axcount.set_xlabel('Day of the week')
axcount.set_ylabel('Frequency')
plt.show()

# scatterplot - regplot
axscatter = plt.subplots()
axscatter = sns.regplot(x='total_bill', y='tip', data=tips)
axscatter.set_title('Scatterplot of Total Bill and Tip')
axscatter.set_xlabel('Total Bill')
axscatter.set_ylabel('Tip')
plt.show()
# 회귀선을 없애려면 fit_reg = False

# 산점도 그래프와 히스토그램을 동시에 - jointplot
joint = sns.jointplot(x='total_bill', y='tip', data=tips)
joint.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
joint.fig.suptitle('Joint Plot of Total Bill and Tip')
plt.show()
# 육각 그래프 - kind = 'hex'
jointhex = sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
jointhex.set_axis_labels(xlabel = 'Total Bill', ylabel = 'Tip')
jointhex.fig.suptitle('Joint Plot of Total Bill and Tip')
plt.show()

# 이차원 밀집도 - kdeplot
axkde = plt.subplots()
axkde = sns.kdeplot(data=tips.total_bill, data2=tips.tip, shade=True)
axkde.set_title('Kernel Density Plot of Total Bill and Tip')
axkde.set_xlabel('Total Bill')
axkde.set_ylabel('Tip')
plt.show()

# 변수의 평균을 나타내는 바 그래프 그리기 - barplot
axbar = plt.subplots()
axbar = sns.barplot(x='time', y='total_bill', data=tips)
plt.show()

# 박스 그래프 - boxplot
axbox = plt.subplots()
axbox = sns.boxplot(x='time', y='total_bill', data=tips)
plt.show()

# 박스 그래프는 분산이 모호하게 표현됨. 박스 그래프에 커널 밀도를 추정한 바이올린 그래프 - violinplot
axviolin = plt.subplots()
axviolin = sns.violinplot(x='time', y='total_bill', data=tips)
plt.show()

# PairGrid
pair_grid = sns.PairGrid(tips)
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.displot, rug=True)
plt.show()

# 바이올린 그래프. 색상추가
axv = plt.subplots()
axv = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips)
plt.show()

axv1 = plt.subplots()
axv1 = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
plt.show()

# 산점도에 색상 추가
scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False)
plt.show()

# 산점도에 크기 추가 - 오류 발생
# scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False, scatter_kws={'s':tips['size']*10})
# plt.show()

# 산점도에 마크 변경
scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False, markers=['o', 'x'])
plt.show()

# anscombe
anscombe_plot = sns.lmplot(x='x', y='y', data=anscombe, fit_reg=False, col='dataset', col_wrap=2)
plt.show()

# FacetGrid 로 여러 그래프를 그리기
facet = sns.FacetGrid(tips, col='time')
facet.map(sns.distplot, 'total_bill', rug=True)
plt.show()

facet2 = sns.FacetGrid(tips, col='day', hue='sex')
facet2 = facet2.map(sns.regplot, 'total_bill', 'tip')
facet2 = facet2.add_legend()
plt.show()

facet3 = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet3 = facet3.map(sns.regplot, 'total_bill', 'tip')
plt.show()