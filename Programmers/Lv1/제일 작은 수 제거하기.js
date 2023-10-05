// 제일 작은 수 제거하기 Lv1
// 연습문제

// forEach splice
function solution(arr) {
  if (arr.length === 1) return [-1];
  var value = arr[0];
  var idx = 0;
  arr.forEach((n, i) => {
    if (n < value) {
      value = n;
      idx = i;
    }
  });
  arr.splice(idx, 1);
  return arr;
}
