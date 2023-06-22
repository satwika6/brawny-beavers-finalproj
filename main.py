#import libraries
import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff 

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Student Alcohol Consumption")

#adding discription to your website
st.text('Description')
st.text('Student alcohol consumption has been a worry for many people. Students have many reasons why they consume, alcohol. Which includes, friends, family, stress, borefom, and even the fear of missing out.   ')

#Thesis here
st.header('Thesis')
st.text('analyze how parental factors (parents income, educational level, parents living together) and academics (school types, school ratings, level of failures) impacts alcooh')

#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
student_alc_df = pd.read_csv("student-mat.csv")

#showing dataset
st.table(student_alc_df.head())
st.text('This dataset data comes a from a secondary school mathclass for students.')

#Adding images to make your streamlit look visually better!
st.image('pro.png')
st.text('You can add photos with descriptions')

#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
# correlation matrix
corr_matrix = new_student_alc_df.corr()

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
