import os
from datetime import datetime
from pathlib import Path
from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource
from google.protobuf.duration_pb2 import Duration

DATA_DIR = Path(os.getcwd(), "data")

def read_data():

    return FileSource(
        path=str(Path(DATA_DIR, "features.parquet")),
        event_timestamp_column="created_on",
    )

def define_entity():

    return Entity(
        name="id",
        value_type=ValueType.INT64,
        description="project id",
    )

