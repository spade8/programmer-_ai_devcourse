import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


house_df = pd.read_csv("1st_monthly_project/streamlit_proj/train.csv")
sns.scatterplot(x = 'SalePrice',y = 'TotalBsmtSF', data = house_df)
plt.show()

# fig = plt.figure(figsize=(10,10))
# sns.scatterplot(x = 'SalePrice',y = 'TotalBsmtSF', data = house_df)
# st.pyplot(fig)



#LotFrontage LotArea OverallQual OverallCond YearBuilt CentralAir



# GrLivArea













