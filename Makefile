clean:
	rm -rf build
	rm -rf dist
	rm -rf CSSdotPy.egg-info
build:
	python3 setup.py bdist_wheel
setversion:
	python3 set_version.py
release:
	twine upload dist/* --verbose
