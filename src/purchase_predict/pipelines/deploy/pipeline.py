from kedro.pipeline import Pipeline, node

from .nodes import assign_alias


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                assign_alias,
                "params:mlflow_model_registry",
                None,
            ),
        ]
    )
