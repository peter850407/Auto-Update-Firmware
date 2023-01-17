#!/bin/bash

SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)

echo -e "安裝\033[0;92m expect \033[0m和\033[0;92m pv \033[0m和\033[0;92m pixz \033[0m和\033[0;92m lbzip2 \033[0m,
     \033[0;92mpython3-pip \033[0m和\033[0;92m selenium \033[0m,
以及輸入\033[0;92mDUT\033[0m的\033[0;92mIP\033[0m, 更改權限, 建立各種資料夾。"

sleep 1
printf "是否繼續進行 [Y/n]？"

read choose
[[ "$choose" != "Y" ]] && exit 1

printf "輸入\033[0;93mDUT\033[0m的\033[0;93mIP\033[0m: "
read IP
touch config/AUF.config

tee config/AUF.config <<EOF
#----------------------------------------#
  DUTIP=$IP
#----------------------------------------#
  DUTDIR=/home
#----------------------------------------#
  PORT=9999
#----------------------------------------#
  dut_password=test0000
#----------------------------------------#
EOF
# sed -i "2c \  DUTIP=$IP" config/AUF.config
echo

chmod +x *
chmod +x config/*

sudo apt install expect pv python3-pip
pip install --upgrade selenium

mkdir -v $SCRIPT_DIR/CPFE_Downloads
mkdir -v $SCRIPT_DIR/CPFE
cd $SCRIPT_DIR/CPFE
mkdir -v $SCRIPT_DIR/CPFE/volteer
mkdir -v $SCRIPT_DIR/CPFE/eldrid
mkdir -v $SCRIPT_DIR/CPFE/brya
mkdir -v $SCRIPT_DIR/CPFE/gimble
mkdir -v $SCRIPT_DIR/CPFE/primus
mkdir -v $SCRIPT_DIR/CPFE/crota
mkdir -v $SCRIPT_DIR/CPFE/brask
mkdir -v $SCRIPT_DIR/CPFE/moli
mkdir -v $SCRIPT_DIR/CPFE/nissa_ite
mkdir -v $SCRIPT_DIR/CPFE/nereid
mkdir -v $SCRIPT_DIR/CPFE/joxer
