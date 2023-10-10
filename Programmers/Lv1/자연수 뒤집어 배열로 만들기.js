// 자연수 뒤집어 배열로 만들기 Lv1
// 연습문제

// Array.from String reverse
function solution(n) {
  return Array.from(String(n), x => Number(x)).reverse();
}
