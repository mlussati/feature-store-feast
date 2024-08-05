import os
from datetime import datetime
from pathlib import Path
from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource
from google.protobuf.duration_pb2 import Duration

DATA_DIR = Path(os.getcwd(), "data")
START_TIME = "2020-02-17"


def read_data():

    project_details = FileSource(
        path=str(Path(DATA_DIR, "features.parquet")),
        event_timestamp_column="created_on",
    )

    return project_details


def define_entity():

    project = Entity(
        name="id",
        value_type=ValueType.INT64,
        description="project id",
    )
    return project


def define_view_each_project():
    project_details_view = FeatureView(
        name="project_details",
        entities=["id"],
        ttl=Duration(
            seconds=(datetime.today() - datetime.strptime(START_TIME, "%Y-%m-%d")) \
            .days * 24 * 60 * 60
        ),
        feature=[
            Feature(name="text", dtype=ValueType.STRING),
            Feature(name="tag", dtype=ValueType.STRING),
        ],
        online=True,
        input=read_data(),
        tags={},
    )
    return project_details_view


if __name__ == '__main__':
    define_view_each_project()

