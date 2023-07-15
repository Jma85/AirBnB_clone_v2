#!/bin/sh

git log --format='%aN <%aE>' | sort -u > AUTHORS
./generate-authors.sh
chmod +x generate-authors.sh