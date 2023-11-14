const maxValue = (nums) => {
  let highest = Number.MIN_SAFE_INTEGER;
  for (const num of nums) {
    if (num > highest) {
      highest = num;
    }
  }
  return highest;
};
​
module.exports = {
  maxValue,
};
​