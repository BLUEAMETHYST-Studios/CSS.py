clean:
	rm -rf build
	rm -rf dist
	rm -rf CSSdotPy.egg-info
	rm -rf cssdotpy/__pycache__
build:
	python3 setup.py bdist_wheel
setversion:
	python3 -c 'open("VERSION", "w").write(input("Version: "))'
release:
	twine upload dist/* --verbose
install:
	pip install cssdotpy
update:
	pip install --upgrade cssdotpy
remove:
	pip uninstall cssdotpy
deploy-website:
	python3 -m http.server 8000 -d docs