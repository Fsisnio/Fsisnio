import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pydeck as pdk
import numpy as np
# Page configuration
st.set_page_config(
    page_title="DOPM Campaign Dashboard",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state='auto')

alt.themes.enable("dark")

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
st.markdown('<div class="title">Welcome to the DOPM Online Campaign Dashboard</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="overview">
        This is a three (03) pages dashboard for a random DOPM online health system evaluation principle campaign from 2023 to 2024. 
        You can use the sidebar menu to navigate through pages or to interact with the graphics.
        You can also make use of the setting menu in the right upper corner of your screen to change colors 
        or the pages structure (wide or not). You can download the database as a csv file and all the graphics as well.
    </div>
""", unsafe_allow_html=True)


# Load the data from the Excel file
df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")

with st.sidebar:
    st.title('📈DOPM Dashboard')
    
    year_list = list(df['year'].unique())  # Corrected to access 'year' column in df
    year_list.sort(reverse=True)  # Sort the list in descending order
    
    selected_year = st.selectbox('Select a year', year_list)
    df_selected_year = df[df['year'] == selected_year]  # Corrected the filtering condition
    df_selected_year_sorted = df_selected_year.sort_values(by="pays", ascending=False)

# Sidebar for user inputs
st.sidebar.header("Filter options")
country = st.sidebar.multiselect('Select country:', options=df['pays'].unique())
age_range = st.sidebar.slider('Select age range:', min_value=int(df['Age'].min()), max_value=int(df['Age'].max()), value=(int(df['Age'].min()), int(df['Age'].max())))
gender = st.sidebar.multiselect('Select gender:', options=df['genre'].unique())

# Filtering the dataframe based on user selection
filtered_data = df[(df['pays'].isin(country) | (country == [])) &
                   (df['Age'].between(age_range[0], age_range[1])) &
                   (df['genre'].isin(gender) | (gender == []))]

# Display statistics

st.write("### Data Overview")
st.markdown("""
This table gives a summary of the collected data during the DOPM online campaign. We have 999 observations and tweleve variables.
""")
# Add a print option
st.write(filtered_data)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pydeck as pdk


# Continue with the rest of your app



# Load the data
df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")
df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude', 'genre': 'gender', 'country': 'pays'}, inplace=True)
st.write("### Country where we implement the project")
st.markdown("""
The campaign is conducted in three (03) west african countries : Benin, Senegal and Ivoiry Coast as showed by the following Map. you can zoom the map by clicking on the '- or +' in the right corner of the map
""")

# Assuming you have added a 'color' column based on 'pays' for color coding in the visualization
# For demonstration, let's define a simple color mapping based on 'pays'. 
# This requires that your dataframe already has a 'pays' column.
color_mapping = {
    'Benin': [255, 165, 0],  # Orange
    'Senegal': [0, 255, 0],  # Green
    'Côte d\'Ivoire': [0, 0, 255]  # Blue
}

# Apply color mapping to each row in the dataframe based on 'pays'
df['color'] = df['pays'].apply(lambda pays: color_mapping.get(pays, [200, 200, 200]))  # Default color if 'pays' not in mapping

# PyDeck visualization
# Define a PyDeck layer for rendering
layer = pdk.Layer(
    'ScatterplotLayer',     # Use a scatter plot layer
    df,
    get_position=['longitude', 'latitude'],
    get_color='color',      # Use the 'color' column for the color of markers
    get_radius=88000,        # Radius of each data point (in meters)
)

# Define the initial view state for the PyDeck map
view_state = pdk.ViewState(
    latitude=df['latitude'].mean(),
    longitude=df['longitude'].mean(),
    zoom=3.6,
    pitch=0,
)

# Create the PyDeck chart using the layer and view state defined above
r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v9')

# Display the PyDeck chart in Streamlit
st.pydeck_chart(r)










# Calculate the frequency (proportion) of each gender
gender_frequency = filtered_data['genre'].value_counts(normalize=True)
# Convert frequencies to percentages
gender_percentage = gender_frequency * 100

# Create a figure and a set of subplots
fig, ax = plt.subplots()
# Plot the frequencies as a bar chart using matplotlib
gender_percentage.plot(kind='bar', ax=ax, color=['skyblue', 'lightgreen', 'lightcoral'])

# Adjustment for horizontal labels
ax.tick_params(axis='x', rotation=0)
# Set the title and labels
st.write("### Gender Distribution")
st.markdown("""
The bar graph visually represents the comparative frequency or count of individuals across different genders within the DOPH dataset . Each bar's height indicates the  proportion of individuals that belong to a specific gender categor. The graph's X-axis categorizes genders, while the Y-axis quantifies the representation of percentages.
""")
ax.set_title('Gender Distribution')
ax.set_xlabel('Gender')
ax.set_ylabel('Percentage')

# Display percentages on top of the bars
for p in ax.patches:
    ax.annotate(f"{round(p.get_height(), 2)}%", (p.get_x() * 1.005, p.get_height() * 1.005))

# Use Streamlit to display the matplotlib figure
st.pyplot(fig)






st.write("## Gender Distribution by country")
st.markdown("""
The bar graph visualizes the comparison of gender ratios across different countries. Each bar represents a country, segmented into colored sections that denote the proportion of genders within that country. The height of each segment corresponds to the percentage of the population that identifies with a specific gender, allowing for an immediate visual comparison across the demographic landscape of the countries. This graphic effectively communicates the gender balance or imbalance within each country, providing insights into the diversity of gender representation. 
""")

fig, ax = plt.subplots()

df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")

politician_involvement = df.groupby('pays')['genre'].value_counts(normalize=True).unstack().fillna(0) * 100
politician_involvement.plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(10, 6), ax=ax)

# Annotate proportion on each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

# Adjusting the legend position to be outside the plot area
ax.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust for horizontal labels and set labels and title
ax.tick_params(axis='x', rotation=0)
ax.set_title('Comparative Gender Distribution by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Proportion (%)')

plt.tight_layout()  # Adjust layout to make room for the legend

st.pyplot(fig)




st.write("## Age Distribution By Country")
fig, ax = plt.subplots()
st.markdown("""

The bar graph  visually represents the distribution of age groups within different countries. Each bar corresponds to a specific country, and its height indicates the prevalence or count of individuals within specific age ranges. The graph segregates countries along the horizontal axis, ensuring each country is distinctly identifiable. Age ranges is represented through different colors within each country's bar, providing a clear visual distinction of age demographics. This graphical representation facilitates the comparison of age distribution patterns across countries, highlighting similarities or disparities in demographic compositions. 
""")

df = pd.read_excel(r"C:\Users\DELL\Documents\data.xlsx")

politician_involvement = df.groupby('pays')['Age'].value_counts(normalize=True).unstack().fillna(0) * 100
politician_involvement.plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(10, 6), ax=ax)

# Annotate proportion on each bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

# Adjusting the legend position to be outside the plot area
ax.legend(title='Age Range', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust for horizontal labels and set labels and title
ax.tick_params(axis='x', rotation=0)
ax.set_title('Comparative Age Distribution by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Proportion (%)')

plt.tight_layout()  # Adjust layout to make room for the legend

st.pyplot(fig)






# Assuming 'df' is your DataFrame

# Calculating the proportion of data sharing systems by gender
data_sharing_proportion = df.groupby('Age')['genre'].value_counts(normalize=True).unstack().fillna(0) * 100
fig, ax = plt.subplots()
# Streamlit title
st.write("## Age Distribution by Gender")
st.markdown("""
The "Age Distribution by Gender" bar graph visually represents the age distribution across different gender categories within our dataset. Each bar signifies a specific gender group, such as male, female, or other, and its height corresponds to the number of individuals or the percentage of the population within a certain age range. This graphical representation allows for easy comparison between genders, highlighting differences or similarities in age distribution. By examining the graph, one can quickly discern patterns, trends, or disparities among genders, providing insights into the demographic composition of the studied population.
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












