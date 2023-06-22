#import libraries
import streamlit as st
import pandas as pd
import warnings
import seaborn as sns
import matplotlib.pyplot as plt 

warnings.filterwarnings("ignore")

#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff 

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Student Alcohol Consumption")


#adding discription to your website
st.text('Description')
st.write('Student alcohol consumption has been a worry for many people. Students have many reasons why they consume alcohol. Which includes, friends, family, school, stress, boredom, and even the fear of missing out. Student alcohol consumption can have serious consequences. Through the recent years many students have consumed alcohol, or consuming it. It can be from 2 drinks, to 10. ')

#Thesis here
st.header('Thesis')
st.write('analyze how parental factors (parents income, educational level, parents living together) and academics (school types, school ratings, level of failures) impacts alcooh')

#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
student_alc_df = pd.read_csv("student-mat.csv")
columns_to_drop = ['romantic', 'reason', 'traveltime', 'nursery']
student_alc_df = student_alc_df.drop(columns_to_drop, axis=1, inplace = False)
student_alc_df["Total alc"] = student_alc_df['Dalc'] + student_alc_df['Walc']

#showing dataset
st.table(student_alc_df.head())
st.text('This dataset data comes a from a secondary school mathclass students and parents.')

#Adding images to make your streamlit look visually better!
st.image('pro.png')

#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
st.write('We our going to begin our data, with a visulization of a correlation matrix, to get an idea of relationships between different features of our data.')
# correlation matrix
corr_matrix = student_alc_df.corr()
# making the heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(corr_matrix, annot = True, fmt = ".2f")
# titled our plot using matplotlib
plt.title("Student alcohol consumption corrrelation matrix")

#adding graphs by images
st.image('pasted image 0.png')
st.text('Discription about your graph and visualizations')

#adding graphs by making plotly_Chart
# Plot!
#st.plotly_chart(BostonHousing, use_container_width=True)
#st.text('Discription')

#adding conclusions
st.header('Conclusion')
st.text('add your conclusion here')
