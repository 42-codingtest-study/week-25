//모르겠어요 진짜로 찾아도 안나와요 그냥 모르겠어요 나는 멍청이~ 야야 뚜룻뚜룻뚜룻뚜룻 그냥 난 멍청이야 ~ 
// 외톨이야~ 외톨이야~ 다리다리다라뚜 
// 겁쟁이야~! 워! 전쟁이야~ 워!
// 야야~ 야야야야~ 야야야야 야야야~
// abcdefu
// 하기싫어요 push_swap도 leak터져서 개빡침 
// 그냥 잉여인간으로 살래 난 멍청해 난 쓸모없어 난 쓰레기야
// 그냥 술먹자 술먹자~
// 맨날 술이야~ 맨날 술이야~
// 수리수리 마수리
// 수리남엔 무슨일이세요 형제님~ 찍찍찍~ 쥐세끼가 끝까지 말이많네
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let N = input[0] * 1;
  const tree = new Array(N + 1);
  for (let i = 0; i < N + 1; i++) {
    tree[i] = {};
  }
  for (let i = 1; i < N + 1; i++) {
    const [now, left, right] = input[i].split(" ").map(Number);
    tree[now].left = left;
    tree[now].right = right;
  }
  const visited = [...tree];
  let result = 0;
  console.log(visited);
  if (tree[1].left !== -1 && visited[1].left !== -2) {
    result += 1;
    visited[1].left = -2;
  }
}
