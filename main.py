# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import warnings
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.figure_factory as ff 
import plotly.express as px

warnings.filterwarnings("ignore")

# look for more information here https://docs.streamlit.io/library/cheatsheet
# adding title
st.title("Student Alcohol Consumption")


# adding description to your website
st.text('Introduction')
st.write('Student alcohol consumption has been a worry for many people. Students have many reasons why they consume alcohol. Which includes, friends, family, school, stress, boredom, and even the fear of missing out. Student alcohol consumption can have serious consequences. Through the recent years many students have consumed alcohol, or consuming it. It can be from 2 drinks, to 10. ')


# Thesis here
st.header('What We Wanted to Explore')
st.text('Our thesis and guiding ideas:')
st.write('We wanted to analyze how parental factors (parents income, educational level, parents living together) and academics (school types, school ratings, level of failures) impacts alcohol consumption. We were also looking for potential correlations between these factors.') 

# SHOWING THE DATA
# dataset Header
st.header('Dataset')

st.write("Our main question that we were trying to answer was if parental factors (parents income, educational level, parents living together) and academics (grades, school types, school ratings, level of failures) and alcohol consumption of students is correlated. The data set below had no 'N/A' fucnation. We determined this using the na code,'student_alc_df.isna().sum() Hence we chose to drop the columns that had data regarding romantic relationships, reason for why their school was chosen, if they had attended nursery school, and travel time to school, as this wasn't what we were looking for correlated factors")

# adding our dataset
student_alc_df = pd.read_csv("student-mat.csv")
columns_to_drop = ['romantic', 'reason', 'traveltime', 'nursery']
student_alc_df = student_alc_df.drop(columns_to_drop, axis=1, inplace = False)
student_alc_df["Total alc"] = student_alc_df['Dalc'] + student_alc_df['Walc']


# showing dataset
st.table(student_alc_df.head())
st.write("This dataset comes a from a secondary school math class' students and parents. You can read more about this dataset here: https://www.kaggle.com/datasets/uciml/student-alcohol-consumption?resource=download")

#st.write("The data set above had no 'N/A' fucnation. We determined this using the nacode,'student_alc_df.isna().sum() So looking at our thesis, we had taken away unnessacy columns that weren't in relaton to the data we were looking for. These columns were romatic, reason, traveltime, and nursery.") 
#(this is already written in the beginning)

st.header("Total Alcohol Consumption")
st.write("""There were two different times for drinking alcohol in the data set. Weekend drinking and Workday drinking. The Dalc (workday) and Walc (weekend) alcohol consumption were added in order to compare other columns to a total alcohol consumption. This code had been applied in order to carry out the process:
new_student_alc_df["Total alc"] = new_student_alc_df['Dalc'] + new_student_alc_df['Walc']
new_student_alc_df.""")

st.markdown("""---""")
st.write('We our going to begin our data, with a visulization of a correlation matrix, to get an idea of relationships between different features of our data.')
# correlation matrix
# Select numerical columns
numerical_columns = student_alc_df.select_dtypes(include=['int64', 'float64']).columns
# Create new DataFrame with numerical columns only
numerical_df = student_alc_df[numerical_columns]
# Calculate correlation matrix
corr_matrix = numerical_df.corr()
# making the heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(corr_matrix, annot = True, fmt = ".2f")

# titled our plot using matplotlib
plt.title("Student alcohol consumption corrrelation matrix")
st.pyplot(plt.gcf())

st.write('Next, we are going to be looking at specific relations within student alcohol consumption, such as, Mother vs Father education, Total alcohol consumption, age, and much more.')

st.markdown("""---""")
#pie chart
st.header("Total Alcohol Comsumption: Pie Chart")
counts = student_alc_df["Total alc"].value_counts()
fig, ax = plt.subplots()
ax.pie(counts, labels = counts.index)
ax.set_aspect("equal")
plt.ylabel('Total Alcohol Consumption Level')
st.pyplot(fig)
#student_alc_df["Total alc"].value_counts().plot.pie()
#student_alc_df["Total alc"].value_counts()


st.markdown("""---""")
# getting into visualizations
st.header("Total Alcohol Comsumption")
fig, ax = plt.subplots()
sns.histplot(student_alc_df, x='Total alc')
st.pyplot(fig)
st.write('This histogram shows the a students alcohol comsumption and how drinks that they have had.')
#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
#adding graphs by images

st.markdown("""---""")
st.header('Mother education level vs the total alcohol consumption')
st.write('(numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)')
fig, ax = plt.subplots()
sns.lineplot(data=student_alc_df, x = 'Medu', y = 'Total alc',)
st.pyplot(fig)
st.write('As you can see here, above the line graph, we can come to a result that the less educated the mother is, the more likely they are to consume alcohol.')
st.write("The association demonstrated by the graphs indicates that student alcohol use is lower when the mother has a higher level of education. And Students typically consume more alcohol when the teacher isn't very well-educated. In addition to these, there were also fluctuation when the mother education levels were higher. ")



