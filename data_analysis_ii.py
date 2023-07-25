# -*- coding: utf-8 -*-
"""Data-Analysis_II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yxEHyyXzOwEq38p1DcL1z3uR3vVrCpK6

#**EXPLORATORY DATA ANALYSIS (EDA)**


##Kategorik ve Sayısal Değişken Analizi

**Genel Resmi Görmek**
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
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

df.head()

df.tail()

df.shape

df.info()

df.columns

df.index

df.describe().T

df.isnull().values.any()

df.isnull().sum()

def look_data(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

look_data(df)

df = sns.load_dataset("tips")

look_data(df)

"""**Kategorik ,Sayısal ve Kardinal Değişkenleri Yakalama**"""

titanic_df = sns.load_dataset("titanic")


# Kategorik değişkenleri yakalama
categorical_vars = titanic_df.select_dtypes(include=['object'])
print("Kategorik Değişkenler:")
print(categorical_vars.head())

# Sayısal değişkenleri yakalama
numeric_vars = titanic_df.select_dtypes(include=['int64', 'float64'])
print("\nSayısal Değişkenler:")
print(numeric_vars.head())

# Kardinal değişkenleri yakalama (Kategorik değişkenler arasından tekil değer sayısı 10'dan fazla olanlar)
cardinal_vars = [col for col in categorical_vars.columns if categorical_vars[col].nunique() > 20]
print("\nKardinal Değişkenler:")
print(categorical_vars[cardinal_vars].head())

"""**Hedef Değişken Analizi**"""

survived_analysis = titanic_df.groupby('survived').agg({
    'pclass': 'mean',
    'age': ['mean', 'median'],
    'fare': ['mean', 'median'],
    'sibsp': 'sum',
    'parch': 'sum'
})

survived_analysis

"""**Korelasyon Analizi**"""

# Korelasyon matrisini hesaplama
correlation_matrix = titanic_df.corr()

# Korelasyon matrisini görselleştirme
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Korelasyon Matrisi')
plt.show()