# 200320 11:55
# Chapter06-04

# 병렬성(Parallelism)
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지합니다. -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일되었습니다. -> 그래서 매우 사용하기 쉽습니다.
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2

# GIL(Globla Interpreter Lock): 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 
# -> 문제점을 방지하기 위해 GIL이 실행됩니다.
# -> 즉 리소스 전체에 락이 걸린다. 
# -> Context Switch(문맥 교환)

# GIL을 우회하려고: 멀티프로세싱을 사용합니다, CPython을 사용합니다.

import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 10000000]

# 동시성 합계 계산 메인함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1)) # sum이 누적시켜줌

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST)) # 미정일 때 코딩하는 법
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor: # alias를 줄게요
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포멧
    msg = '\n Result -> {} Time : {:.2f}s' # 엔터 쳐준거죠
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))

# 실행하는 시점도 지금까지는 그냥 실행했지만, 우리가 메인함수의 진입점을 알려줘야 됩니다.
if __name__ == '__main__': # 지금 이 파일을 실행하는게 메인파일에서 실행을 한다면
    main()
# 안그러면 멀티프로세싱 실행할 때 작업이 안됩니다. 시작점이 요 코드가 없으면