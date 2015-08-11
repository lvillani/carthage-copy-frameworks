all: DESCRIPTION.rst


DESCRIPTION.rst: README.md
	pandoc -f markdown -t rst -o $@ $<


upload: all
	python setup.py bdist upload
	python setup.py sdist upload
