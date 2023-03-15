// 소수 찾기 Lv2
// 완전탐색

function solution(numbers) {
  // numbers의 원소로 만들 수 있는 수 탐색
  function DFS(S, vst) {
    if (!numberL.includes(parseInt(S))) {
      numberL.push(parseInt(S));
    }

    if (S.length >= n) {
      return;
    }

    for (let i = 0; i < n; i++) {
      if (!vst.includes(i)) {
        DFS(S + numbers[i], [...vst, i]);
      }
    }
  }

  // 해당 숫자가 소수인지 판별
  function check(num) {
    if (num < 2) {
      return false;
    }
    for (p of primeLst) {
      if (p > parseInt(Math.sqrt(num))) {
        break;
      }
      if (num % p === 0) {
        return false;
      }
    }
    return true;
  }

  // 소수 리스트 계산
  let primeLst = [];
  let maxV = 10000000;
  for (let i = 2; i < parseInt(Math.sqrt(maxV)) + 1; i++) {
    if (primeLst.length === 0) {
      primeLst.push(i);
    } else {
      let flag = false;
      for (let p of primeLst) {
        if (i % p === 0) {
          flag = true;
          break;
        }
      }
      if (!flag) {
        primeLst.push(i);
      }
    }
  }

  let n = numbers.length;
  let numberL = [];
  for (let i = 0; i < n; i++) {
    if (numbers[i] !== "0") {
      DFS(numbers[i], [i]);
    }
  }

  let answer = 0;
  for (let num of numberL) {
    if (check(num)) {
      answer += 1;
    }
  }
  return answer;
}
