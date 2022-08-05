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

# seaborn 라이브러리로 히스토그램을 그린다.
