from kedro.pipeline import Pipeline, node

from .nodes import load_csv_from_bucket


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                load_csv_from_bucket,
                ["project_id", "bucket_path"],
                "primary",
            )
        ]
    )
