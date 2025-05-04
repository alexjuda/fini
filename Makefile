.PHONY: nop
nop:
	@echo Hello!

.PHONY: test
test:
	uv run pytest -vv src

.PHONY: format
format:
	uv run ruff format src
	uv run ruff check --fix src

.PHONY: typecheck
typecheck:
	uv run pyright src
