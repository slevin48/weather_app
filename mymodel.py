
from urllib.request import urlopen
import json
import numpy as np
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
import plotly.graph_objects as go

def run(k):
    res = urlopen("https://samples.openweathermap.org/").read()
    sample = json.loads(res)
    url = sample['products']['forecast_5days']['samples'][0]
    res = urlopen(url).read()
    data = json.loads(res)
    time = [data['list'][i]['dt'] for i in range(40)]
    temp = [data['list'][i]['main']['temp'] for i in range(k)]

    X = np.arange(k).reshape(-1, 1)
    y = np.array(temp)

    rng = np.random.RandomState(1)
    regr_1 = DecisionTreeRegressor(max_depth=4)
    regr_2 = AdaBoostRegressor(
        DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
    )

    regr_1.fit(X, y)
    regr_2.fit(X, y)

    y_1 = regr_1.predict(X)
    y_2 = regr_2.predict(X)

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=y,mode='markers',name='Temperatures'))
    fig.add_trace(go.Scatter(y=y_1,mode='lines',name='n_estimators=1'))
    fig.add_trace(go.Scatter(y=y_2,mode='lines',name='n_estimators=100'))

    return fig