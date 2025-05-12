# Explain AI

A simple Python package and Gradio app that performs zero-shot text classification using Hugging Face's `facebook/bart-large-mnli` model.

## Installation

```bash
pip install .
```

## Usage

```python
from explainai import explain

text = "I want to understand this situation."
labels = "education, finance, politics"
print(explain(text, labels))
```
