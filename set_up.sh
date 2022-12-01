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
sed -i "2c \  DUTIP=$IP" config/AUF.config

chmod +x *

sudo apt install expect pv python3-pip
pip install selenium

mkdir -v CPFE_Downloads
mkdir -v CPFE
cd CPFE
mkdir -v volteer
mkdir -v eldrid
mkdir -v brya
mkdir -v gimble
mkdir -v primus
mkdir -v crota
mkdir -v brask
mkdir -v moli
mkdir -v nissa_ite
mkdir -v nereid
mkdir -v joxer
