### FastAPI & Redis
* 시각화 결과를 앱에서 확인

![fastAPI APP](https://github.com/SmartDigitalAg/APSIM_Scenario/assets/93760723/c0847601-58b0-46b1-b80c-e86776ac118e)

1. Redis 설치 및 설정 (Ubuntu)
   * 레디스 설치 전
    ```angular2html
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```
    
   * redis-server 설치
    ```angular2html
    $ sudo apt-get install redis-server
    ```
    
   * redis 설치 확인
    ```angular2html
    $ redis-server --version
    ```

   * 현재 서버의 총 메모리 확인
   ```angular2html
   $ vmstat -s
   ```
   ![redisserver](https://github.com/SmartDigitalAg/APSIM_Scenario/assets/93760723/d19daa76-506d-4aaa-8ab2-b7d229e48851)
   
   * 레디스 재시작 및 상태 확인
   ```angular2html
   # 재시작
   $ sudo service redis-server start 
   # 상태 확인
   $ sudo service redis-server status
   ```
   
   * 포트 오픈 확인
   ```angular2html
   $ netstat -nlpt | grep 6379
   ```
   
2. python 레디스 설치 및 연결
```angular2html
$ pip install redis
```
```python
import redis

# 레디스 연결
r = redis.StrictRedis(host='localhost', port=6379, db=0)
```

3. redis-cli에서 사용
   * redis-cli 접속
   ```angular2html
   $ redis-cli
   ```

   * 저장된 키 확인
   ```angular2html
   127.0.0.1:6379> keys *
   ```

   * 저장된 키 삭제
   ```angular2html
   127.0.0.1:6379> del 키
   ```

   * 저장된 키 전체 삭제
   ```angular2html
   127.0.0.1:6379> flushall
   ```
