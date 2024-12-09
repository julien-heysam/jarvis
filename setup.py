import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


def parse_requirements(filename: str):
    with open(filename, "r") as file:
        return [line for line in file.read().splitlines() if line and not line.startswith("-")]


setup(
    name="jarvis",
    version="0.1.0",
    description="Jarvis AI is an intelligent voice-activated digital assistant leveraging large language models to provide contextual interaction, system automation, and personalized task management through natural language processing, speech recognition, and multi-device integration.",
    author="JulienW",
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "jarvis=src.interface.cli.cli:cli",
        ],
    },
    install_requires=parse_requirements("requirements.txt"),
    extras_require={
        "dev": parse_requirements("requirements.dev.txt"),
    },
    zip_safe=False,
    license="MIT",
)
