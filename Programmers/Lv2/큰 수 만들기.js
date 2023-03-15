// 큰 수 만들기 Lv2
// 탐욕법(Greedy)

function solution(number, k) {
  var answer = "";
  let n = number.length;
  let idx = 0;
  // 이미 저장된 수보다 큰 수가 들어가는 경우
  // 저장된 작은 수는 모두 제거
  while (idx < n) {
    while (
      k > 0 &&
      answer.length !== 0 &&
      parseInt(answer.slice(-1)) < parseInt(number[idx])
    ) {
      answer = answer.slice(0, -1);
      k--;
    }
    answer += number[idx];
    idx++;
  }
  // 계속해서 작아지는 형태였다면 남은 k만큼 뒷부분을 잘라줌
  if (k != 0) {
    while (k > 0) {
      answer = answer.slice(0, -1);
      k--;
    }
  }
  return answer;
}
