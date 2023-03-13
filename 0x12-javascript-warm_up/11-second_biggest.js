#!/usr/bin/node

const nums = process.argv.slice(2);

if (nums.length < 2) {
  console.log(0);
} else {
  for (let i = 0; i < nums.length; i++) {
    nums[i] = parseInt(nums[i]);
  }
  nums.sort(function (a, b) { return b - a; });
  console.log(nums[1]);
}
