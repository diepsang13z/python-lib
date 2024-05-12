# pandas?
Pandas is a popular open-source data manipulation and analysis library for the Python programming language. It
provides a powerful and flexible set of tools for working with structured data, making it a fundamental tool for
data scientists, analysts, and engineers.

Pandas is designed to handle data in various formats, such as tabular data, time series data, and more, making it
an essential part of the data processing workflow in many industries.


# Data Structures:
Pandas offers two primary data structures - DataFrame and Series.

1. A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure
with labeled axes (rows and columns).
2. A Series is a one-dimensional labeled array, essentially a single column or row of data.

**Data Import and Export**: Pandas makes it easy to read data from various sources, including CSV files, Excel
spreadsheets, SQL databases, and more. It can also export data to these formats, enabling seamless data
exchange.

**Data Merging and Joining**: You can combine multiple DataFrames using methods like merge and join, similar
to SQL operations, to create more complex datasets from different sources.
Efficient Indexing: Pandas provides efficient indexing and selection methods, allowing you to access specific
rows and columns of data quickly.

**Custom Data Structures**: You can create custom data structures and manipulate data in ways that suit your
specific needs, extending Pandas' capabilities.

# Series Attributes and Methods
Pandas Series come with various attributes and methods to help you manipulate and analyze data effectively.

Here are a few essential ones:
- values: Returns the Series data as a NumPy array.
- index: Returns the index (labels) of the Series.
- shape: Returns a tuple representing the dimensions of the Series.
- size: Returns the number of elements in the Series.
- mean(), sum(), min(), max(): Calculate summary statistics of the data.
- unique(), nunique(): Get unique values or the number of unique values.
- sort_values(), sort_index(): Sort the Series by values or index labels.
- isnull(), notnull(): Check for missing (NaN) or non-missing values.
- apply(): Apply a custom function to each element of the Series.

# DataFrame Attributes and Methods
DataFrames provide numerous attributes and methods for data manipulation and analysis, including:

- shape: Returns the dimensions (number of rows and columns) of the DataFrame.
- info(): Provides a summary of the DataFrame, including data types and non-null counts.
- describe(): Generates summary statistics for numerical columns.
- head(), tail(): Displays the first or last n rows of the DataFrame.
- mean(), sum(), min(), max(): Calculate summary statistics for columns.
- sort_values(): Sort the DataFrame by one or more columns.
- groupby(): Group data based on specific columns for aggregation.
- fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
- apply(): Apply a function to each element, row, or column of the DataFrame.
