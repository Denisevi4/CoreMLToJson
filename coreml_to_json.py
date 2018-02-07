from protobuf_to_dict import protobuf_to_dict

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
    return model_json





