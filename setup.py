from setuptools import setup, find_packages

setup(
    name="smart_terminal",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "colorama",
        "openai",
    ],
    entry_points={
        'console_scripts': [
            'pllm = smart_terminal.cli:cli',
        ],
    },
)
