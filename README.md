# Auto Update Firmware
### 自動從[CPFE](https://www.google.com/chromeos/partner/fe/)下載並刷進DUT
``` python
1. 一開始執行 './set_up.sh' 設定環境
2. 執行 './get_CPFE_file.py' 登入 Google partner account
3. 執行 './auto_update_firmware ${BOARD} ${VERSION}' 可自動去CPFE下載 FW 並刷 FW
   Ex. ./auto_update_firmware crota 14505.300.0
```
***
* 注意： 要記得workstation和DUT在同一個網域
### 自動從[CPFE](https://www.google.com/chromeos/partner/fe/)尋找想要的版本
``` python
1. 執行 './get_CPFE_last_versions.py ${BASEBOARD}' 可自動列出所有${BASEBOARD}版本
   Ex. ./get_CPFE_last_versions.py brya
2. 執行 './get_CPFE_last_versions.py ${BASEBOARD} ${VERSION}' 則是列出${BASEBOARD}指定版本
   Ex. ./get_CPFE_last_versions.py brya 14505
```

