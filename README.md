# QEMU 설치
## QEMU를 설치하기 위한 전제 조건
- Linux에 소프트웨어 패키지를 설치하기 전 리포지토리를 업데이트 해야 함
```bash
sudo apt update && upgrade    # 리포지토리 업데이트
```
- QEMU를 사용하여 VM을 설정할 수 있는지 확인하기 위해 libvirt-daemon을 설치하고 활성화해야 함 (이가 없을 경우 QEMU 또는 기타 하이퍼바이저가 작동 거부)
```bash
sudo apt install libvirt-daemon    # libvirt-daemon 설치
sudo systemctl enable libvirtd     # libvirtd 활성화
sudo systemctl start libvirtd      # libvirtd 시작
# systemctl : 서비스 제어 명령어 (systemctl [명령][서비스명] / systemctl [명령][서비스명].service)
```
---
## libvirt
- libvirt : 가상화를 관리하기 위한 오픈 소스 API 데몬이자 관리 도구
## daemon
- daemon : 사용자가 직접적으로 제어하지 않고, 백그라운드에서 돌며 여러 작업을 하는 프로그램
- 보통 데몬을 뜻하는 'd'를 이름 끝에 달고 있으며 일반적으로 프로세스로 실행
- 대개 부모 프로세스를 갖지 않음 (PPID가 1개)
## Hypervisor
- Hypervisor(하이퍼바이저) : 가상 머신과 기본 하드웨어 사이에 위치하는 소프트웨어
#### 역할
1. 하이퍼바이저는 메모리, CPU 성능, 네트워크 대역폭과 같은 하드웨어 리소스를 분할하고 분할한 리소스를 각 VM에 할당하는 역할을 함
2. 하이퍼바이저는 각 가상 머신을 격리된 상태로 유지하는 역할을 담당
  - 이를 통해 각 가상 머신은 다른 가상 머신에 영향을 미치는 문제와 독립적으로 작동
3. 하이퍼바이저는 동일한 컴퓨터에 있는 가상 머신 간 및 네트워크 간 통신을 가능케 함
---
#### 문제 발생
<img width="458" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/06d20d0b-0aff-469a-9559-6156b5b17224">
- libvirtd.service라는 서비스의 unit 파일이 시스템에 존재하지 않아 서비스가 활성화할 수 없음

#### 해결 방안
1. kvm 지원 확인
```bash
$ sudo kvm-ok                  # kvm 지원 확
INFO: /dev/kvm exists          # /dev/kvm 디바이스가 존재
KVM acceleration can be used   # 시스템이 KVM 가상화 가속을 지원
```
2. 필수 패키지 설치
```bash
$ sudo apt install -y qemu qemu-kvm libvirt-daemon libvirt-clients bridge-utils virt-manager
```
- qemu-kvm : KVM(Kernel-bassed Virtual Machine)을 사용하는 QEMU 컴포넌트(재사용 가능한 웹의 구성요소)로, 하드웨어 가속 가상화를 위해 커널 모듈과 함께 사용
- libvirt-clients : libvirt 라이브러리를 사용하여 가상화를 관리하기 위한 명령줄 도구와 클라이언트 라이브러리
- bridge-utils : Linux 브리지 네트워크를 구성하기 위한 유틸리티. 가상 머신의 네트워크 구성에 사용
- virt-manager : 가상 머신을 그래픽 사용자 인터페이스(GUI)로 관리할 수 있는 가상화 관리 도구. 일반적으로 VM을 만들고 관리하는 데 사용
- -> 위 명령어를 실행하면 시스템에 가상화 관련 패키지가 설치, 가상 머신을 만들고 관리하는 데 필요한 도구 및 라이브러리 제공
<img width="440" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/87bdaa28-b5a3-4aad-bb3c-665d321cfe7a">
: 더이상 실패 문구가 뜨지 않음 (해결 성공)

