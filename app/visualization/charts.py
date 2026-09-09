import pandas as pd
import plotly.express as px

def make_chart(rows):
    if not rows: return None
    df=pd.DataFrame(rows)
    numeric=list(df.select_dtypes(include="number").columns)
    categorical=[c for c in df.columns if c not in numeric]

    if numeric and categorical and len(df)>1:
        return px.bar(df,x=categorical[0],y=numeric[0])
    if len(numeric)>=2 and len(df)>1:
        return px.scatter(df,x=numeric[0],y=numeric[1])
    return None
