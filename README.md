# IPFS와 Blochchain을 이용한 파일 업로드 시스템
## Requirement
- Gahache
- Web3.py
- ipfshttpclient
- flask

## Description (in public)

분산형 파일 시스템에 데이터를 저장하고 인터넷으로 공유하기 위한 프로토콜인 IPFS(InterPlanetary File System) 및 모든 거래 내역을 투명하게 볼 수 있는 Blockchain을 이용하여 디지털 저작물을 영구적으로 네트워크에 업로드 할 수 있는 프로그램을 제작

##
```
ipfs init &
ipfs daemon &
sudo python3 server.py &
sudo python3 gui.py &
```

### manual
 - build
```
wget https://dist.ipfs.io/go-ipfs/v0.4.17/go-ipfs_v0.4.17_linux-amd64.tar.gz
tar zxvf go-ipfs_v0.4.17_linux-amd64.tar.gz
cd go-ipfs
sudo ./install.sh
```

## 구성도
![Untitled](https://user-images.githubusercontent.com/23713051/147915276-237ae6ae-6ffc-4fb2-9187-61d9e69ee768.png)

## 결과
![Untitled1](https://user-images.githubusercontent.com/23713051/147915322-249b0b9a-69ff-454f-8c3c-9c7af6fe31e5.png)
![Untitled2](https://user-images.githubusercontent.com/23713051/147915328-624b5961-930e-4764-9395-81e8714514e9.png)

