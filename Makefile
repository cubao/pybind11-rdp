all:
	@echo nothing special

clean:
	rm -rf build dist wheelhouse *.egg-info
force_clean:
	docker run --rm -v `pwd`:`pwd` -w `pwd` -it alpine/make make clean
.PHONY: clean force_clean

build:
	mkdir -p build && cd build && \
	cmake .. && make
.PHONY: build

DOCKER_TAG_WINDOWS ?= ghcr.io/cubao/build-env-windows-x64:v0.0.1
DOCKER_TAG_LINUX ?= ghcr.io/cubao/build-env-manylinux2014-x64:v0.0.1
DOCKER_TAG_MACOS ?= ghcr.io/cubao/build-env-macos-arm64:v0.0.1
DOCKER_TAG_SUPERLINTER ?= ghcr.io/cubao/superlinter:v0.0.1

test_in_win:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/win:`pwd`/build -it $(DOCKER_TAG_WINDOWS) bash
test_in_mac:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/mac:`pwd`/build -it $(DOCKER_TAG_MACOS) bash
test_in_linux:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/win:`pwd`/build -it $(DOCKER_TAG_LINUX) bash
test_in_superlinter:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/win:`pwd`/build -it $(DOCKER_TAG_SUPERLINTER) bash

python_install:
	python setup.py install
python_build:
	python setup.py bdist_wheel
python_sdist:
	python setup.py sdist
python_test:
	python -c 'import cubao_cmake_example; print(cubao_cmake_example.add(1, 2))'

# conda create -y -n py36 python=3.6
# conda create -y -n py37 python=3.7
# conda create -y -n py38 python=3.8
# conda create -y -n py39 python=3.9
# conda create -y -n py310 python=3.10
# conda env list
python_build_py36:
	conda run --no-capture-output -n py36 make python_build
python_build_py37:
	conda run --no-capture-output -n py37 make python_build
python_build_py38:
	conda run --no-capture-output -n py38 make python_build
python_build_py39:
	conda run --no-capture-output -n py39 make python_build
python_build_py310:
	conda run --no-capture-output -n py310 make python_build
python_build_all: python_build_py36 python_build_py37 python_build_py38 python_build_py39 python_build_py310
python_build_all_in_linux:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/win:`pwd`/build -it $(DOCKER_TAG_LINUX) make python_build_all
	make repair_wheels && rm -rf dist/*.whl && mv wheelhouse/*.whl dist && rm -rf wheelhouse
python_build_all_in_macos: python_build_py38 python_build_py39 python_build_py310

repair_wheels:
	python -m pip install auditwheel
	ls dist/* | xargs -n1 auditwheel repair --plat manylinux2014_x86_64

pypi_remote ?= pypi
upload_wheels:
	python -m pip install twine
	twine upload wheelhouse/*.whl -r $(pypi_remote)

tar.gz:
	tar cvzf ../cmake_example.tar.gz .
	ls -alh ../cmake_example.tar.gz
