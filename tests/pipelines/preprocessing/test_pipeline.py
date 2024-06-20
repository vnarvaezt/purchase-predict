from kedro.runner import SequentialRunner

from purchase_predict.pipelines.preprocessing.pipeline import create_pipeline


def test_pipeline(catalog_test):
    # allows the pipeline execution
    runner = SequentialRunner()
    pipeline = create_pipeline()
    pipeline_output = runner.run(pipeline, catalog_test)
    assert pipeline_output["X_train"].shape[0] == pipeline_output["y_train"].shape[0]
    assert pipeline_output["X_test"].shape[0] == pipeline_output["y_test"].shape[0]
