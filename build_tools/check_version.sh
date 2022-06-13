#!/bin/bash
#title       :check_version.sh
#description :Checks for match between git tag and the Python package version
#author      :Kacper Sokol <kacper@xmlx.io>
#license     :MIT
#==============================================================================

PACKAGE_VERSION=$(python -c "import xml_book; print(xml_book.__version__)")

# git describe --tags
GIT_TAG=$(git tag --points-at HEAD)

if [ -z "$GITHUB_TAG" ]; then
  if [ -z "$GIT_TAG" ]; then
    echo "This git commit is not tagged. Cannot create a release."
    exit 1
  else
    if [ "$GIT_TAG" == "$PACKAGE_VERSION" ]; then
      echo "Safe to deploy package version $PACKAGE_VERSION."
    else
      echo "The Python version ($PACKAGE_VERSION) and git tag ($GIT_TAG) do" \
        "not agree."
      exit 1
    fi
  fi
else
  if [ "$GIT_TAG" == "$GITHUB_TAG" ]; then
    if [ "$GITHUB_TAG" == "$PACKAGE_VERSION" ]; then
      echo "Safe to deploy package version $PACKAGE_VERSION."
    else
      echo "The Python version ($PACKAGE_VERSION) and git tag ($GIT_TAG) do" \
        "not agree."
      exit 1
    fi
  else
    echo "Internal error: the GitHub tag ($GITHUB_TAG) and git tag" \
      "($GIT_TAG) do not agree."
    exit 1
  fi
fi
