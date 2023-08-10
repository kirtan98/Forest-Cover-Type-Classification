import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

train_data = pd.read_csv(r"/content/mlproject/forest-cover-type-prediction/train.csv")

train_data.shape

train_data.head()

train_data.columns

train_data.info

train_data.describe(include='all')

cover_type = {
    1: 'Spruce/Fir',
    2: 'Lodgepole Pine',
    3: 'Ponderosa Pine',
    4: 'Cottonwood/Willow',
    5: 'Aspen',
    6: 'Douglas-fir',
    7: 'Krummholz'
}

train_data['Cover_Type'] = train_data['Cover_Type'].map(cover_type)

plt.figure(figsize=(12, 7))
sns.histplot(data=train_data, x="Elevation", hue="Cover_Type", multiple="stack", palette="husl", linewidth=0)
plt.title("Elevation by Cover Type")
plt.show()

plt.figure(figsize=(12, 7))
sns.histplot(train_data, x="Elevation", hue="Cover_Type", element="poly", palette="Paired")
plt.title("Elevation Density by Cover Type")
plt.show()

soil_df = train_data.iloc[:, 15:55]
soil_df_encoded = pd.DataFrame(soil_df)
train_data['Soil_Types'] = soil_df_encoded.idxmax(axis=1)
train_data['Soil_Types'] = train_data['Soil_Types'].str.replace('Soil_Type','')

WildernessArea_df = train_data.iloc[:, 11:15]
WildernessArea_df_encoded = pd.DataFrame(WildernessArea_df)
train_data['Wilderness_Area'] = WildernessArea_df_encoded.idxmax(axis=1)
train_data['Wilderness_Area'] = train_data['Wilderness_Area'].str.replace('Wilderness_Area','')

sorted_soil_order = sorted(train_data['Soil_Types'].unique())
train_data['Soil_Types'] = pd.Categorical(train_data['Soil_Types'], categories=sorted_soil_order, ordered=True)

plt.figure(figsize=(12, 7))
sns.histplot(data=train_data, x="Soil_Types", hue="Cover_Type", multiple="stack", palette="husl", linewidth=0)
plt.title('Distribution of Cover Types by Soil Types')
plt.show()

sorted_wilderness_order = sorted(train_data['Wilderness_Area'].unique())
train_data['Wilderness_Area'] = pd.Categorical(train_data['Wilderness_Area'], categories=sorted_wilderness_order, ordered=True)

plt.figure(figsize=(12, 7))
sns.histplot(data=train_data, x="Wilderness_Area", hue="Cover_Type", multiple="stack", palette="husl", linewidth=0)
plt.title('Distribution of Cover Types by Wilderness Areas')
plt.show()

fig = px.scatter_3d(train_data, x='Hillshade_9am', y='Hillshade_Noon', z='Hillshade_3pm',
                    color='Cover_Type', opacity=0.7)
fig.update_layout(
    title='Hillshade at 9am, Noon and 3pm',
    width=1000,
    height=800,
)
fig.show()

fig = px.scatter_3d(train_data, x='Elevation', y='Slope', z='Hillshade_9am',
                    color='Cover_Type', opacity=0.7)
fig.update_layout(
    title='Elevation, Slope, and Hillshade at 9am',
    width=1000,
    height=800,
)
fig.show()

fig = px.scatter_3d(train_data, x='Elevation', y='Slope', z='Hillshade_Noon',
                    color='Cover_Type', opacity=0.7)
fig.update_layout(
    title='Elevation, Slope, and Hillshade at Noon',
    width=1000,
    height=800,
)
fig.show()

fig = px.scatter_3d(train_data, x='Elevation', y='Slope', z='Hillshade_3pm',
                    color='Cover_Type', opacity=0.7)
fig.update_layout(
    title='Elevation, Slope, and Hillshade at 3pm',
    width=1000,
    height=800,
)
fig.show()
