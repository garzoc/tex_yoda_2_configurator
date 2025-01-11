#!/usr/bin/env bash

set -ex

readonly tex_binary="${1}"

xxd "${tex_binary}" | grep -Eo "0220 [0-9a-f ]{9} 0000" | sort | uniq
