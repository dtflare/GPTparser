from setuptools import setup, find_packages

setup(
    name="GPTparser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain==0.1.4",
        "openai==1.10.0",
        "deeplake",
        "tiktoken",
        "newspaper3k",
        "python-dotenv"
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'GPTparser=GPTparser.GPTparser:main',
            'combinR=GPTparser.extra_scripts.combinR:main',
            'j_val=GPTparser.extra_scripts.j_val:main',
            'wordcount=GPTparser.extra_scripts.wordcount:main',
        ],
    },
)
