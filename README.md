# IPFS와 Blochchain을 이용한 파일 업로드 시스템
## Requirement
- Gahache
- Web3.py
- ipfshttpclient

tcp:6666

- KVM must be available

AWS generally does not support virtualization based on hardware. Therefore, you must use AWS ec2 bare metal instances that have a high price.
Alternatively, it is recommended to setup on the local PC.


## Description (in public)

분산형 파일 시스템에 데이터를 저장하고 인터넷으로 공유하기 위한 프로토콜인 IPFS(InterPlanetary File System) 및 모든 거래 내역을 투명하게 볼 수 있는 Blockchain을 이용하여 디지털 저작물을 영구적으로 네트워크에 업로드 할 수 있는 프로그램을 제작

## Run
### auto
```
run ganache

sudo ipfs init 
sudo ipfs daemon&
sudo python3 server.py &
sudo python3 gui.py
```

### manual
 - build
```
wget https://dist.ipfs.io/go-ipfs/v0.4.17/go-ipfs_v0.4.17_linux-amd64.tar.gz
tar zxvf go-ipfs_v0.4.17_linux-amd64.tar.gz
cd go-ipfs
sudo ./install.sh
```
 - run
`ipfs init`, 
`ipfs daemon`
## 구성도
![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a1ba582-a0b1-4a5c-a068-8d6cb4082789/Untitled.png)


