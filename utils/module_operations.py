from importlib import import_module


def get_class(module_path, class_name):
    try:
        module = import_module(module_path)
        return  getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(class_name)