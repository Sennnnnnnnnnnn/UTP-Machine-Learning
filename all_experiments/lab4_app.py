import streamlit as st
import pandas as pd
import altair as alt

# Data
df = pd.DataFrame({
    "Age": [23, 35, 44, 55, 31, 45, 36, 22, 32, 27, 33, 44],
    "Income": [35000, 88000, 60000, 80000, 37000, 75000, 54000, 29000, 82000, 36000, 61000, 63000],
    "Education": ["High School", "Bachelors", "Masters", "PhD", "High School", "Masters",
                  "Bachelors", "High School", "Bachelors", "High School", "Bachelors", "Masters"],
    "Occupation": ["Salesman", "Doctor", "Artist", "Scientist", "Teacher", "Engineer",
                   "Artist", "Clerk", "Doctor", "Teacher", "Engineer", "Scientist"],
})

st.title("Exploratory Graphics vs Presentation Graphics")

# 1. Exploratory: interactive scatter plot
st.header("Exploratory Graphics: Interactive Scatter Plot")
scatter = alt.Chart(df).mark_circle(size=60).encode(
    x="Age", y="Income", color="Education",
    tooltip=["Age", "Income", "Education", "Occupation"],
).interactive()
st.altair_chart(scatter, use_container_width=True)
st.write("Hover over a point to see its age, income, education and occupation. Scroll to zoom and drag to pan.")

# 2. Presentation: static bar chart
st.header("Presentation Graphics: Static Bar Chart")
bar = alt.Chart(df).mark_bar().encode(
    x="Education", y="sum(Income)", color="Education",
)
st.altair_chart(bar, use_container_width=True)
st.write("A static chart with one clear message: total income by education level.")

# 3. Linked highlighting
st.header("Interactive Linked Highlighting for High-Dimensional Data")
highlight = alt.selection_point(on="mouseover", fields=["Education"], nearest=True)
color = alt.condition(highlight, "Education", alt.value("lightgray"))

linked_scatter = alt.Chart(df).mark_circle(size=60).encode(
    x="Age", y="Income", color=color,
    tooltip=["Age", "Income", "Education", "Occupation"],
).add_params(highlight)

linked_bar = alt.Chart(df).mark_bar().encode(
    x="Education", y="sum(Income)", color=color,
).add_params(highlight)

st.altair_chart(linked_scatter | linked_bar, use_container_width=True)
st.write("Hover over an education level in either chart to highlight the matching data in the other.")

# 4. Occupation counts with education context
st.header("Finding Appropriate Graphics and Linking Multivariate Context")
occupation = alt.Chart(df).mark_bar().encode(
    x="Occupation", y="count()", color="Education",
    tooltip=["Occupation", "Education", "count()"],
).interactive()
st.altair_chart(occupation, use_container_width=True)
st.write("A count bar chart suits a categorical variable; colour keeps education level as context.")