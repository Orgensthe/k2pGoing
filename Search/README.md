# Search

## Hash Tables: Ice Cream Parlor 
[문제](https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search)

### 문제 이해
입력
t = 아이스크림 가게 수
money = 가지고 있는 돈 
n = 맛의 종류
cost = 각 맛에 대한 가격

출력
선택한 맛에 대한 cost의 인덱스(1부터)

제한 조건
항상 2개의 맛을 선택해야 한다
모든 돈을 다 써야한다

### 생각 과정
1. Counter로 dict를 만들어서 i= money-1부터 시작해서 i가 있고 money-i가 있으면 정답이라 생각했음 하지만 오답이였는데 찾는 것은 문제가 없으나 위치정보가 사라져서 몇번째인지 알 수 없음...
2. 위치, 데이터, 개수가 들어있는 dict를 만들어서 위와 같은 비교 결과로 내용을 도출해보자 (타임아웃 발생) 
3. 일단 2번을 했었을 때 무언가 반복을 돌면 안되는 것 같음 멘붕...
4. 대한님 코드를 보고 힌트를 얻음...(그저 빛) 넣으면서 검증... (대단쓰... 왜 이 생각을 하지 못했을까...)
