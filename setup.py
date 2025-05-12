from setuptools import setup, find_packages

setup(
    name="explainai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gradio",
        "transformers",
        "torch"
    ],
    entry_points={
        "console_scripts": [
            "explainai=explainai.main:explain"
        ]
    },
    author="Your Name",
    description="Explain AI - A Zero-Shot Text Classifier",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://huggingface.co/spaces/your_username/explainai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
