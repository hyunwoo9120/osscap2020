# osscap2020 Racing Matrix

## 2020 오픈소스기초설계 프로젝트

### [Racing Matrix]

라즈베리파이와 led matrix, pygame 등의 모듈을 이용하여 레이싱게임을 구현하였다.<br>
플레이어가 장애물을 피한다는 설정과 더불어 장애물을 제거하는 destruct 아이템, HP를 회복하는 heal 아이템을 구현했다.<br>
각 게임 진행상황에 따른 BGM과 효과음을 두어 기존의 레이싱 게임에서 차별성을 두었다.<br>
조건에 따라 게임이 종료되면 플레이 시간을 점수로 받아 플레이어의 총 순위를 보여준다.<br>
플레이어의 이름과 점수가 파일에(.pickle) 저장되며 시작화면에서 상위(1~3위) 플레이어의 이름을 출력한다.<br>

### 1. 필요한 모듈 설치

- pygame
```C
$ python3 -m pip install -U pygame --user
```

- GPIO package
```C
$ sudo apt-get update
$ sudo apt-get install rpi.gpio
```

- numpy
```C
$ sudo apt-get install python3-numpy
```

- keyboard
```C
$ pip install keyboard
```

### 2. 사용법

- 게임 시작하기
```C
$ git clone https://github.com/hyunwoo9120/osscap2020.git
$ cd ./osscap2020/playRacingMatrix/
$ sudo python3 main.py
```

#### 시작화면 / start
1. BGM on/off
    - 'o' 키를 통해 소리를 ON / OFF 한다.
2. 랭킹 출력 (1~3위)
    - 입력받은 '플레이어 이름'과 플레이어의 '플레이 시간'을 기록해 플레이 시간이 긴 플레이어 이름 3개가 출력된다.
3. 유저 네임 등록
    - 터미널에 '사용자의 이름을 입력하세요: '가 출력될 때까지 엔터 키를 누른다.
    - 키보드로 플레이어의 이름을 등록한다. (영문, 숫자, 스페이스만 입력해야한다.)
    - 플레이어의 이름을 입력하면 바로 게임이 시작된다.

#### 게임 화면 / playRacing
1. 플레이 시간(초)
    - 게임화면으로 넘어가면 0초부터 카운트된다. (0.1초 => 1점)
    
2. 플레이어
    - 키보드'a'(좌),'d'(우)를 통해 좌,우로 이동한다.
    - hp < 50 : 차량을 빨간색으로 출력한다.
    - 50 <= hp < 110 : 차량을 초록색으로 출력한다.
    - 110 <= hp <= 160 : 차량을 파란색으로 출력한다.
    
3. 장애물
    - 3개의 라인 중 랜덤한 위치에서 장애물이 내려온다.
    - 장애물에 한 번 부딪히면 1초동안 다른 장애물에 부딪혀도 hp가 감소되지 않는다.
    - 단, 다른 장애물에 겹쳐진 상태로 1초가 지나면 hp가 감소할 수 있으니 주의해야 한다.
      
4. HP 게이지(160, 16칸)
    - 플레이어가 장애물에 1번 충돌씩 hp가 60 감소하고 게이지가 6칸 깎인다.
    - hp < 50 : 게이지를 빨간색으로 출력한다.
    - 50 = h < 110 : 초록색으로 출력한다.
    - 110 = h <= 160 : 파란색으로 출력한다.
    
5. 아이템(Destruct/Heal)
    - 3개의 라인 중 랜덤한 위치에서 랜덤한 아이템이 내려온다.
    - 아이템을 획득 시 아이템 효과와 함께, 1초동안 다른 장애물에 부딪혀도 hp가 감소되지 않는다.
      + Destruc 아이템 획득 시, 화면에 있는 모든 장애물이 제거된다.
      + Heal 아이템 획득 시, hp가 40이 증가하고 게이지가 4칸 채워진다.
      
6. 플레이 종료
    - 플레이어의 HP가 0이 될 경우 게임을 종료한다.
    - 'q'키를 눌러 플레이를 종료한다.
    - 플레이 종료 시 종료 화면으로 이동한다.

#### 종료 화면 / gameOver
1. 플레이어 이름/플레이어 랭킹/홈 아이콘(장식)/플레이어 점수
    - 플레이어의 닉네임, 랭킹, 플레이어 점수(플레이 시간)를 출력한다.
    
2. 추가 플레이 혹은 종료
    - 'Enter'키를 눌러 시작화면으로 이동한다.
    - 'q'키를 눌러 게임을 완전히 종료한다.
