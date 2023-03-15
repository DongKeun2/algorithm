// 조이스틱 Lv2
// 탐욕법(Greedy)

function solution(name) {
  var answer = 0;
  // 'A'에서 해당 문자로 변환하는 데 필요한 조작 횟수
  let n = name.length;
  for (let i = 0; i < n; i++) {
    answer += Math.min(name.charCodeAt(i) - 65, 91 - name.charCodeAt(i));
  }

  // 각 자리에서 'A'를 사이에 낀 다른 문자 탐색
  // 오른쪽으로 시작하여 i를 찍고 돌아가는 경우 or 왼쪽으로 시작하여 j를 찍고 돌아가는 경우
  // 만약 뒤에 'A'만 존재한다면, i를 끝으로 하는 경로는 시작지점에서 i번째까지 가는 것이 최소
  let tmp = 20;
  for (let i = 0; i < n; i++) {
    let flag = false;
    for (let j = i + 1; j < n; j++) {
      if (name[j] !== "A") {
        tmp = Math.min(tmp, i * 2 + n - j, (n - j) * 2 + i);
        flag = true;
        break;
      }
    }
    if (!flag) {
      tmp = Math.min(tmp, i);
    }
  }
  answer += tmp;
  return answer;
}
