"""
Setup para PyWhatsWeb
"""

from setuptools import setup, find_packages
import os

# Lê o README
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "PyWhatsWeb - Biblioteca Python para WhatsApp Web"

setup(
    name="pywhatsweb",
    version="1.0.0",
    author="TI Léo Team",
    author_email="ti.leo@example.com",
    description="Biblioteca Python para automação do WhatsApp Web",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tileo/pywhatsweb",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
    install_requires=[
        "qrcode>=7.0",
        "Pillow>=8.0.0",  # Para geração de QR codes
    ],
    extras_require={
        "mysql": ["mysql-connector-python>=8.0.0"],
        "flask": ["Flask>=2.0.0"],
        "django": ["Django>=3.0.0"],
        "celery": ["celery>=5.0.0"],
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "pywhatsweb=pywhatsweb.cli.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="whatsapp, automation, bot, messaging, python",
    project_urls={
        "Bug Reports": "https://github.com/tileo/pywhatsweb/issues",
        "Source": "https://github.com/tileo/pywhatsweb",
        "Documentation": "https://github.com/tileo/pywhatsweb#readme",
    },
)
