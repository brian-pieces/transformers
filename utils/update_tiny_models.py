import json

from create_dummy_models import create_tiny_models

if __name__ == "__main__":

    with open("tests/utils/tiny_model_summary.json") as fp:
        tiny_model_info = json.load(fp)

    existing_model_classes = {}
    for name in tiny_model_info:
        existing_model_classes.update(tiny_model_info[name]["model_classes"])
    existing_model_classes = sorted(list(existing_model_classes))

    output_path = "tiny_models"
    all = True
    model_types = None
    models_to_skip = existing_model_classes
    no_check = True
    upload = False
    organization = "hf-internal-testing"

    create_tiny_models(
        output_path,
        all,
        model_types,
        models_to_skip,
        no_check,
        upload,
        organization,
    )
