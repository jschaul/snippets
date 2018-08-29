# wire 
sudo dnf install -y pkgconfig haskell-platform libstdc++-devel libstdc++-static gcc-c++ libtool automake openssl-devel libsodium-devel ncurses-compat-libs libicu-devel clang-devel dh-autoreconf debhelper cmake valgrind skopeo socat

# develop
sudo dnf install -y htop tig zsh terminator
# qubes-specific
sudo dnf install -y qubes-gpg-split qubes-usb-proxy

# aws 
sudo dnf install -y awscli

which stack || { 
    curl -sSL https://get.haskellstack.org/ | sh 
    export PATH=~/.local/bin:$PATH
}
which cargo || {
    curl https://sh.rustup.rs -sSf | sh
    source $HOME/.cargo/env
}
which makedeb || {
  (git clone https://github.com/wireapp/wire-server && cd wire-server/tools/makedeb && stack install .)
}

export TARGET_LIB="$HOME/.wire-dev/lib"
export TARGET_INCLUDE="$HOME/.wire-dev/include"
mkdir -p "$TARGET_LIB"
mkdir -p "$TARGET_INCLUDE"
mkdir -p $HOME/.stack
cat $HOME/.stack/config.yaml | grep $TARGET_INCLUDE || {
    echo "extra-include-dirs:\n- $TARGET_INCLUDE\nextra-lib-dirs:\n- $TARGET_LIB" >> $HOME/.stack/config.yaml
}

! ls $TARGET_INCLUDE/cbox.h || {
    (git clone https://github.com/wireapp/cryptobox-c && cd cryptobox-c && make install)
}


# export PKG_CONFIG_PATH=$HOME/.wire-dev/lib/pkgconfig
# pkg-config --exists libzauth

## google version manager
# bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
# gvm install go1.10.3
## install dep dependency manager 
# curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
