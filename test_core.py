from explainai.core import explain

def test_explain():
    model = None
    input_data = {}
    result = explain(model, input_data)
    assert isinstance(result, dict)
