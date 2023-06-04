from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Emotion Classifier",
    description="Classify Emotions from Text",
    packages = find_packages(),
    install_requires=requirements, 
    entry_points="""[console_scripts]
    classifier=main:main""",
    author="Diarra Bell"
)