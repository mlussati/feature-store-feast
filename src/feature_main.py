import os
import json
import pandas as pd
from pathlib import Path
from urllib.request import urlopen

URL_PRJ = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/projects.csv"
URL_TGS = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/tags.csv"

# Load Labeled projects
def load_label_project(url_project: str, url_tags: str) -> pd.DataFrame:

    try:
        projects = pd.read_csv(url_project)
        tgs = pd.read_csv(url_tags)

        df = pd.concat([projects, tgs], axis=1)
        df["text"] = df.title + " " + df.description
        df.drop(["title", "description"], axis=1, inplace=True)
        return df
    except Exception as e:
        return e

def convert_to_parquet():

    df_res = load_label_project(URL_PRJ, URL_TGS)
    df_res.created_on = pd.to_datetime(df_res.created_on)

    # Convert to parquet
    DATA_DIR = Path(os.getcwd(), "data")
    print(DATA_DIR)
    return df_res.to_parquet(
        Path(DATA_DIR, "features.parquet"),
        compression=None,
        allow_truncated_timestamps=True,
    )


if __name__ == '__main__':
    df_res = convert_to_parquet()
