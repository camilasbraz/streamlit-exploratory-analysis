import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from st_aggrid import AgGrid
import time
# Create a Streamlit app
st.title("Exploratory Data Analysis: report generator")

with st.sidebar.expander("About this app"):
    st.write(
        "EDA Analysis automatized using Streamlit and the ydata_profiling package.\n\n"
        "Source code here: [GitHub Repository](https://github.com/camilasbraz/streamlit-exploratory-analysis)\n\n"
        "Contact: [camilabraz03@gmail.com](mailto:camilabraz03@gmail.com)\n\n"
        "Application and code under the MIT License"
    )

st.sidebar.title("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check the file extension
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "csv":
        # Read CSV file
        df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
        # Read Excel file
        df = pd.read_excel(uploaded_file)


    columns_to_analyze = st.sidebar.radio(
        'Select wheter to include all columns in the report or a subset of columns.',
        ('All columns', 'Subset columns'))
    
    if columns_to_analyze == 'All columns':
        df = df
    elif columns_to_analyze == 'Subset columns':
        column_list = list(df.columns)
        columns_subset = st.sidebar.multiselect(
            'Select what to include in the report.',
            column_list
        )
        df = df[columns_subset]
    
    mode_choice = st.sidebar.radio(
        'Select analysis mode:',
        ('Minimal Mode', 'Complete Mode')
    )

    if mode_choice == 'Minimal Mode':
        mode = 'minimal'
    elif mode_choice == 'Complete Mode':
        mode = 'complete'
        st.sidebar.warning("The Complete Mode, which includes more detailed analysis and visualizations, can be resource-intensive and may not work efficiently on very large datasets")


    with st.sidebar.expander("Advanced Options"):
        sensitive_info = st.checkbox("Handle sensitive information?")
        schema = st.checkbox("Load JSON dataset type schema?")
        if schema:
            schema_json = st.sidebar.file_uploader("Upload JSON dataset type schema file", type=["json"])
        desc = st.checkbox("Load JSON column descriptions?")
        if desc:
            desc_json = st.sidebar.file_uploader("Upload JSON column descriptions file", type=["json"])

    
    # Display the raw data
    st.subheader("Data Content")
    grid = AgGrid(
        df)
    
    if st.button('Generate Report'):

        # grid_df = grid=['data']
        
        # df = pd.DataFrame(grid_df)
        # Create a Pandas Profiling report
        st.markdown("### EDA Report")

        # Create a dynamic progress bar
        progress_bar = st.empty()
        progress_percent = 0
        title = uploaded_file.name.split(".")[0].capitalize()  + "| EDA Report"
        # Step 1: Profile the data
        # st.write("Profiling the data...")

        profile = ProfileReport(
            df,
            explorative=True,
            title=title,
            mode=mode,
            duplicates=None if sensitive_info else 'raise',  
            samples=None if sensitive_info else {'head': 5}, 
            sensitive=sensitive_info, 
            schema=schema_json if schema else None,
            descriptions=desc_json if desc else None
        )

        progress_percent += 15
        progress_bar.progress(progress_percent)

        # Step 2: Render the report to HTML
        # st.write("Rendering the report to HTML...")
        # st.write("This may take some time depending on the data size.")
        export_html = profile.to_html()
        progress_percent += 70
        progress_bar.progress(progress_percent)

        # Final progress update
        progress_percent = 100
        progress_bar.progress(progress_percent)

        # Step 4: Provide the option to download the HTML report
        st.markdown("##### You can now download the complete EDA report:")
        title_html = uploaded_file.name.split(".")[0].capitalize()  + "_EDA_Report" + '.html'
        st.download_button(label="Download Report", data=export_html, file_name=title_html)

else:
    st.warning("Plase upload your CSV or XLSX file.")
