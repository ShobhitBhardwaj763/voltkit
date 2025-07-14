from setuptools import setup, find_packages

# Fix UnicodeDecodeError on Windows by explicitly using UTF-8
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="voltkit",
    version="1.0.0",
    description="VoltKit: A Python toolkit for electrical and electronics engineering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shobhit Bhardwaj",
    author_email="email@example.com",  # Optional: add real email or remove line
    url="",  # Replace with your GitHub repo URL after upload
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "streamlit"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    keywords="electrical engineering simulation education phasors fft bode streamlit",
    python_requires='>=3.7',
)
