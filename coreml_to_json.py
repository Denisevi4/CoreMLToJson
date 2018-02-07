from protobuf_to_dict import protobuf_to_dict

# From https://apple.github.io/coremltools/coremlspecification/sections/TreeEnsembles.html
TreeNodeBehavior = [
            'BranchOnValueLessThanEqual',
            'BranchOnValueLessThan',
            'BranchOnValueGreaterThanEqual',
            'BranchOnValueGreaterThan',
            'BranchOnValueEqual',
            'BranchOnValueNotEqual',
            'LeafNode'
]

def _replace_behavior(json):
    if isinstance(json, dict):
        for k,v in json.items():
            if k == "nodeBehavior":
                json[k] = TreeNodeBehavior[v]
            _replace_behavior(v)
    if isinstance(json, list):
        for ijson in json:
            _replace_behavior(ijson)

def coreml_to_json(file_or_model):
    """Converts CoreML to Json"""
    

    if isinstance(file_or_model, str):
        from coremltools.proto import Model_pb2
        model = Model_pb2.Model()

        with open(file_or_model, "rb") as f:
            model.ParseFromString(f.read())
    else:
        model = file_or_model
    
    model_json = protobuf_to_dict(model)
    _replace_behavior(model_json)
    
    return model_json





