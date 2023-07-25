# -*- coding: utf-8 -*-
"""Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q-rlwQBv_XvQbIxuFAO-rDWh_K1qQ-F0

#**DATA ANALYSIS WITH PYTHON**

---

##NUMPY (Numerical Python extensions)

NumPy, Python programlama dili için bir kütüphanedir; büyük, çok boyutlu diziler ve matrisler için destek ekler ve bu dizilerde çalışacak geniş bir üst düzey matematiksel işlev koleksiyonu sunar. Veri bilimi için olmazsa olmazdır.Ayrıca Numpy bilmeden Makine ve Derin öğrenme algoritmalarına geçemezsiniz. Numpy ile çok fazla işlem yapılabilmekte.

numpy kütüphanesi np kısaltma adıyla aşağıdaki gibi eklenir:

***import numpy as np***

### **Numpy Array**

Arrayler’i bir çeşit veri depolama olarak görebilirsiniz. Numpy’nin veriyi kullanabilmesi için verileri ‘Array’ haline getirmeliyiz. Array’in ne olduğundan bahsetmedik değil mi ? Arrayler aslında birer matrislerdir. Listelerden farkı; Verimli veri depo etmeye ve yüksek seviyeden vektörel işlemler yapma imkanı sağlar. Listeler içindeki her bir elemanın veri tipini ayrı ayrı saklarken , Numpy tek tipte numpyarray olarak veri tipini saklayarak hızlı işlem hacmi sunar.
"""

import numpy as np

x = [2, 3, 4]
y = [2, 3, 4]

xy = []

for i in range(0, len(x)):
    xy.append(x[i] * y[i])

xy

x = np.array([ 2, 3, 4])
y = np.array([2, 3, 4])

x*y

"""Numpy Array oluşturmak"""

Data = [[1,2,3],[4,5,6],[7,8,9]]

# Datayı Array formuna çevirebilmek için
Array = np.array(Data)

Array

type(Array)

"""**Numpy işlemleri** (Attributes of Numpy Arrays)



"""

dizi = np.arange(0, 30, 3) #0 dan başlayıp 3 er artan 30 a kadar (30 dahil değil) dizi oluşturur.

dizi

a = np.random.randint(10, size=5) # 5 adet sıfır ile 10 arasında değer üretir.

np.zeros(10, dtype=int) # 10 adet 0 üretir

np.random.normal(10, 4, (3, 4)) # Ortalaması 10 standart sapması 4 olan 3 e 4 lük matris oluştur.

a.ndim #Boyut sayısı

a.shape # Boyut bilgisi / tek boyutlu içinde 5 tane eleman var /satır ve sütun sayısı

a.size #toplam eleman sayısı

a.dtype # veri tipi

"""**Reshape** (Yeniden şekillendirme)"""

b=np.random.randint(1, 10, size=9)

b

b=np.random.randint(1, 10, size=9).reshape(3, 3)

b

c = np.random.randint(1, 10, size=9)

c

c.reshape(3,3)

"""**Index Seçimi** (Index Selection)"""

a = np.random.randint(10, size=10)

a

a[0:6]

a[0]=12

a

n= np.random.randint(10, size=(3, 5))

n

n[0,0]

n[2,2]

n[2,3]

n[1,4]

"""satır ve sütunlara 1 er ekleyip koordinat değerine gidebilirsiniz."""

n[:,0] # satırların hepsini seç ancak sadece 0. sütünları seç

n[1,:] #Tüm sütunları seç ancak satırlarda 1. yi seç

n[0:2, 0:3]

"""**Fancy Index**"""

ar= np.arange(0, 30, 3)

ar

catch=[1,2,3] # Alınacak indexlerin seçimi

ar[catch]

"""**Conditions on Numpy**"""

import numpy as np

a=np.array([1,2,3,4,5])

"""Klasik döngü kullanarak"""

ab=[]

for i in a:
  if i<4:
    ab.append(i)

ab

"""Numpy ile"""

a[a<4]

a[a!=4]

a[a>=2]

