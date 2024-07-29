from kedro.pipeline import Pipeline, node

from .nodes import auto_ml


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                auto_ml,
                [
                    "X_train",
                    "y_train",
                    "X_test",
                    "y_test",
                    "params:automl_max_evals",
                    "params:log_to_mlflow",
                    "params:mlflow_experiment_id",
                    "params:mlflow_model_registry",
                ],
                dict(model="model", mlflow_run_id="mlflow_run_id"),
            )
        ]
    )
