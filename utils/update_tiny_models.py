import json
import time
from transformers import AutoModel, TFAutoModel
import transformers

# from create_dummy_models import create_tiny_models

if __name__ == "__main__":

    with open("../tests/utils/tiny_model_summary.json") as fp:
        tiny_model_info = json.load(fp)

    for name in list(tiny_model_info.keys())[:]:
        print(name)
        tiny_model_info[name]["model_classes"] = []
        ckpt = f"hf-internal-testing/tiny-random-{name}"
        try:
            model_class = getattr(transformers, name)
            model = model_class.from_pretrained(ckpt)
            tiny_model_info[name]["model_classes"].append(model.__class__.__name__)
            time.sleep(1)
        except:
            pass
        try:
            model_class = getattr(transformers, f"TF{name}")
            model = model_class.from_pretrained(ckpt)
            tiny_model_info[name]["model_classes"].append(model.__class__.__name__)
            time.sleep(1)
        except:
            pass

        with open("../tests/utils/new_tiny_model_summary.json", "w") as fp:
            json.dump(tiny_model_info, fp, ensure_ascii=False, indent=4)

    # existing_model_classes = {}
    # for name in tiny_model_info:
    #     existing_model_classes.update(tiny_model_info[name]["model_classes"])
    # existing_model_classes = sorted(list(existing_model_classes))
    #
    # output_path = "tiny_models"
    # all = True
    # model_types = None
    # models_to_skip = existing_model_classes
    # no_check = True
    # upload = False
    # organization = "hf-internal-testing"
    #
    # create_tiny_models(
    #     output_path,
    #     all,
    #     model_types,
    #     models_to_skip,
    #     no_check,
    #     upload,
    #     organization,
    # )