"""**Mathematical Operations**"""

a/5

a*5/2

a**2

a-1

np.subtract(a, )

np.add(a, 1)

np.mean(a)

np.sum(a)

np.min(a)

np.max(a)

np.var(a)

"""#**PANDAS (Python for Data Analysis/ Panel Data)**

##Pandas Series
##Reading Data
##Quick Look at Data
##Selection in Pandas
##Toplulaştırma ve Gruplama(Aggregation & Grouping)
##Apply ve Lambda
##Birleştirme (Join) İşlemleri

Yükleme işlemi:

**pip install pandas**

**pip install pandas=versiyon**

**import pandas as pd**
"""

import pandas as pd

"""##**Pandas Series** (Tek Boyutlu DataFrame)

Tek boyutlu ve index bilgiisi barındıran veri tipidir. DataFrame ise çok boyutlu ve index bilgisi barındırır.
"""

s=pd.Series([23,45,67,3,102]) # içine liste veya farklı türde bir veri yapısı konularak pandas serisine çevrilir.

type(s)

s.index

s.dtype

s.size

s.ndim

s.values

type(s.values) # Python index bilgisiyle ilgilenmediğimizi anlar ve ndarray olarak ifadeyi bize döndürür.

s.head()

s.tail(2)

"""##**Veri Okuma** (Reading Data)

df = pd.read_csv("example1.csv")

df = pd.read_excel("example.xlsx")

pandas cheatsheetine bakınız.

##**Fast Look at Data**
"""

import pandas as pd
import seaborn as sns

df=sns.load_dataset("titanic")

df.head()

"""**Passenger ID**: Her bir yolcu için ayrı değer taşıyan ve Int64(Tamsayı) değerinde olan bir değişken.

**Survıved**: Ilgılı yolcunun hayatta kalıp kalmadığını gösterir. Float64 tipindedir.(1: Hayatta, 2 : Hayatta değil)

**Pclass** : Tamsayı değerli bir değişkendir ve yolcunun bilet sınıfını gösterir.

**Name**: Kategorik bir değişkendir. Yolcunun ismini gösterir.

**Sex** : Başka bir kategorik değişkendir. Yolcunun cinsiyetini gösterir.

**Age** : Float64 tipindeki değişken yolcunun yaşını gösterir.

**Sibsp** : İnt64 tipindeki değişken gemideki yolcunun kardeş ve eş sayısını gösterir.

**Parch**  : İnt64 tipindedir ve yolcunun çocuk sayısını, ebeveyn sayısını gösterir.

**Ticket**  : Kategorik değişken olak ticket değişkeni yolcunun bilet kodunu gösterir.

**Fare** : Tamsayı değerindeki fare değişkeni yolcunun bilete ödediği miktarı belirtir.

**Cabin** : Kategorik değişken olan cabin değişkeni yolcunun kabin numarasını gösterir.

**Embarked**: Son değişkenimiz olan embarked değişkeni kategorik bir değişken olup yolcunun gemiye binmiş olduğu güverte bilgisini taşır.

**Deck**: Güverte
"""

df.tail()

df.shape

df.info()

df.columns

df.index

df.describe()

df.describe().T

df.isnull()

df.isnull().values.any()

df.isnull().sum()

df["sex"].head()

df["sex"].value_counts()

"""**Selection Pandas**"""

df[0:13]

df.drop(0,axis=0).head()

delete_index=[1,2,3,4]

df.drop(delete_index,axis=0).head(8)

#df.drop(delete_index, axis=0, inplace=True)

"""**Değişken-index çevrimi**"""

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)

df = sns.load_dataset("titanic")

df.head()

"sex" in df # Değişken sorgulama

df["age"].head()

type(df["age"].head()) #değişken tipi pandas serisidir

type(df[["age"]].head()) # Değişken seçiminde dataframe olarak kalması istenirse çift parantez kullanılmalı

df[["age", "alive"]]

col_names = ["age", "sex", "alive"]

df[col_names]

df["age2"] = df["age"]**2

