# Ramer-Douglas-Peucker Algorithm (c++ binding for python via pybind11)

>   A speed up (~8000x) version of [python version of rdp](https://github.com/fhirschmann/rdp).

C++/pybind11/NumPy implementation of the Ramer-Douglas-Peucker algorithm (Ramer 1972; Douglas and Peucker 1973) for 2D and 3D data.

The Ramer-Douglas-Peucker algorithm is an algorithm for reducing the number of points in a curve that is approximated by a series of points.


## Installation

### via pip

```bash
pip install -U pybind11-rdp
```

### from source

```bash
git clone --recursive https://github.com/cubao/pybind11-rdp
pip install ./pybind11-rdp
```

Or

```bash
pip install git+https://github.com/cubao/pybind11-rdp.git
```

(you can build wheels for later reuse by ` pip wheel git+https://github.com/cubao/pybind11-rdp.git`)

### in the browser (pyodide / wasm)

A pyodide wheel is built by the `Wheel on pyodide` job in
[`.github/workflows/wheels.yml`](.github/workflows/wheels.yml) and published to
PyPI together with the other wheels. Inside pyodide:

```js
const pyodide = await loadPyodide();
await pyodide.loadPackage(["numpy", "micropip"]);
const micropip = pyodide.pyimport("micropip");
await micropip.install("pybind11-rdp"); // or a local wheel: "./pybind11_rdp-...wasm32.whl"
const rdp = pyodide.pyimport("pybind11_rdp").rdp;
```

To build and test locally:

```bash
make pyodide_install   # pip install pyodide-build
make pyodide_wheel     # -> dist/*wasm32.whl
make pyodide_web       # builds, writes tests/pyodide/wheels.json, serves :8123
# open http://localhost:8123/tests/pyodide/index.html
```

Each wheel is ABI-tagged for one pyodide runtime (`pyemscripten_2024_0_wasm32` …)
and the page's pyodide version has to match that tag. CI builds one wheel per
supported pyodide version; locally `pyodide build` picks the xbuildenv whose
CPython matches your host interpreter, so a Python 3.12 host gets pyodide 0.27.x
(ABI 2024_0). Use `pyodide xbuildenv install <version> --force` to target
another version — `gen_wheels_json.py` then writes it into `wheels.json`, and
`?pyodide_version=` overrides it in the browser.

[`tests/pyodide/index.html`](tests/pyodide/index.html) loads pyodide (by default
from the jsdelivr CDN), installs the wheel from `dist/` and runs `tests/` in the
browser. If the CDN is slow, mirror the runtime once and the page picks it up
automatically:

```bash
python tests/pyodide/fetch_pyodide_dist.py --version 0.27.8
```

## Usage

Test installation: `python -c 'from pybind11_rdp import rdp; print(rdp([[1, 1], [2, 2], [3, 3], [4, 4]]))'`

Simple pythonic interface:

```python
from pybind11_rdp import rdp

rdp([[1, 1], [2, 2], [3, 3], [4, 4]])
[[1, 1], [4, 4]]
```

With epsilon=0.5:

```python
rdp([[1, 1], [1, 1.1], [2, 2]], epsilon=0.5)
[[1.0, 1.0], [2.0, 2.0]]
```

Numpy interface:

```python
import numpy as np
from pybind11_rdp import rdp

rdp(np.array([1, 1, 2, 2, 3, 3, 4, 4]).reshape(4, 2))
array([[1, 1],
       [4, 4]])
```

## Tests

```bash
make python_install
make python_test
```

## Benchmark

```bash
python3 test.py
```

## Notice

As <https://github.com/fhirschmann/rdp/issues/13> points out, `pdist` in `rdp` is **WRONGLY** Point-to-Line distance.
We use Point-to-LineSegment distance.

```python
from rdp import rdp
print(rdp([[0, 0], [10, 0.1], [1, 0]], epsilon=1.0)) # wrong
# [[0.0, 0.0],
#  [1.0, 0.0]]

from pybind11_rdp import rdp
print(rdp([[0, 0], [10, 0.1], [1, 0]], epsilon=1.0)) # correct
# [[ 0.   0. ]
#  [10.   0.1]
#  [ 1.   0. ]]
```

## References

Douglas, David H, and Thomas K Peucker. 1973. “Algorithms for the Reduction of the Number of Points Required to Represent a Digitized Line or Its Caricature.” Cartographica: The International Journal for Geographic Information and Geovisualization 10 (2): 112–122.

Ramer, Urs. 1972. “An Iterative Procedure for the Polygonal Approximation of Plane Curves.” Computer Graphics and Image Processing 1 (3): 244–256.
