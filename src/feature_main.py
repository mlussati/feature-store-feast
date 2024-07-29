import os
import json
import pandas as pd
from pathlib import Path
from urllib.request import urlopen


# Load Labeled projects
def load_label_project(url_project: str, url_tags: str) -> pd.DataFrame:

    try:
        projects = pd.read_csv(url_project)
        tgs = pd.read_csv(url_tags)

        df = pd.merge(projects, tgs, on="id")
        df["text"] = df.title + " " + df.description
        df.drop(["title", "description"], axis=1, inplace=True)
        return df
    except Exception as e:
        return e
