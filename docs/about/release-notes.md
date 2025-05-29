# Release Notes

---

## Upgrading

To upgrade `pybind11-rdp` to the latest version, use pip:

```bash
pip install -U pybind11-rdp
```

## Version 0.1.5 (2025-05-29)

*   Use scikit-build-core instead of setuptools
*   Add pyi stubs
*   Binary release for python 3.12, 3.13

## Version 0.1.4 (2023-07-28)

*   Handle degenerate case, related to <https://github.com/mapbox/geojson-vt/issues/104>
*   How to test? Use `ulimit -s 100 && python3 test.py`?

## Version 0.1.3 (2023-07-28)

*   Update docs, update packaging

## Version 0.1.2 (2023-03-02)

*   Identical API to rdp, notice difference

## Version 0.1.1 (2022-11-03)

*   Fix source packaging

## Version 0.1.0 (2022-11-03)

*   Export `LineSegment`

## Version 0.0.1 (2022-10-15)

*   First release to pypi

---

You can also checkout releases on:

-   GitHub: <https://github.com/cubao/pybind11-rdp/releases>
-   PyPi: <https://pypi.org/project/pybind11-rdp>
