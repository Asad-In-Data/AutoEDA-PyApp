import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# from streamlit_extras.add_vertical_space import add_vertical_space
# from streamlit_extras.badges import badges, get_badges
# Uncomment the above imports if you have the streamlit_extras library installed

st.set_page_config(page_title="EDA App ", layout="wide",page_icon=":bar_chart:")
st.title("Exporatory Data Analysis (EDA) App")
fileuploaded= st.file_uploader("Upload your data file", type=["csv", "xlsx"])
if fileuploaded is not None:
    if fileuploaded.name.endswith('.csv'):
        df = pd.read_csv(fileuploaded)
        st.write("Data uploaded successfully!")
        st.subheader("Data Preview")
        st.write("Slider to choose the number of rows to display")
        value= st.slider("Number of rows to display", min_value=1, max_value=100, value=10)
        st.dataframe(df.head(value))
        st.write("Choose the type of EDA")
        EDA_type=st.selectbox("Select EDA Type", ["Descriptive", "Exploratory", "Visual"])
        if st.button("Run EDA"):
          if EDA_type == "Descriptive":
            st.write("Descriptive EDA selected. Displaying basic statistics and data types.")
            st.subheader("Data Summary")
            st.write(df.describe() if 'df' in locals() else "No data available. Please upload a file.")
            st.write("Data Types:", df.dtypes)
            st.write("Data Shape:", df.shape)
            st.write("Columns:", df.columns.tolist())
          elif EDA_type == "Exploratory":
            st.write("Exploratory EDA selected. Displaying unique values and missing values.")
            st.write("Unique Values:", df.nunique())
            st.write("Missing Values:", df.isnull().sum())
          elif EDA_type == "Visual":
            st.write("Visual EDA selected. Displaying plots and charts.")
            st.subheader("Data Visualization")
            st.write("Choose the type of Columns to visualize")
            col_type = st.selectbox("Select Column Type", ["Numerical", "Categorical"])
            st.write("Plot type")
            plot_type = st.selectbox("Select Plot Type", ["Count Plot", "Bar Plot", "Violin Plot", "Box Plot"])
            if col_type == "Numerical":
              st.write("Displaying numerical columns")
              numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
              st.write("Numerical Columns:", numerical_cols)
              x_axis = st.selectbox("Select X-axis for plot", options=numerical_cols)
              y_axis = st.selectbox("Select Y-axis for plot", options=numerical_cols)
            elif col_type == "Categorical":
                st.write("Displaying categorical columns")
                categorical_cols = df.select_dtypes(include=[object]).columns.tolist()
                st.write("Categorical Columns:", categorical_cols)
                x_axis = st.selectbox("Select X-axis for plot", options=categorical_cols)
                y_axis = st.selectbox("Select Y-axis for plot", options=categorical_cols)
                plot_categorical_cols(                    df,
                    categorical_cols,
                    target_col=y_axis,
                    plot_type=plot_type.lower(),
                    figsize=(6, 3),
                    rotation=45,
                    palette=None,
                    show_labels=True,
                    label_type='count'
                )
                if len(categorical_cols) > 0:
                    for col in categorical_cols:
                        sns.countplot(data=df, x=col)
                        plt.title(f"Count Plot of {col}")
                        st.pyplot(plt)
                        plt.clf()

    elif fileuploaded.name.endswith('.xlsx'):
        df = pd.read_excel(fileuploaded)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
      # Display the first few rows of the uploaded data
    st.subheader("Column Selection")
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
else:
    st.write("Please upload a data file to get started.")

    # Here you can add the code to run the EDA



    # Here you can add the code to display the data
    # For example, you can use pd.read_csv() to read the data and st.dataframe() to display it
    # df = pd.read_csv("your_data_file.csv")
    # st.dataframe(df)



st.markdown("""
<div style="text-align: center;">
    <h3>Contact Us</h3>
    <p>If you have any questions or feedback, please contact us at <a href="mailto:asadalich56@gmail.com">
     <span style="vertical-align:middle; color:#C1A9A9; font-weight:bold; font-size:18px;">Contact</span> </a> </p>
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
                <img src="https://img.icons8.com/ios-filled/32/000000/domain.png" style="vertical-align:middle; margin-right:8px;"/>
                <span style="vertical-align:middle; color:#00B8A9; font-weight:bold; font-size:18px;">Website</span>
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
                <img src="https://img.icons8.com/ios-filled/32/000000/linkedin.png" style="vertical-align:middle; margin-right:8px;"/>
                <span style="vertical-align:middle; color:#00B8A9; font-weight:bold; font-size:18px;">LinkedIn</span>
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
                <span style="vertical-align:middle;color:#00B8A9; font-weight:bold; font-size:18px;">GitHub</span>
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


def plot_categorical_cols(
    df,
    categorical_cols,
    target_col,
    plot_type='countplot',
    figsize=(6, 3),
    rotation=45,
    palette=None,
    show_labels=False,
    label_type='count'):
    
    for col in categorical_cols:
        plt.figure(figsize=figsize)

        if plot_type == 'countplot':
            ax=sns.countplot(data=df, x=col, hue=target_col, palette=palette)

        elif plot_type == 'barplot':
            # barplot needs numeric y — here using value_counts
            temp = df.groupby([col, target_col]).size().reset_index(name='count')
            ax=sns.barplot(data=temp, x=col, y='count', hue=target_col, palette=palette)

        elif plot_type == 'violinplot':
            sns.violinplot(data=df, x=col, y=target_col, palette=palette)

        elif plot_type == 'boxplot':
            sns.boxplot(data=df, x=col, y=target_col, palette=palette)

        else:
            print(f"Plot type '{plot_type}' not supported.")
            continue

        if show_labels:
            # For each bar
            for p in ax.containers:
                labels = []
                for bar in p:
                    height = bar.get_height()
                    if height == 0:
                        labels.append("")
                        continue
                    if label_type == 'count':
                        labels.append(f'{int(height)}')
                    elif label_type == 'percent':
                        total = len(df)
                        percent = 100 * height / total
                        labels.append(f'{percent:.1f}%')
                    else:
                        labels.append(f'{int(height)}')

                ax.bar_label(p, labels=labels, label_type='edge', padding=2,
                             fontsize=8, color='black', weight='bold')
        plt.title(f"{col} vs {target_col}",weight='bold',fontsize=13,color='black')
        plt.xlabel(col,weight='bold')
        plt.ylabel(target_col,weight='bold')
        plt.xticks(rotation=rotation)
        plt.tight_layout()