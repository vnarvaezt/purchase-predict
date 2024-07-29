import os
import mlflow

from mlflow.tracking import MlflowClient


def assign_alias(registry_name: str):
    """
    Asigns alias
    """
    env = os.getenv("ENV")
    if env == "local" or "staging":
        alias = "challenger"
    elif env == "production":
        alias = "champion"
    else:
        raise EnvironmentError("Wrong environment variable")
    # FIXME: doesnt raise error
    client = MlflowClient()
    latest_v = client.get_latest_versions(registry_name, stages=["None"])
    print("latest_v", latest_v)
    client.set_registered_model_alias(registry_name, alias, latest_v[0].version)
