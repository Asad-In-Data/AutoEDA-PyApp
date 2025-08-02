import streamlit as st
import pandas as pd
import numpy as np
# from streamlit_extras.add_vertical_space import add_vertical_space
# from streamlit_extras.badges import badges, get_badges
# Uncomment the above imports if you have the streamlit_extras library installed

st.set_page_config(page_title="EDA App ", layout="wide",page_icon=":bar_chart:")
st.title("Exporatory Data Analysis (EDA) App")
st.sidebar.title("EDA App Sidebar")
st.sidebar.write("This is the sidebar of the EDA App")
st.sidebar.write("You can add more options here")   
st.write("For example, you can add a file uploader to upload your data")
fileuploaded= st.file_uploader("Upload your data file", type=["csv", "xlsx"])
if fileuploaded is not None:
    if fileuploaded.name.endswith('.csv'):
        df = pd.read_csv(fileuploaded)
        st.write("Data uploaded successfully!")
        st.write("Choose the type of EDA")
        EDA_type=st.selectbox("Select EDA Type", ["Descriptive", "Exploratory", "Visual"])
        if EDA_type == "Descriptive":
            st.write("Descriptive EDA selected. Displaying basic statistics and data types.")
            st.write(df.describe())
            st.write("Data Types:", df.dtypes)
        elif EDA_type == "Exploratory":
            st.write("Exploratory EDA selected. Displaying unique values and missing values.")
            st.write("Unique Values:", df.nunique())
            st.write("Missing Values:", df.isnull().sum())
        elif EDA_type == "Visual":
            st.write("Visual EDA selected. Displaying plots and charts.")
            st.bar_chart(df.select_dtypes(include=[np.number]).head())
    elif fileuploaded.name.endswith('.xlsx'):
        df = pd.read_excel(fileuploaded)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
    st.subheader("Data Preview")
    st.write("Slider to choose the number of rows to display")
    value= st.slider("Number of rows to display", min_value=1, max_value=100, value=10)
    st.dataframe(df.head(value))  # Display the first few rows of the uploaded data
    st.subheader("Data Summary")
    st.write(df.describe() if 'df' in locals() else "No data available. Please upload a file.")
    st.write("Data Shape:", df.shape)
    columns= df.columns.tolist()
    selected_columns = st.selectbox("Select columns to display", options=columns, index=0)
    st.dataframe(df[selected_columns].head())  # Display selected columns
    
    #Filtering data
    st.subheader("Data Filtering")
    filter_column = st.selectbox("Select column to filter", options=columns)
    unique_values = df[filter_column].dropna().unique()
    filter_value = st.selectbox("Enter value to filter by", options=unique_values, index=0)
    if filter_value:    
        filtered_df = df[df[filter_column].astype(str).str.contains(filter_value, na=False)]
        st.write("Filtered Data:")
        st.dataframe(filtered_df)

        st.subheader("Plots")
        x_axis = st.selectbox("Select X-axis for plot", options=columns)
        y_axis = st.selectbox("Select Y-axis for plot", options=columns)
        if x_axis and y_axis:
            st.bar_chart(filtered_df[[x_axis, y_axis]].set_index(x_axis))
            st.line_chart(filtered_df[[x_axis, y_axis]].set_index(x_axis))
            st.area_chart(filtered_df[[x_axis, y_axis]].set_index(x_axis))
        else:
            st.write("Please select valid columns for plotting.")   
    st.subheader("Data Insights")

    st.write("Data Types:", df.dtypes)  
    st.write("Missing Values:", df.isnull().sum())
    st.write("Unique Values:", df.nunique())
else:
    st.write("Please upload a data file to get started.")
    
    

st.write("You can also add a button to run the EDA")
if st.button("Run EDA"):
    st.write("Running EDA...")
    # Here you can add the code to run the EDA


st.sidebar.write("You can also add a checkbox to show/hide the data")
st.sidebar.checkbox("Show Data", value=True)
if st.sidebar.checkbox("Show Data"):
    st.write("Here is the data:")
    # Here you can add the code to display the data
    # For example, you can use pd.read_csv() to read the data and st.dataframe() to display it
    # df = pd.read_csv("your_data_file.csv")
    # st.dataframe(df)
