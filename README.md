[![Build Status](https://github.com/xmlx-io/xml-book-code/actions/workflows/test-and-release.yml/badge.svg)](https://github.com/xmlx-io/xml-book-code/actions/workflows/test-and-release.yml)
[![GitHub Release](https://img.shields.io/github/v/release/xmlx-io/xml-book-code?display_name=tag&logo=github)](https://github.com/xmlx-io/xml-book-code/releases/latest)  
[![MIT Licence](https://img.shields.io/github/license/xmlx-io/xml-book-code.svg)](https://github.com/xmlx-io/xml-book-code/blob/master/LICENCE)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://github.com/xmlx-io/xml-book-code)  
[![Read Book][book-badge]](https://book.xmlx.io)

# :floppy_disk: eXplainable Machine Learning – Code :floppy_disk: #

This repository holds a Python package implementing a collection of modules
used by the [eXplainable Machine Learning book][book] (Jupyter Book).

## Usage ##

The package can be installed with
```bash
pip install .
```

To run the tests, first install the development dependencies
```bash
pip install -r requirements-dev.txt
```
and execute
```bash
PYTHONPATH=./ pytest \
  --junit-xml=_pytest_junit.xml \
  --cov-report=term-missing \
  --cov-report=xml:_pytest_coverage.xml \
  --cov=xml_book \
  xml_book/
```

## Useful Resources ##

- XMLX Organisation
    * [Website][org]
    * [GitHub][org-github]
- XML Book
  * [Website][book]
  * [Documentation][docs]
  * [GitHub][book-repo]

[org]: https://xmlx.io/
[book]: https://book.xmlx.io/
[docs]: https://book.xmlx.io/docs
[org-github]: https://github.com/xmlx-io
[book-repo]: https://github.com/xmlx-io/xml-book/
[book-badge]: https://img.shields.io/badge/read-book-orange.svg?logo=data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MS43OCA3MS4xNSI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiNmZTdkMzc7fS5jbHMtMntmaWxsOiNmZmY7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5sb2dvLXNxdWFyZTwvdGl0bGU+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNNC44LDQ1Ljg3cTIuNyw4LjQ2LDEzLjc4LDguNzVoOS4xN3E5LjYzLDAsMTMuMTMsNy41M1E0NC4zLDU0LjYyLDU0LDU0LjYyaDguNDVxMTEuNzYsMCwxNC41NS04LjcybDQuNzgsMS42UTc5LjcxLDU0Ljg4LDc1LDU4LjU4VDYyLjYzLDYyLjMzSDUzLjg4cS0xMCwwLTEwLDguODJoLTZxMC04LjgyLTEwLjEzLTguODJIMTkuMzNxLTcuODMsMC0xMi41My0zLjc4VDAsNDcuNVoiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0yMC4zOSw0MS4zNEExMy44OCwxMy44OCwwLDAsMSwxNC4yMyw0MGExMC41OSwxMC41OSwwLDAsMS00LjQyLTQuMDZBMTQuMTcsMTQuMTcsMCwwLDEsOCwyOS4xNEw4LDI5aDUuM2MuMDcsMi43NC43LDQuNzUsMS44OCw2LjA1YTYuNTgsNi41OCwwLDAsMCw1LjA5LDEuOTIsNi43Myw2LjczLDAsMCwwLDMuOC0xLDUuOSw1LjksMCwwLDAsMi4yLTIuNzUsMTAuNDMsMTAuNDMsMCwwLDAsLjcyLTRWNC4zM2wtNS40NC0uNzJWMEgzNy4xMVYzLjU1bC00LjU3Ljc4VjI5LjE5YTE0LDE0LDAsMCwxLTEuMzksNi4zOSw5LjkyLDkuOTIsMCwwLDEtNC4wOSw0LjI1QTEzLjQzLDEzLjQzLDAsMCwxLDIwLjM5LDQxLjM0Wm0yMC45MS0uNTlWMzcuMjJsNC41Ni0uNzhWNC4zM0w0MS4zLDMuNTVWMEg1OC44OHE2LjM5LDAsMTAsMi43NWMyLjQsMS44MywzLjU5LDQuNTksMy41OSw4LjI3YTcuNTksNy41OSwwLDAsMS0xLjcxLDQuODYsMTAuMzcsMTAuMzcsMCwwLDEtNC41NSwzLjE4LDkuNTMsOS41MywwLDAsMSw0LjIyLDIsMTAsMTAsMCwwLDEsMi43MywzLjU4LDEwLjkyLDEwLjkyLDAsMCwxLDEsNC42NHEwLDUuNTktMy42NCw4LjU1dC05Ljg2LDNabTEwLjA4LTQuMzFoOS4yM2E4LjUsOC41LDAsMCwwLDUuODYtMS44Niw2LjY4LDYuNjgsMCwwLDAsMi4wOS01LjI4LDEwLDEwLDAsMCwwLS43Ni00LjExLDUuNjQsNS42NCwwLDAsMC0yLjM2LTIuNjMsNy42NSw3LjY1LDAsMCwwLTQtLjkzSDUxLjM4Wm0wLTE5LjExaDguOTNhNi43LDYuNywwLDAsMCw0Ljc5LTEuNzIsNi4xNyw2LjE3LDAsMCwwLDEuODQtNC43QTUuODksNS44OSwwLDAsMCw2NC44Niw2YTkuMzgsOS4zOCwwLDAsMC02LTEuNjRoLTcuNVoiLz48L3N2Zz4K
