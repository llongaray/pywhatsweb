"""
Setup script para PyWhatsWeb
Compatível com versões antigas do pip
"""

from setuptools import setup, find_packages
import os

# Ler README
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Ler requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Ler requirements-dev
def read_requirements_dev():
    with open("requirements-dev.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pywhatsweb",
    version="0.1.0",
    author="TI Léo Team",
    author_email="ti.leo@example.com",
    description="Biblioteca Python para automação do WhatsApp Web baseada no whatsapp-web.js",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/llongaray/pywhatsweb",
    project_urls={
        "Bug Reports": "https://github.com/llongaray/pywhatsweb/issues",
        "Source": "https://github.com/llongaray/pywhatsweb",
        "Documentation": "https://github.com/llongaray/pywhatsweb#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.8",
    install_requires=[
        "selenium>=4.0.0",
        "webdriver-manager>=3.8.0",
        "requests>=2.25.0",
        "python-dotenv>=0.19.0",
        "qrcode>=7.3.0",
        "pillow>=8.0.0",
    ],
    extras_require={
        "dev": read_requirements_dev(),
    },
    include_package_data=True,
    zip_safe=False,
    keywords="whatsapp, automation, selenium, web, bot, messaging",
    entry_points={
        "console_scripts": [
            "pywhatsweb=pywhatsweb.cli:main",
        ],
    },
)