st.sidebar.write("You can also add a text input to filter the data")
st.sidebar.text_input("Filter Data", placeholder="Enter filter criteria")   
st.sidebar.write("You can also add a date input to filter the data by date")
st.sidebar.date_input("Filter by Date") 
st.sidebar.write("You can also add a time input to filter the data by time")
st.sidebar.time_input("Filter by Time") 
st.sidebar.write("You can also add a multiselect to choose multiple options")
st.sidebar.multiselect("Select Options", ["Option 1", "Option 2", "Option 3"], default=["Option 1", "Option 2"])
st.sidebar.write("You can also add a radio button to choose one option")    
st.sidebar.radio("Select Option", ["Option A", "Option B", "Option C"])
st.sidebar.write("You can also add a progress bar to show the progress of the EDA")
st.sidebar.progress(50)  # Example progress bar at 50%
st.sidebar.write("You can also add a spinner to show that the EDA is running")
with st.spinner("Running EDA..."):
    # Simulate a long-running process
    import time
    time.sleep(2)  # Simulate a delay of 2 seconds
st.sidebar.write("You can also add a markdown text to display some information")
st.sidebar.markdown("### EDA App Information")
st.sidebar.markdown("This is a simple EDA app built with Streamlit. You can use it to explore your data and perform basic EDA tasks.")
st.sidebar.write("You can also add a code block to display some code")  
st.sidebar.code("""
import pandas as pd 
import numpy as np
from streamlit.components.v1 import html
# Example code block    
""")
st.sidebar.write("You can also add a table to display some data")
st.sidebar.table(pd.DataFrame({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]}))
st.sidebar.write("You can also add a chart to display some data")   
st.sidebar.line_chart(pd.DataFrame(np.random.randn(100, 2), columns=["Column 1", "Column 2"]))
st.sidebar.write("You can also add a map to display some data") 
st.sidebar.map(pd.DataFrame({
    "lat": [37.76, 37.77, 37.78],
    "lon": [-122.45, -122.46, -122.47]
}))
st.sidebar.write("You can also add a video to display some information")
st.sidebar.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Example video link
st.sidebar.write("You can also add an image to display some information")   
st.sidebar.image("https://via.placeholder.com/150", caption="Example Image")  # Example image link
st.sidebar.write("You can also add a file download button to download the data")
st.sidebar.download_button(
    label="Download Data",
    data=pd.DataFrame(np.random.randn(100, 2)).to_csv(),
    file_name="data.csv",
    mime="text/csv"
)   


st.markdown("""
<div style="text-align: center;">
    <h3>Contact Us</h3>
    <p>If you have any questions or feedback, please contact us at <a href="mailto:asadalich56@gmail.com">asadalich56@gmail.com</a></p>
</div>
<br>
""", unsafe_allow_html=True)
# Display three social links in a row with icons
col_link1, col_link2, col_link3 = st.columns(3)
with col_link1:
    st.markdown(
        '''
        <div style="display: flex; justify-content: center;">
            <a href="https://datz-asadanalyst.github.io/" target="_blank" style="text-decoration:none;">
                <img src="https://img.icons8.com/ios-filled/32/4285F4/domain.png" style="vertical-align:middle; margin-right:8px;"/>
                <span style="vertical-align:middle;">Website</span>
            </a>
        </div>
        ''',
        unsafe_allow_html=True
    )
with col_link2:
    st.markdown(
        '''
        <div style="display: flex; justify-content: center;">
            <a href="https://www.linkedin.com/in/datz-asad-analyst56" target="_blank" style="text-decoration:none;">
                <img src="https://img.icons8.com/ios-filled/32/FFD700/linkedin.png" style="vertical-align:middle; margin-right:8px;"/>
                <span style="vertical-align:middle; color:#FFD700; font-weight:bold; font-size:18px;">LinkedIn</span>
            </a>
        </div>
        ''',
        unsafe_allow_html=True
    )
with col_link3:
    st.markdown(
        '''
        <div style="display: flex; justify-content: center;">
            <a href="https://github.com/Datz-AsadAnalyst" target="_blank" style="text-decoration:none;">
                <img src="https://img.icons8.com/ios-filled/32/000000/github.png" style="vertical-align:middle; margin-right:8px;"/>
                <span style="vertical-align:middle;">GitHub</span>
            </a>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown("---")  
st.markdown(""" 
<div style="text-align: center;">
    <div style="font-size: 16px; color: #888;">
        <p>Made with ❤️ by Datz Asad Analyst</p>
        <p> © 2023 EDA App. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True) 

st.logo("logo.png", size= "Large")  # Streamlit does not have st.logo; remove or replace with st.image if needed
