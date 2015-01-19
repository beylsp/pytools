help:
	@echo "clean - remove all build/python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"

clean: clean-build clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf deb_dist/
	rm -rf *.egg-info
	rm -rf *.tar.gz

clean-pyc:
	find . -name '*.pyc' | xargs rm -rf
	find . -name '*.pyo' | xargs rm -rf
	find . -name '*~' | xargs rm -rf

