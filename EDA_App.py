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
    elif fileuploaded.name.endswith('.xlsx'):
        df = pd.read_excel(fileuploaded)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
    st.write("Data uploaded successfully!")
    st.subheader("Data Preview")
    st.dataframe(df.head())  # Display the first few rows of the uploaded data
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
st.sidebar.write("You can also add a selectbox to choose the type of EDA")
st.sidebar.selectbox("Select EDA Type", ["Descriptive", "Exploratory", "Visual"])
st.sidebar.write("You can also add a slider to choose the number of rows to display")
st.sidebar.slider("Number of rows to display", min_value=1, max_value=100, value=10)
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
st.sidebar.write("You can also add a footer to the app")
st.sidebar.markdown("---")  
st.sidebar.markdown("### Footer")
st.sidebar.markdown("This is the footer of the EDA App. You can add more information here.")
st.sidebar.markdown("© 2023 EDA App. All rights reserved.") 
st.sidebar.write("You can also add a help section to the app")
st.sidebar.markdown("### Help") 
st.sidebar.markdown("If you need help using the EDA App, please refer to the documentation or contact support.")
st.sidebar.write("You can also add a contact section to the app")   
st.sidebar.markdown("### Contact")
st.sidebar.markdown("If you have any questions or feedback, please contact us at support@   edapp.com")
st.sidebar.write("You can also add a license section to the app")   
st.sidebar.markdown("### License")
st.sidebar.markdown("This app is licensed under the MIT License. You can use it for personal or commercial projects, but please give credit to the original author.")
st.sidebar.write("You can also add a disclaimer section to the app")        
st.sidebar.markdown("### Disclaimer")
st.sidebar.markdown("The EDA App is provided 'as is' without any warranties or  conditions of any kind, either express or implied. The author is not responsible for any damages or losses that may occur from using this app.")
st.sidebar.write("You can also add a changelog section to the app")
st.sidebar.markdown("### Changelog")    
st.sidebar.markdown("- Version 1.0: Initial release")
st.sidebar.markdown("- Version 1.1: Added new features and fixed bugs") 
st.sidebar.markdown("- Version 1.2: Improved performance and added more options")
st.sidebar.write("You can also add a credits section to the app")
st.sidebar.markdown("### Credits")
st.sidebar.markdown("This app was created by [Your Name](https://yourwebsite.com    ).")
st.sidebar.write("You can also add a link to your website or social media profiles")    
st.sidebar.markdown("[Your Website](https://yourwebsite.com)")
st.sidebar.markdown("[Your Twitter](https://twitter.com/yourprofile)")  
st.sidebar.markdown("[Your LinkedIn](https://linkedin.com/in/yourprofile)")
st.sidebar.markdown("[Your GitHub](https://github.com)")
st.sidebar.write("You can also add a section to display the app version")   
st.sidebar.markdown("### App Version")
st.sidebar.markdown("Version 1.0.0")
st.sidebar.write("You can also add a section to display the app author")
st.sidebar.markdown("### App Author")   
st.sidebar.markdown("Created by [Your Name](https://yourwebsite.com)")
st.sidebar.write("You can also add a section to display the app license")
st.sidebar.markdown("### App License")
st.sidebar.markdown("This app is licensed under the MIT License. You can use it for personal or commercial projects, but please give credit to the original author.")
st.sidebar.write("You can also add a section to display the app disclaimer")    
st.sidebar.markdown("### App Disclaimer")
st.sidebar.markdown("The EDA App is provided 'as is' without any warranties or conditions of any kind, either express or implied. The author is not responsible for any damages or losses that may occur from using this app.")

st.write("EDA App .... My first app")
st.write("This is the main page of the EDA App. You can use the sidebar to navigate through the app and explore different features.")
st.write("You can also add more pages to the app by creating new Python files and linking them in the sidebar.")
st.write("For example, you can create a page for data visualization, a page for data cleaning, or a page for machine learning.")
st.write("You can also add more features to the app by using Streamlit components and libraries.")
st.write("For example, you can use the `streamlit_extras` library to add vertical space, badges, or other components to enhance the app's functionality.")
st.write("You can also use the `streamlit` library to create interactive widgets, charts    , and maps to visualize your data.")
st.write("You can also use the `pandas` library to manipulate and analyze your data, and the `numpy` library to perform numerical operations.")
st.write("You can also use the `matplotlib` or `seaborn` libraries to create static or interactive visualizations of your data.")
st.write("You can also use the `plotly` library to create interactive plots and dashboards.")
st.write("You can also use the `altair` library to create declarative visualizations of your data.")
st.write("You can also use the `bokeh` library to create interactive visualizations and dashboards.")
st.write("You can also use the `dash` library to create web applications with Python.") 
st.write("You can also use the `streamlit` library to create web applications with Python.")
st.write("You can also use the `streamlit` library to create interactive dashboards and reports with Python.")
st.write("You can also use the `streamlit` library to create data applications with Python.")
st.write("You can also use the `streamlit` library to create machine learning applications with Python.")
st.write("You can also use the `streamlit` library to create data science applications with Python.")
st.write("You can also use the `streamlit` library to create data analytics applications with Python.")
st.write("You can also use the `streamlit` library to create data visualization applications with Python.")
st.write("You can also use the `streamlit` library to create data exploration applications with Python.")
st.write("You can also use the `streamlit` library to create data storytelling applications with Python.")

st.logo("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")
st.write("You can also use the `streamlit` library to create data journalism applications with Python.")