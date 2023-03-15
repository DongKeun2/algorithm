// H-Index Lv2
// 정렬

function solution(citations) {
  var answer = 0;

  // 완전탐색
  let n = citations.length;
  for (let i = 0; i <= n; i++) {
    let cnt = 0;
    for (let j = 0; j < n; j++) {
      if (citations[j] >= i) {
        cnt++;
      }
    }

    if (cnt >= i && i >= n - cnt) {
      answer = Math.max(answer, i);
    }
  }

  return answer;
}
