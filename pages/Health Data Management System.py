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
st.markdown('<div class="title">Welcome to the Health Data Management Page</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="overview">
        Here , we present the health data management system accross countries by gender and age. We also present the Politician implication in Helath Data Management accross countries and by year.
    </div>
""", unsafe_allow_html=True)

df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")


# Load your DataFrame

# Streamlit title
st.write("## Data Management Sytem within Hospital")
st.markdown("""
The pie chart provides a visual representation of the distribution of different data management systems used across hospitals. Each slice of the pie indicates the proportion of hospitals utilizing a specific system, showcasing the diversity and prevalence of various solutions in the healthcare industry. This graphical tool aids in quickly identifying the most commonly adopted systems, as well as those that are less widespread. By analyzing the pie chart, stakeholders can gain insights into current trends in hospital data management practices, enabling informed decisions regarding technology adoption and integration for improved patient care and operational efficiency.
""")


# Sidebar to select country
selected_country = st.sidebar.selectbox('Select a country', df['pays'].unique())

# Filter dataframe for the selected country
df_country = df[df['pays'] == selected_country]
data_sharing_counts = df_country['data_management'].value_counts(normalize=True) * 100

# Pie chart for the selected country
fig, ax = plt.subplots()
ax.pie(data_sharing_counts, labels=data_sharing_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.coolwarm(np.linspace(0,1,len(data_sharing_counts))))
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title for the pie chart

# Display the plot in Streamlit
st.pyplot(fig)

st.write("## Data Sharing System Within Hospital")
st.markdown("""
The graph represents the distribution and prevalence of different data sharing systems utilized within hospital settings. Each bar in the graph corresponds to a specific data sharing system, with the height of the bar indicating the frequency or proportion of hospitals employing that particular system. Colors or patterns may differentiate the systems for clarity. This visualization aids in understanding the current landscape of data management and exchange practices in healthcare facilities.
""")
fig, ax = plt.subplots()
politician_involvement = df.groupby('pays')['data_sharing_system'].value_counts(normalize=True).unstack().fillna(0) * 100
politician_involvement.plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(10, 6), ax=ax)

# Adjustment for horizontal labels
ax.tick_params(axis='x', rotation=0)

# Adding descriptive labels and title
ax.set_title('Data Sharing System within hospital')
ax.set_xlabel('Country')
ax.set_ylabel('Proportion (%)')

# Loop through each patch (bar segment) in the plot for annotations
for bar in ax.patches:
    height = bar.get_height()
    if height > 0:  # Only annotate non-zero values
        ax.annotate(f'{height:.1f}%', 
                    (bar.get_x() + bar.get_width() / 2, bar.get_y() + height/2),
                    ha='center', va='center',
                    color='black', fontsize=8, rotation=0)

# Moving the legend to the right of the plot
ax.legend(title='Data Sharing System', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to make room for the legend
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)
# Calculating the proportion of data sharing systems by gender
data_sharing_proportion = df.groupby('year')['politician_implication'].value_counts(normalize=True).unstack().fillna(0) * 100
fig, ax = plt.subplots()
# Streamlit title
st.write("## Politician implication in Helath Data Management Advocacy")
st.markdown("""
The "Politician Implication in Health Data Management Advocacy" heatmap visually represents the level of engagement and involvement of politicians in advocating for effective health data management systems. Each cell within the heatmap indicates the intensity of political activity or support for data management initiatives across different periods. Colors range from cool to warm, denoting varying degrees of involvement - cooler colors suggest minimal participation, while warmer tones highlight areas with higher political engagement. This visualization aids in identifying patterns of political commitment, showcasing regions times where advocacy efforts are robust or lacking, thereby guiding strategic planning for future advocacy campaigns.
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
st.write("## Politician Involvement by Country")

st.markdown("""
The graph represents the varying degrees of political engagement across Benin, Senegal and Ivoiry Coast in advocating for health data management policies. Each bar denotes a specific country, with the height of the bar corresponding to the level of politician involvement in policy advocacy efforts. The graph aims to highlight the disparities or similarities in political commitment towards enhancing health data governance. By comparing these involvements side by side, viewers can quickly identify which countries are leading in political advocacy for health data management and which are lagging behind, thereby providing insights into global health data policy trend
""")

fig, ax = plt.subplots()


politician_involvement = df.groupby('pays')['politician_implication'].value_counts(normalize=True).unstack().fillna(0) * 100
politician_involvement.plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(10, 6), ax=ax)

# Annotate proportion on each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

# Adjusting the legend position to be outside the plot area
ax.legend(title='Politician Involvement', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust for horizontal labels and set labels and title
ax.tick_params(axis='x', rotation=0)
ax.set_title('Proportion of Politician Involvement by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Proportion (%)')

plt.tight_layout()  # Adjust layout to make room for the legend

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
