from setuptools import setup, find_packages

setup(
    name="research_assistant",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit==1.18.1",
        "autogen==0.1.1",
        "requests==2.26.0",
        "python-dotenv==0.19.2",
        "pyyaml==6.0",
    ],
)
