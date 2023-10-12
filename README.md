# chatting survice

## setting


## 사용기술

### Web Socket
- 연결이 유지되는 동안, 양뱡향 통신 지원
- 클라이언트/서버 상호 간에 즉기성이 높은 데이터 전송
- http와 동일한 포트 80/443 사용 
- 장고 채널스에서 기본 지원


### Redis Pub/Sub
서버 단에서 채팅방의 다른 유저에게 메시지 뿌리는 역화르. 유저에게 전달은 웹소켓이 담당
- 레디스 특정 채널에 구독을 하면 구독자가 됨, 레디스 특정 채널에 메세지를 publish하면 구독 중인 구독자들에게 메세지 전달
- 레디스의 pub/sub은 메세지를 전달하는 시스템임, 메세지는 보관하지 않음
- 서버 대수를 늘려 horizontal로 손쉬운 scale out을 지원


### asgiref 
- ASGI는 파이썬 비동기 웹의 표준
- 장고 WSGI/ ASGI 모두를 기본에서 잘지원, 원하는 방식 선택하면됨
    - 장고의 일반적인 뷰처리(DJANGO, DRF 등)은 WSGI 방식이 성능이 더 잘나올수 있음


### CHANNELS
- 웹소켓 처리에 대한 추상화 지원
- 웹소켓 처리에도 장고의 기능 지원 
- 손쉬운 프로세스 간의 통신, REDIS를 채널 레이어 백엔드로 지정해야함
<b>채널</b>
- Consumer Instance 내부에서 생성
- 하나의 연결마다 Consumer 클래스의 Instance가 자동 생성, 각 Consumer Instance 마다 고유한 채널명 가짐
- 그채널을 통해 Consumer Instance는 채널 레이어와 통신