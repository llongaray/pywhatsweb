.PHONY: help install install-dev test lint format clean build publish

help: ## Mostra esta ajuda
	@echo "PyWhatsWeb - Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Instala a biblioteca em modo desenvolvimento
	pip install -e .

install-dev: ## Instala dependências de desenvolvimento
	pip install -e ".[dev]"

test: ## Executa os testes
	pytest tests/ -v --cov=pywhatsweb --cov-report=html

test-fast: ## Executa testes sem cobertura
	pytest tests/ -v

lint: ## Executa verificações de qualidade de código
	black --check pywhatsweb tests examples
	isort --check-only pywhatsweb tests examples
	flake8 pywhatsweb tests examples
	mypy pywhatsweb

format: ## Formata o código automaticamente
	black pywhatsweb tests examples
	isort pywhatsweb tests examples

clean: ## Remove arquivos temporários
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: ## Constrói o pacote para distribuição
	python -m build

build-check: ## Verifica se o pacote pode ser construído
	python -m build --sdist --wheel
	twine check dist/*

publish-test: ## Publica no PyPI de teste
	twine upload --repository testpypi dist/*

publish: ## Publica no PyPI (produção)
	twine upload dist/*

pre-commit: ## Instala e configura pre-commit
	pre-commit install
	pre-commit run --all-files

docs: ## Gera documentação
	sphinx-build -b html docs/ docs/_build/html

check-all: lint test ## Executa todas as verificações

dev-setup: install-dev pre-commit ## Configura ambiente de desenvolvimento completo
