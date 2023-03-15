// 구명보트 Lv2
// 탐욕법(Greedy)

function solution(people, limit) {
  var answer = 0;
  let n = people.length;
  people.sort((a, b) => a - b);

  // 가장 무거운 사람부터 확인
  // 아직 탑승하지 않은 가장 가벼운 사람과 함께 보내기
  let [l, r] = [0, n - 1];
  while (l <= r) {
    if (limit >= people[r] + people[l]) {
      l++;
    }
    r--;
    answer++;
  }

  return answer;
}
