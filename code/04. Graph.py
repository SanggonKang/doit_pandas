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