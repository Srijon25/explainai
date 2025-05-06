---
title: 'ExplainAI: An Open Source Framework for Visual Explanation of Transformer-Based Neural Networks'
tags:
  - python
  - transformers
  - explainable ai
  - visualization
  - attention
  - nlp
authors:
  - name: Your Name
    orcid: 0000-0000-0000-0000
    affiliation: 1
affiliations:
  - name: Your Department, Your University or Organization
    index: 1
date: 2025-05-06
---

# Summary

Transformer-based neural networks such as BERT, GPT, and ViT offer high performance but are often criticized for their lack of interpretability. **ExplainAI** is an open-source framework that enables intuitive visual explanation of these models using modern XAI techniques such as attention maps, integrated gradients, and SHAP. The tool offers a web-based interface, CLI, and API integration, making it suitable for research, teaching, and debugging purposes.

# Statement of Need

While existing tools like Captum and ELI5 provide general-purpose model interpretability, they lack specialized support for transformer architectures and interactivity. ExplainAI provides transformer-specific visualization, real-time rendering, and modular plugin-based extension, helping researchers interpret predictions during training or inference.

# Functionality

- Visualize attention heads across layers
- Generate attribution maps using Integrated Gradients and SHAP
- Web interface (Streamlit) and Python API
- Plugin support for custom model layers

# Example

```python
from explainai import ExplainModel
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
explainer = ExplainModel(model, tokenizer)
explainer.visualize_attention("The movie was surprisingly good!")
```

# Acknowledgements

We acknowledge the maintainers of Hugging Face, Captum, and Streamlit for foundational libraries and tools.

# References

```bibtex
@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and others},
  journal={Advances in neural information processing systems},
  year={2017}
}

@article{ribeiro2016why,
  title={"Why should I trust you?": Explaining the predictions of any classifier},
  author={Ribeiro, Marco Tulio and others},
  journal={Proceedings of the 22nd ACM SIGKDD},
  year={2016}
}
```
