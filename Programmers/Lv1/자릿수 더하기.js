// 자릿수 더하기 Lv1
// 연습문제

// 형 변환 String, Number
function solution(n) {
  var answer = 0;
  const str_n = String(n);
  for (let i = 0; i < str_n.length; i++) answer += Number(str_n[i]);
  return answer;
}
