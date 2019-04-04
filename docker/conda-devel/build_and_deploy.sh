#!/usr/bin/env bash

# Get the Anaconda Cloud access token.
ANACONDA_TOKEN=${ANACONDA_TOKEN:-$1}

# Check the OS.
if [ "$(uname)" == "Darwin" ]; then
    OS=osx-64
else
    OS=linux-64
fi

# Set the bin directory.
BIN_DIR=$HOME/sire.app/bin

# Set the source and Conda build directory on macOS.
SRC_DIR=.
CONDA_DIR=./docker/conda-devel/recipe

# Linux runs in a docker container from $HOME.
if [ ! -d $CONDA_DIR ]; then
    SRC_DIR=$HOME/Sire
    CONDA_DIR=$HOME/BioSimSpace/docker/conda-devel/recipe
fi

# Move the to build directory.
cd $CONDA_DIR

# Set the default Conda label.
LABEL=dev

# Get the tag associated with the latest commit.
TAG=$(git --git-dir=$SRC_DIR/.git tag --contains)

# If the tag is not empty, then set the label to main.
if [ ! -e $TAG ]; then
    LABEL=main
fi

# Build the Conda package.
$BIN_DIR/conda-build -c conda-forge -c omnia -c michellab .

# Upload the package to the michellab channel on Anaconda Cloud.
$BIN_DIR/anaconda -t $ANACONDA_TOKEN upload --user michellab $HOME/sire.app/conda-bld/$OS/biosimspace-* --label $LABEL