---
## QEMU 다운로드
- APT 패키지 관리자를 사용하여 설치 가능
- QEMU 웹사이트, GitHub 저장소에서 수동으로 다운로드한 후 컴파일 가능
1. QEMU 설치
```bash
sudo apt install qemu-kvm    # QEMU 설치
```
2. QEMU 빌드
```bash
sudo apt install git                                    # git 설치
git clone https://gitlab.com/qemu-project/qemu.git      # 링크에 있는 파일 복제
cd qemu                                                 # QEMU로 이동
git submodule init                                      # git 저장소에서 서브모듈 초기화
git submodule update --recursive                        # git 저장소에 있는 서브모듈 모두 업데이트
./configure
make
# git clone : Git 버전 관리 시스템을 사용하여 원격 저장소로부터 프로젝트나 코드를 복제하는 명령어
# ./configure :  소프트웨어의 빌드 프로세스를 시작하기 전에 필요한 환경 구성 및 설정을 수행
```
---
#### 문제 발생
./configure에서 파이썬 pip가 깔려있지 않다는 문구가 뜸

#### 해결 방안
1. python3 pip 설치
```bash
$ sudo apt update
$ sudo apt install python3-pip
```
- pip : 파이썬으로 작성된 패키지 소프트웨어를 설치·관리하는 패키지 관리 시스템
- 위 명령은 Python 모듈을 빌드하는 데 필요한 모든 종속성도 설치함
2. pip 버전을 확인하여 확인
```bash
$ pip3 --version
```
<img width="443" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/dc65fda8-99b2-4bbb-a6e6-376c1c52544a">
- 설치가 완료
<img width="319" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/1042ad12-5e43-435d-a5a2-6eb70ca242d5">

- bash에서 해당 파일이나 디렉토리를 찾을 수 없다는 오류 문구가 뜸
```bash
git clone https://bitbucket.org/ssoulaimane/webcontentcontrol-gambas3
cd webcontentcontrol-gambas3
./configure && make && sudo make install
```

<img width="384" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/e575b602-e4c6-4b63-96d0-59713d1fcb92">
- 에러 뜸

3. configure 스크립트가 설치되어 있는 지 확인
- configure 명령어를 실행할 수 있는 파일인 configure 스크립트가 설치되어 있는 지 확인하기 위해 아래 코드를 사용한다.
```bash
$ ls -l    # ls : 파일 목록을 출력하는 명령어, -l : long format 파일 및 디렉토리의 다양한 정보 표시
```

<img width="538" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/18764e5f-fcac-4e86-b232-0d8a024ad418">

- 확인해 보니 configure가 설치되어 있지 않음
```bash
$ sudo apt install software-name              # 에러
$ sudo apt update
$ sudo apt install software-name              # 에러
```
```bash
$ cd ~
~$ cd qemu
~/qemu$ ./configure
```
<img width="493" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/a150f69b-1861-4d8f-ba9a-b46bacbbb319">

- Sphinx를 찾을 수 없다는 문구가 뜸
```bash
sudo apt-get install python3-sphinx    # Sphinx 설치
sphinx-build --version                 # Sphinx가 올바르게 설치되었는지 확인
```
- 아직 찾을 수 없다는 문구가 뜸
```bash
sudo apt-get install ninja-build
```
- E: Unable to locate package ninga-build 라는 오류 문구가 뜸
```bash
sudo apt-get update
sudo apt-get install ninja-build
./configure
```
```bash
sudo apt-apt install libglib2.0-dev    # glib-2.0 설치
meson --reconfigure builddir           # Meson 재설정
```
- Command 'meson' not found, but can be installed with:
sudo apt install meson 라는 문구가 뜸
```bash
sudo apt install meson        # Meson 설치
./configure
```

<img width="551" alt="image" src="https://github.com/Roalzlwm/study/assets/116416194/2bbe6d2e-b985-40b8-96fb-f063756ed1f1">



---
3. Virtual Machine Manager(virt-manager) 설치
- 가상머신을 설정하고 관리하기 위한 편리한 GUI 도구
```bash
sudo apt install virt-manager
```
---
## QEMU/KVM을 사용하여 Linux 가상 머신 설정
- QEMU가 모두 설정되었으므로 테스트 진행
- 원하는 운영 체제를 설치하고 VM 구성을 시험해 보며 가장 적합한 것을 찾음
ex. Manjaro와 같은 Linux 배포판