df["age3"] = df["age"] + df["age2"]

df.head()

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, df.columns.str.contains("age")].head()

df.loc[:, ~df.columns.str.contains("age")].head()

"""## **Loc ve İLoc**

**İloc**: integer based selection (string ifade girilemez.)

**loc**:label based selection
"""

df.iloc[0:4]

df.loc[0:4]

"""iloc,index işlemi olarak tanındı ve 4. index yani 3 dahil olmak üzere taşıdı. Ancak loc ifadesi 4 ü dahil olarak alır."""

df.iloc[0:4, 0:4]

df.loc[0:4,"sex"]

col_names=["sex","alive"]

df.loc[0:5, col_names]

"""**Koşullu Seçimler**"""

df[df["fare"]>20].head()

df[df["age"]<30]["age"].count()

df.loc[df["age"]<30, ["fare","class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
#birden fazla koşul parantez içine alınmalı

"""##Aggregation and Grouping"""

df = sns.load_dataset("titanic")

"""**Passenger ID**: Her bir yolcu için ayrı değer taşıyan ve Int64(Tamsayı) değerinde olan bir değişken.

**Survıved**: Ilgılı yolcunun hayatta kalıp kalmadığını gösterir. Float64 tipindedir.(1: Hayatta, 2 : Hayatta değil)

**Pclass** : Tamsayı değerli bir değişkendir ve yolcunun bilet sınıfını gösterir.

**Name**: Kategorik bir değişkendir. Yolcunun ismini gösterir.

**Sex** : Başka bir kategorik değişkendir. Yolcunun cinsiyetini gösterir.

**Age** : Float64 tipindeki değişken yolcunun yaşını gösterir.

**Sibsp** : İnt64 tipindeki değişken gemideki yolcunun kardeş ve eş sayısını gösterir.

**Parch**  : İnt64 tipindedir ve yolcunun çocuk sayısını, ebeveyn sayısını gösterir.

**Ticket**  : Kategorik değişken olak ticket değişkeni yolcunun bilet kodunu gösterir.

**Fare** : Tamsayı değerindeki fare değişkeni yolcunun bilete ödediği miktarı belirtir.

**Cabin** : Kategorik değişken olan cabin değişkeni yolcunun kabin numarasını gösterir.

**Embarked**: Son değişkenimiz olan embarked değişkeni kategorik bir değişken olup yolcunun gemiye binmiş olduğu güverte bilgisini taşır.

**Deck**: Güverte
"""

df["fare"].mean()

df.groupby("sex")["age"].mean()
#Cinsiyete göre grupla yaş değişkeninin ortalamasını al

df.groupby("sex").agg({"fare": "mean"})

df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "sibsp"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})

"""##**Pivot table**"""

df.pivot_table("survived", "sex", "sibsp")

df.pivot_table("survived", "sex", ["embarked", "class"],aggfunc="std")

df["cut_age"] = pd.cut(df["age"], [0, 20, 30, 40, 90])

df["cut_age"].head()

df.head()

"""**apply-lambda kullanımı**"""

df["age"].isnull().sum()

def fill_age(row):
    if pd.isnull(row['age']):
        return df['age'].mean()
    else:
        return row['age']

df['age'] = df.apply(lambda row: fill_age(row), axis=1)

df["age"].isnull().sum()

"""**Join işlemleri**"""

users = {
    'ID': [1, 2, 3],
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 28, 30]
}

users

purchases = {
    'ID': [1, 2, 3],
    'Product': ['Apple', 'Banana', 'Orange'],
    'Price': [1.0, 0.5, 0.8]
}

purchases

users_df = pd.DataFrame(users)
purchases_df = pd.DataFrame(purchases)

users_df

purchases_df

merged_df = users_df.merge(purchases_df, on='ID')

merged_df

"""Concat ile birleştirme"""

import numpy as np

v = np.random.randint(1, 20, size=(5, 3))

v

df1 = pd.DataFrame(v, columns=["var1", "var2", "var3"])

df1

df2=df1+10

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

?pd.concat