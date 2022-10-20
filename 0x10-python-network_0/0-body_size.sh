#!/bin/bash
# displays size of body in bytes
curl -i $1 | grep Content-Length | tail -c 4
