// 같은 숫자는 싫어 Lv1
// 스택/큐

// forEach push 20 ms 83MB
function solution(arr) {
  const answer = [];
  arr.forEach(n => {
    if (answer.length > 0) {
      answer[answer.length - 1] !== n && answer.push(n);
    } else answer.push(n);
  });
  return answer;
}
