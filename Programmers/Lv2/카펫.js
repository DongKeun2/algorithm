// 카펫 Lv2
// 완전탐색

function solution(brown, yellow) {
  var answer = [];
  // n + m = brown/2 + 2
  // nm = yellow + brown
  for (let n = 1; n < 2500; n++) {
    let m = (yellow + brown) % n ? null : (yellow + brown) / n;
    if (m && n + m === brown / 2 + 2) {
      answer = [m, n];
      break;
    }
  }
  return answer;
}
