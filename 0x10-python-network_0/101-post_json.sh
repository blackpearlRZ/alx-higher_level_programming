#!/bin/bash
# if ur here for whatever reason uk whats this
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
