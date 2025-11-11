import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def find_cols_with_nulls_gt_five(df: pd.DataFrame) -> pd.Series:
    """
    Identify columns in the DataFrame that contain null values.

    Parameters:
    df (pd.DataFrame): The input DataFrame to check for null values.

    Returns:
    list: A list of column names that contain null values.
    """
    null_percent = df.isnull().mean() * 100

    return null_percent[null_percent > 5]

 

def draw_heat_map_outliner(df: pd.DataFrame, title:str):
    """
    Draw a heatmap to visualize the correlation between features in the DataFrame.
    """

    sns.heatmap(df.isnull(), cbar=False)
    plt.title(title)
    plt.show()


def draw_boxplots(df: pd.DataFrame, features: list, title: str):
    """
    Draw boxplots for the specified features in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features.
    features (list): A list of feature names to plot.
    title (str): The title of the plot.
    """
    sns.boxplot(data=df[features])
    plt.title(title)
    plt.show()


def find_outliers_iqr(df: pd.DataFrame, feature: list) -> pd.DataFrame:
    """
    Identify outliers in a specified feature using the IQR method.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the feature.
    feature (str): The feature name to check for outliers.

    Returns:
    pd.DataFrame: A DataFrame containing the outliers.
    """
    outliers = pd.DataFrame()
    for feature in feature:
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = pd.concat([outliers, df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]])

    return outliers


def find_outliers_zscore(df: pd.DataFrame, features: list, threshold: float = 3.0) -> pd.DataFrame:
    """
    Identify outliers in a specified feature using the Z-score method.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the feature.
    feature (str): The feature name to check for outliers.
    threshold (float): The Z-score threshold to identify outliers.

    Returns:
    pd.DataFrame: A DataFrame containing the outliers.
    """
    outliers = pd.DataFrame()
    for feature in features:
        mean = df[feature].mean()
        std = df[feature].std()

        z_scores = (df[feature] - mean) / std
        outliers = pd.concat([outliers, df[abs(z_scores) > threshold]])

    return outliers


def impute_with_median(df: pd.DataFrame, feature: str) -> pd.DataFrame:
    """
    Impute missing values in a specified feature with the median of that feature.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the feature.
    feature (str): The feature name to impute missing values.

    Returns:
    pd.DataFrame: The DataFrame with imputed values.
    """
    median_value = df[feature].median()
    df[feature].fillna(median_value, inplace=True)

    return df




def draw_barplot(df: pd.DataFrame, x: str, y: str, title: str):
    """
    Draw a bar plot for the specified x and y features in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features.
    x (str): The feature name for the x-axis.
    y (str): The feature name for the y-axis.
    title (str): The title of the plot.
    """
    plt.figure(figsize=(8,4))
    plt.bar(df[x], df[y], color='skyblue')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()



def draw_histogram(df: pd.DataFrame, feature: str, title: str):
    """
    Draw a histogram for the specified feature in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the feature.
    feature (str): The feature name to plot.
    title (str): The title of the plot.
    """
    plt.figure(figsize=(8,4))
    plt.hist(df[feature], bins=10, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()


def draw_scatterplot(df: pd.DataFrame, x: str, y: str):
    """
    Draw a scatter plot for the specified x and y features in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features.
    x (str): The feature name for the x-axis.
    y (str): The feature name for the y-axis.
    title (str): The title of the plot.
    """
    sns.scatterplot(x=x, y=y, data=df)
    plt.title(f"Scatter plot: {x} vs {y}")
    plt.show()



def draw_correlation_heatmap(df: pd.DataFrame, title: str, col_list: list = None):
    """
    Draw a correlation heatmap for the features in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features.
    title (str): The title of the plot.
    """
    corr = df[col_list].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title(title)
    plt.show()


def draw_bubbleplot(df: pd.DataFrame, x: str, y: str, size: str):
    """
    Draw a bubble plot for the specified x and y features in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features.
    x (str): The feature name for the x-axis.
    y (str): The feature name for the y-axis.
    size (str): The feature name for the size of the bubbles.
    title (str): The title of the plot.
    """
    x = df[x]
    y = df[y]
    bubble = df[size]
    color=df[size]

    plt.figure(figsize=(12,6))
    plt.scatter(x, y, s=bubble*5,c=color, cmap='viridis', alpha=0.5)
    plt.title(f"Bubble chart: {x} vs {y} (size {size})")
    plt.xlabel('solar radiation')
    plt.ylabel('Temperature')
    plt.show()