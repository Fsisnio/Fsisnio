import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# CSS to inject contained in a multiline string
custom_css = """
    <style>
        .title {
            color: #f63366;
            font-size: 24px;
            text-align: center;
        }
        .overview {
            font-size: 18px;
            margin-top: 20px;
        }
        .data-table {
            margin-top: 20px;
        }
        /* Additional custom CSS can go here */
    </style>
"""

# Inject custom CSS with markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Assume 'df' is loaded from your Excel file
# df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")

# Rest of your Streamlit app code goes here
# Use the custom CSS classes in markdown
st.markdown('<div class="title">Welcome to the Health Data Accessibility Page</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="overview">
        we present the participant opinions on personnal health data accessibility  accross countries by gender and age.
    </div>
""", unsafe_allow_html=True)

df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")



# Calculating the proportion of data sharing systems by gender
data_sharing_proportion = df.groupby('pays')['accès_aux_données'].value_counts(normalize=True).unstack().fillna(0) * 100
fig, ax = plt.subplots()
# Streamlit title
st.write("## Accessibility to Personnal Health Data by Country.")
st.markdown("""
Each country is listed on one axis, and participant opinions about  data accessibility plotted on the other. The intensity of colors indicates the level of access to personal health data by the participant of the campaign. This visualization enables quick identification of patterns and outliers, offering insights into global disparities in health data access. By comparing countries side-by-side, stakeholders can identify areas needing improvement and foster discussions on policies to enhance data availability for better health outcomes
""")

# Creating a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data_sharing_proportion, annot=True, cmap='coolwarm', fmt=".1f", cbar_kws={'label': 'Proportion (%)'}, ax=ax)

# Adding descriptive titles and labels
plt.title('Data Sharing System within Hospital by Gender')
plt.xlabel('Data Sharing System')
plt.ylabel('Gender')

# Display the plot in Streamlit
st.pyplot(fig)







# Assuming 'df' is your DataFrame

# Calculating the proportion of data sharing systems by gender
data_sharing_proportion = df.groupby('genre')['accès_aux_données'].value_counts(normalize=True).unstack().fillna(0) * 100
fig, ax = plt.subplots()
# Streamlit title
st.write("## Accessibility to Personnal Health Data by Gender")
st.markdown("""
It visualizes the disparity in personal data access across genders. It employs color gradients to depict varying levels of access, ranging from minimal to extensive, across different categories or time periods. Each row represents a gender, and each column corresponds to a specific category or time, with the color intensity indicating the level of access. This graphical representation helps identify patterns or inequalities in data access between genders, offering insights into potential areas for improvement or further investigation to ensure equitable access to personal data.
""")
# Creating a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data_sharing_proportion, annot=True, cmap='coolwarm', fmt=".1f", cbar_kws={'label': 'Proportion (%)'}, ax=ax)

# Adding descriptive titles and labels
plt.title('Data Sharing System within Hospital by Gender')
plt.xlabel('Data Sharing System')
plt.ylabel('Gender')

# Display the plot in Streamlit
st.pyplot(fig)





# Assuming 'df' is your DataFrame

# Calculating the proportion of data sharing systems by gender
data_sharing_proportion = df.groupby('Age')['accès_aux_données'].value_counts(normalize=True).unstack().fillna(0) * 100
fig, ax = plt.subplots()
# Streamlit title
st.write("## Accessibility to Personnal Health Data by age ")
st.markdown("""
The heatmap  represents the variation in access levels to personal health data across different age groups. Each cell in the heatmap corresponds to a specific age group and indicates the degree of accessibility through varying colors. The vertical axis categorizes individuals by age groups, and the horizontal axis could represent different metrics or conditions affecting access. This visualization aids in quickly identifying age-related trends or disparities in accessing personal health data, highlighting areas where improvements may be necessary to ensure equitable access for all age groups
""")
# Creating a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data_sharing_proportion, annot=True, cmap='coolwarm', fmt=".1f", cbar_kws={'label': 'Proportion (%)'}, ax=ax)

# Adding descriptive titles and labels
plt.title('Data Sharing System within Hospital by Gender')
plt.xlabel('Data Sharing System')
plt.ylabel('Gender')

# Display the plot in Streamlit
st.pyplot(fig)









# Assuming 'df' is your DataFrame

# Calculating the proportion of data sharing systems by gender
data_sharing_proportion = df.groupby('year')['accès_aux_données'].value_counts(normalize=True).unstack().fillna(0) * 100
fig, ax = plt.subplots()
# Streamlit title
st.write("## Accessibility to Personnal Health Data by year ")
st.markdown("""
The heatmap represents the level of accessibility for a given year, with color intensity indicating higher or lower access levels.
""")
# Creating a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data_sharing_proportion, annot=True, cmap='coolwarm', fmt=".1f", cbar_kws={'label': 'Proportion (%)'}, ax=ax)

# Adding descriptive titles and labels
plt.title('Data Sharing System within Hospital by Gender')
plt.xlabel('Data Sharing System')
plt.ylabel('Gender')

# Display the plot in Streamlit
st.pyplot(fig)









with st.expander('About', expanded=True):
    st.write('''
        - Data: Self Generated Data
        - Purpose: This is a suggestion to any intersted NGO/Company. It is customable
        - Author: Spéro FALADE
        - Contact: faladespero1@gmail.com
        - LinkedIn:https://www.linkedin.com/in/sp%C3%A9ro-falade-977180103/
        - Target: Make the dashboard User Friendly.        
    ''')



