#!/bin/bash
# if ur here for whatever reason uk whats this
curl -s -o /dev/null -w "%{http_code}" "$1"
