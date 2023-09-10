# Stramlit exploratory analysis app with ydata profiling: EDA Tool by Camila Braz

This is a Streamlit application that allows you to perform automated Exploratory Data Analysis (EDA) on datasets loaded from CSV or Excel files. The app has been developed using the `ydata_profiling` package to generate detailed EDA reports.

[Cool datasets](https://www.springboard.com/blog/data-science/15-fun-datasets-to-analyze/)

## Access the Application

You can access the online application [here](https://eda-automatic-analysis.streamlit.app/).

## Usage

1. Access the application using the provided link above.
2. In the left sidebar, upload your CSV or Excel file.
3. Choose whether you want to include all columns in the report or select a subset of them.
4. Select the analysis mode: "Minimal" or "Complete."
5. If desired, check the "Handle sensitive information" option to deal with sensitive data.
6. If desired, check the "Load JSON dataset type schema" option and upload a JSON schema file.
7. Click the "Generate Report" button to initiate the analysis.
8. Wait for processing and report generation.
9. Download the generated report by clicking the "Download Report" button or visualize it on the application page.

<!-- https://ydata-profiling.ydata.ai/docs/master/pages/getting_started/concepts.html -->

Available types in json type schema are: Numerical should be Numeric, Categrorical, Booelan and DateTime. There is also the unsupported type.
You don´t dave to especify all columns types, the program can infer this.

<!-- ```python
from ydata_profiling.model.typeset import ProfilingTypeSet
typeset = ProfilingTypeSet()
typeset.plot_graph(dpi=100)

``` -->

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis, often abbreviated as EDA, is an essential process in data analysis. It involves a set of techniques and practices for summarizing, visualizing, and understanding data before formal statistical or machine learning modeling is applied. The primary goals of EDA are as follows:

1. **Understand the Data**: The primary objective of EDA is to understand the data at a deeper level. This involves examining the structure, nature, and characteristics of the data. It's important to grasp key properties of the data such as its distribution, trends, patterns, and outliers.

2. **Identify Patterns**: EDA helps in identifying patterns, trends, and relationships in the data. This can include detecting seasonality, correlations between variables, anomalous behaviors, and other insights that can be useful for making informed decisions.

3. **Detecting Missing Values and Inconsistencies:** During EDA, it's possible to identify missing values, outliers and inconsistencies in the data. Addressing these issues is crucial to ensure that subsequent analyses are accurate and reliable.

4. **Selecting Relevant Variables:** EDA assists in selecting the most relevant variables for analysis. This may involve identifying variables that have a strong influence on the desired outcomes and eliminating redundant or irrelevant variables.

5. **Assessing Data Quality:** EDA allows for an assessment of data quality by checking if the data meets the criteria of integrity, consistency, and reliability required for subsequent analyses.

6. **Data Preparation:** During EDA, it's common to perform data cleaning and transformation, preparing the data for more advanced analyses such as statistical modeling or machine learning.

7. **Hypothesis Generation:** EDA often leads to the generation of hypotheses that can be tested later through more formal statistical analyses. This helps in directing the investigation and exploring specific aspects of the data.

8. **Communicating Results:** EDA also plays an important role in communicating results to stakeholders. Data visualizations and descriptive summaries generated during EDA can help make insights more comprehensible and accessible to a non-technical audience.

In essence, EDA is a crucial step that sets the foundation for data-driven decision-making and modeling.

## Streamlit

Streamlit is an open-source Python library that allows the creation of web applications for data science and machine learning with minimal effort. It is designed to make it easy for data scientists and engineers to turn data scripts into shareable web apps. Streamlit is known for its simplicity and quick development cycle, making it a popular choice for creating interactive data dashboards and prototypes.

## Usage

1. Clone this repository to your local machine
2. Navigate to the directory
3. Run on terminal:

```terminal
python -m venv venv
venv\Scripts\activate
pip3 install -r requirements.txt
streamlit run app.py
```

4. Enjoy

## License

Licensed under the MIT LICENSE.

#### Future work:

- [Comparing Datasets](https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/comparing_datasets.html): Explore the documentation on comparing datasets using ydata_profiling.

- [Custom Report Appearance](https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/custom_report_appearance.html): Investigate customizing the appearance of the generated EDA reports using ydata_profiling.

- [Settings](https://ydata-profiling.ydata.ai/docs/master/pages/advanced_usage/available_settings.html): Investigate more settings.
