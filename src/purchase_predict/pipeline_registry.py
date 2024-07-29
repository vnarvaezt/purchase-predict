"""Project pipelines."""

from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

# from purchase_predict.pipelines.loading import pipeline as loading_pipeline
from purchase_predict.pipelines.preprocessing import pipeline as preprocessing_pipeline
from purchase_predict.pipelines.model import pipeline as model_pipeline
from purchase_predict.pipelines.deploy import pipeline as deployment_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # p_loading = loading_pipeline.create_pipeline()
    p_preprocesing = preprocessing_pipeline.create_pipeline()
    p_model = model_pipeline.create_pipeline()
    p_deploy = deployment_pipeline.create_pipeline()
    return {
        "__default__": p_model,
        "global": Pipeline([p_preprocesing, p_model]),
        # "loading_pipeline": p_loading,
        "preprocessing": p_preprocesing,
        "data_science": p_model,
        "deployment": p_deploy,
    }
