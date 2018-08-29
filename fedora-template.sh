#!/usr/bin/env bash

# wire 
sudo dnf install -y pkgconfig haskell-platform libstdc++-devel libstdc++-static gcc-c++ libtool automake openssl-devel libsodium-devel ncurses-compat-libs libicu-devel clang-devel dh-autoreconf debhelper cmake valgrind skopeo socat

# develop
sudo dnf install -y htop tig zsh terminator
# qubes-specific
sudo dnf install -y qubes-gpg-split qubes-usb-proxy

# aws 
sudo dnf install -y awscli
