#!/bin/bash
# Create docker files for release
#
# 1. peg_solitaire_live: Production image
# 2. peg_solitaire_test: Production image + test code

set -u
set -e

build_dir=dockers/build
docker_tag_base=akarbstein/peg_solitaire

# FIXME: Insert sanity checking for $build_dir
if [ ! -d "${build_dir}" ]; then
  echo "Build dir does not exists"
  exit -1
fi

# Cleanup
# FIXME: Die if $build_dir directory is not empty
rm -rf ${build_dir}/*

# Live container
cp LICENSE ${build_dir}
cp README.md ${build_dir}
cp *.py ${build_dir}
cp dockers/peg_solitaire_live/Dockerfile ${build_dir}
docker build -t ${docker_tag_base}_live ${build_dir}

# Test container
cp -a tests ${build_dir}
cp dockers/peg_solitaire_test/Dockerfile ${build_dir}
docker build -t ${docker_tag_base}_test ${build_dir}

# Cleanup
rm -rf ${build_dir}/*

exit 0
