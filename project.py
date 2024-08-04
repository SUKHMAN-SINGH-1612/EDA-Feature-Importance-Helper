import streamlit as st
import pandas as pd
import numpy as np

feature = None


def data_preprocessing(df):
    # Remove identifier columns
    identifier_columns = []
    for col in df.columns:
        if len(df[col].unique()) == len(df):
            identifier_columns.append(col)
    df = df.drop(columns=identifier_columns)

    # Label encoding
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])
    return df

def check_target(df, target):
    # Check if the number of unique values is equal to the total number of rows
    if df[target].nunique() / len(df) > 0.3:
        return 'Regression'
    else:
        return 'Classification'

def feature_selector(df, target):
    global feature
    if check_target(df, target) == 'Regression':
        from sklearn.ensemble import RandomForestRegressor
        X = df.drop(columns=[target])
        y = df[target]
        model = RandomForestRegressor()
        model.fit(X, y)
        importance = model.feature_importances_
        features = pd.DataFrame({'Feature': X.columns, 'Importance': importance}).sort_values(by='Importance', ascending=False)
        return features
    if check_target(df, target) == 'Classification':
        from sklearn.ensemble import RandomForestClassifier
        X = df.drop(columns=[target])
        y = df[target]
        model = RandomForestClassifier()
        model.fit(X, y)
        importance = model.feature_importances_
        features = pd.DataFrame({'Feature': X.columns, 'Importance': importance}).sort_values(by='Importance', ascending=False)
        return features

def top_features():
    return feature.head(5)

def determine_type(column):
    if df[column].nunique() / len(df) > 0.1:
        return 'continuous'
    else:
        return 'discrete'

st.title('EDA Feature Importance Helper')
st.write("This project involves preprocessing a dataset by encoding categorical variables, determining the nature of the target variable (regression or classification), and selecting features based on their importance.")
x = st.file_uploader('Upload a file', type=['csv', 'xls', 'xlsx'])
if x is not None:
    if x.name.endswith('csv'):
        df = pd.read_csv(x)
    elif x.name.endswith('xlsx'):
        df = pd.read_excel(x)
    st.write('Data')
    st.write(df.head())
    st.write('Data Dictionary')
    st.write(pd.DataFrame({'Data Type': df.dtypes}))
    st.write("Data Preprocessing")
    df = data_preprocessing(df)
    st.write(df.head())
    st.write('Select target column')
    target = st.selectbox('Target Column', df.columns)

    if st.button('Show Feature Importance'):
        feature_importance_df = feature_selector(df, target)
        st.write(feature_importance_df)
        
        # Set 'Feature' column as the index
        feature_importance_df.set_index('Feature', inplace=True)

        # Display the bar chart with 'Feature' as x-axis and 'Importance' as y-axis
        st.bar_chart(feature_importance_df)