st.markdown("""---""")
st.header("Relationship between Father Education and the Student Alcohol Consumption")
fig, ax = plt.subplots()
sns.lineplot( data=student_alc_df, x = 'Fedu', y = 'Total alc')
st.pyplot(fig)
st.write("However, looking at the relationship between the Father's educational level and Studennt alcohol consumption, we can come to a result that the more educated the father is, the more likely they are to consume alcohol.")


st.markdown("""---""")
st.header("Total Alcohol Consumption in relation to Failures")
fig, ax = plt.subplots()
sns.histplot(student_alc_df, x = 'failures', hue = 'Total alc', palette = 'Set2')
plt.title("Failures vs Total alchol comsumption")
plt.xlabel('failures')
plt.ylabel('Total alc')
st.pyplot(fig)
st.write("Although it seems to be that students that don't fail drink more overall, lower scoring studeents individually drink more alcohol overall.This could show that students that often drink alcohol tend to perform worse in schools")

st.markdown("""---""")
#adding graphs by making plotly_Chart
# Plot!
#sns.scatterplot(student_alc_df, x='Medu', y='Total alc')
fig = px.scatter(student_alc_df, x='Medu', y='Total alc')
st.plotly_chart(fig)
st.write(" Students with mothers that have no education at all drink less alcohol overall, meanwhile students with mother that have some type of eduction show similar results of total alcohol consumption.")
#use_container_width=True)
#st.text('Discription')



st.markdown("""---""")
st.header("Student age to total alcohol consumption")
fig, ax = plt.subplots()
x_axis = student_alc_df['age']
y_axis = student_alc_df['Total alc']
plt.bar(x_axis, y_axis)
plt.xlabel('age')
plt.ylabel('total alcohol consumption')
plt.show()
st.pyplot(fig)
st.write("Students ages 19 and 21 have the lowest alcohol consumption and 20 year olds drink less compared to other ages. The other ages drink the same amount of alcohol.")


st.markdown("""---""")
st.header("Looking at the correlation between alcohol comsumption in grades")
fig, ax = plt.subplots()
sns.distplot(student_alc_df[student_alc_df['Total alc'] < 5]['G3'])
plt.xlabel('G3')
plt.ylabel('Total alc')
plt.title("Looking at the correlation between low alcohol consumption in grades")
st.pyplot(fig)
st.write("This graph shows students only with less than 5 total alcohol consumption and shows student that drink alot of alcohol tend to score around 10/20 and there is an abscence of alcohol drinkers with a high mark.")


fig, ax = plt.subplots()
sns.distplot(student_alc_df[student_alc_df['Total alc'] >= 5]['G3'])
plt.xlabel('G3')
plt.ylabel('Total alc')
plt.title("Looking at the correlation between high alcohol consumption in grades")
st.pyplot(fig)
st.write("This graph shows students only with alcohol consumption greater of equal to 5. This also shows the same pattern of no alcohol drinkers achieving high marks.")

st.markdown("""---""")
#Scatter matrix
st.header("Scatter Matrix")
numerical_student_alc_df = student_alc_df[['health','absences','famrel','goout', 'Total alc']]
fig = px.scatter_matrix(numerical_student_alc_df)
st.plotly_chart(fig)


st.markdown("""---""")

#adding conclusions
st.header('Conclusion')

#st.write('Write a paragraph about some of the conclusions you can make from the visualizations, relate it back to how it answers the thesis')
st.write("From the graphs and other visual representations, there seems to be a pattern where alcohol consumption affects the grade they are achieving. A factor that caused these behaviour could be correlated to parental influence. Referring to the thesis, there is relationship we are able to establish from analyzing this dataset.")

#st.write('Write a paragraph about some of the things you learned through making the notebook and dashboard, like what new tools, languages, and libraries you can use and what you can do now')
st.write("We have learned a lot of new and different Python tools so far this week, like learning the fundamentals to producing various images. We were able to analyze  data table(s) of our choosing thanks to the tools, languages, and libraries. In the notebooks we were able to learn about panda, seaborn, myplot.lib and many more. We were also able to learn about strings, floats, and boolean. All of these skills we learned had allowed us to create and present our analyzations for our data set. ")

#st.write("write a little about things you thought went well and things you could implement better if there was time")
st.write("We believe that something that went well, was learning python, and understanding how to use it proper.Another thing that we believe that went when was learning about the visualizations, and making graphs, charts, and finding info from the graph. Also implicating us in our final project. Something that we believed that could have been implemented better if there was time could be to add all the information that we had. Like how we could figure out there were N/A values in our chart, and more.")
