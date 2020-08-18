# Stacks and Queues

## Balanced Brackets 
[문제](https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues)

### 문제 이해
입력
n = 테스트 케이스 개수
s = 배열(괄호가 들어있는)

출력
return YES, NO 

제한 조건
서로 짝이 맞아야한다.
항상 먼저 왼쪽 괄호가 먼저 와야하고 그 이후에 순서에 맞게 해당하는 괄호가 와야한다. 

### 생각 과정
1. 좌측 괄호들을 스택에 넣고 우측 괄호가 나오면 스택의 맨 위 값을 가져와서 비교한다. 주어진 배열을 다 돌았는데 스택에 값이 남아 있으면 문제가 있다
