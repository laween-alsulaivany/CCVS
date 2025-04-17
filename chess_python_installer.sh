#!/bin/bash

sudo apt update; sudo apt install zlib1g-dev build-essential libssl-dev ;
# Set version and install prefix
PY_VERSION=3.10.12
INSTALL_DIR=$HOME/CCVS/.chessPython

# Download Python 3.10.12 source code
wget https://www.python.org/ftp/python/$PY_VERSION/Python-$PY_VERSION.tgz

# Extract it
tar -xf Python-$PY_VERSION.tgz
cd Python-$PY_VERSION

# Configure the build to use the custom directory
./configure --prefix=$INSTALL_DIR --enable-optimizations

# Compile (you can use -j$(nproc) to speed it up with parallel jobs)
make -j$(nproc)

# Install to the custom directory
make install

# Optional: Add it to your PATH for this session
# export PATH=$INSTALL_DIR/bin:$PATH

# Verify
python3.10 --version

cd ..

$INSTALL_DIR/bin/pip3 install pip --upgrade
$INSTALL_DIR/bin/pip3 install -r requirements.txt

rm -r Python-$PY_VERSION.tgz
rm -r Python-$PY_VERSION
