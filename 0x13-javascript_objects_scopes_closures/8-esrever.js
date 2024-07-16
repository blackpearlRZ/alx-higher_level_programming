#!/usr/bin/node

exports.esrever = function (list) {
  function swap (list, i, j) {
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }

  for (let i = 0; i < list.length / 2; i++) {
    swap(list, i, list.length - i - 1);
  }
  return (list);
};
