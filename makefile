install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
packege-install:
	python3 -m pip install --user dist/*.whl
