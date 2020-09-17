import onnx


def get_op_types(model_path):
    model = onnx.load_model(model_path)
    nodes = model.graph.node

    op_types = [node.op_type for node in nodes]
    return list(set(op_types))

if __name__ == '__main__':
    onnx_path = "lstm.onnx"
    op_types = get_op_types(onnx_path)
    print(op_types)
