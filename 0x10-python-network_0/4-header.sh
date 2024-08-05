#!/bin/bash
# takes URL as an argument, sends GET request to URL,displays the body
curl -sH "X-School-User-Id: 98" "$1"
