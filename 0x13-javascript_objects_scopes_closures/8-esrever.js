#!/usr/bin/node
exports.esrever = function (list) {
  const ReverseList = [];
  for (let i = (list.length - 1); i >= 0; i--) {
    ReverseList.push(list[i]);
  }
  return ReverseList;
};
