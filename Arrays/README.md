# Arrays

## New Year Chaos(2020.08.11 ~ 12)

[문제]([https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays](https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=arrays))

### 생각 과정
1. 주어진 배열에서 같은 크기의 배열을 빼면 값이 나오는데 이 때 양수는 모두 더하고 음수 중에서 2를 넘어가지 않는 것은 절대값으로 더해주었다(틀림, 음수 중에서도 의지와 상관없이 밀렸으나 중간에 한번 앞으로 간 것이 있을 수 있음)
2. 원래 배열에서 주어진 배열을 만들어 가는 과정을 코드로 직접 보여주는 법을 생각했음(배열의 원소를 옮기고 빼고 하는 방식으로... 타임아웃)
3. 아침에 승훈님(센세)의 해법을 듣고 그대로 실현... 계속 반복해서 배열을 조작하지 않고 뒤에서부터 앞으로 이동하면서 자기보다 앞의 2개만을 조사해서 자기보다 작으면 원래 그 자리에 있는 것 크면 움직인 것이므로 총합에 더하기.. 그리고 원래 자신의 위치보다 2가 많으면 Chaotic 

## Minimum Swaps 2(2020.08.31 ~ 09.01)
[문제]([https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays])

### 생각 과정
1. 앞에와 뒤에의 차이가 있으면 변곡이 생기면 해당 자리끼리 교환하는 방법 >> 테스트케이스 몇개 진행해보니 올바르지 않음
2. 좌에서 우로 우에서 좌로 탐색하면서 변곡이 생기는 부분에서 서로 교환 >> 테스트케이스 몇개 진행해보니 올바르지 않음
3. 하나를 잡아두고 해당 인덱스에 와야할 값을 찾는 방법 >> 타임아웃 발생
4. 위에 것을 그대로 가되 탐색을 할 때 인덱스만 찾는 것이 아니라 같이 바꿔즈는 작업 수반

## Array Manipulation(2020.09.13)
[문제]([https://www.hackerrank.com/challenges/crush/problem?h_l=interview&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays])
### 생각 과정
1. 단순히 모든 범위에 해당하는 숫자를 차례대로 더해서 제일 큰 수 찾기(타임아웃 발생)
2. 잘 모르겠음..(인터넷의 풀이를 보니 변곡을 이용... 정확히 어떻게 되는 건지는 이해가 안되지만 일단 되기는 됨)