from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="ASR-metrics",
    version="1.0.12",
    description="A Python package to get CER and WER for automatic speech recognitions",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/m-d-hasan/ASR-metrics",
    author="Md Hasan",
    author_email="mdhasan.nsu@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["ASR_metrics"],
    include_package_data=True,
    install_requires=["python-Levenshtein==0.12.0"],
    entry_points={
        "console_scripts": [
            "ASR-metrics=ASR_metrics.calculate.__main__:main",
        ]
    },
)

