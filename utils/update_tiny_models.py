from create_dummy_models import create_tiny_models

if __name__ == "__main__":

    output_path = "tiny_models"
    all = True
    model_types = None
    models_to_skip = []
    no_check = True
    upload = True
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
