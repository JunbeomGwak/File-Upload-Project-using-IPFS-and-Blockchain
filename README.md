# IPFS와 Blochchain을 이용한 파일 업로드 시스템
## Requirement
- Gahache
- Web3.py
- ipfshttpclient
- flask

## Description (in public)

분산형 파일 시스템에 데이터를 저장하고 인터넷으로 공유하기 위한 프로토콜인 IPFS(InterPlanetary File System) 및 모든 거래 내역을 투명하게 볼 수 있는 Blockchain을 이용하여 디지털 저작물을 영구적으로 네트워크에 업로드 할 수 있는 프로그램을 제작

## 시작
```
ipfs init &
ipfs daemon &
sudo python3 server.py &
sudo python3 gui.py &
```

### Requirement
 - go-ipfs build
```
wget https://dist.ipfs.io/go-ipfs/v0.4.17/go-ipfs_v0.4.17_linux-amd64.tar.gz
tar zxvf go-ipfs_v0.4.17_linux-amd64.tar.gz
cd go-ipfs
sudo ./install.sh
```

## 구성도
![Untitled](https://user-images.githubusercontent.com/23713051/147915276-237ae6ae-6ffc-4fb2-9187-61d9e69ee768.png)

## 과정
<img width="167" alt="KakaoTalk_20220114_164029242" src="https://user-images.githubusercontent.com/23713051/149469993-7492ec67-7fac-4f4b-a554-224b85696fa3.png">
- 저작자 이름, 생성 시간, 저작물 종류 등 정보를 입력


![KakaoTalk_20220114_164048526](https://user-images.githubusercontent.com/23713051/149469889-22482889-39bf-4aa6-ad53-0bcbd7457eba.png)
- 저작물 파일을 선택한 후, 업로드를 진행하면 해당 파일은 IPFS 네트워크에 업로드 되고, IPFS Hash를 반환 받음

![Untitled2](https://user-images.githubusercontent.com/23713051/147915328-624b5961-930e-4764-9395-81e8714514e9.png)
- 업로드가 완료 되면, 반환된 ipfs hash 및 전송된 정보를 블록체인에 기록한 후 리턴값을 반환

![KakaoTalk_20220114_164056999](https://user-images.githubusercontent.com/23713051/149469891-98289e5c-b6c9-4285-95da-f7987122ec21.png)
- 정상적으로 IPFS 네트워크에 파일이 업로드 되어있음을 확인할 수 있음.
