[tool.poetry]
name = "git-09112023"
version = "0.1.0"
description = ""
authors = ["Василь Картичак <w.i.k.mailua@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
aiogram = "^3.1.1"
rich = "^13.6.0"


[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
faker = "^20.0.0"
flake8 = "^6.1.0"
black = "^23.11.0"
isort = "^5.12.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"