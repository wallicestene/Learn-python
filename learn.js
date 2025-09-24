const fs = require("fs");
const path = require("path");

// creating a directory and removing a directory
const manipulateDirectory = (name) => {
  // creating a directory
  if (!fs.existsSync(name)) {
    fs.mkdir(name, (err) => {
      if (!err) {
        console.log("Directory created successfully");
      } else {
        console.log(err);
      }
    });
  } else {
    fs.rmdir(name, (err) => {
      if (!err) {
        console.log("Directory removed successfully");
      } else {
        console.log(err);
      }
    });
  }
};
// manipulateDirectory("learning nodejs");

// creating  a server and reading & writing files
const http = require("http");
const { log } = require("console");
const server = http.createServer((req, res) => {
  const url = "/";
  if (req.url === url) {
    fs.readFile("log.html", (err, data) => {
      res.writeHead(200, { "Content-type": "text/html" });
      res.write(data);
      return res.end();
    });
  } else if (req.url === url + "server") {
    res.writeHead(200, { "Content-type": "text/html" });
    res.end("<h1>This is the server</h1>");
  }
});
//   listening to the sever
// server.listen(3000);



// Leet code
/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = (nums) => {
  let k = 1;
  for (let i = 1; i < nums.length; i++) {
    const element = nums[i]
    if (nums[k] !== element - 1) {
      k++
      nums[k] = element
    }
  }
};
// removeDuplicates([1, 1, 2, 2, 3, 4, 5, 5]);

var lengthOfLastWord = function (s) {
  //  let words = s.trim().split(" ").pop()
  //  return words.length;
  let words = s.split(" ")
  for (let i = words.length - 1; i >= 0; i--) {
    if (words[i].length > 0) {
      return words[i].length
    }
  }
};
// log(lengthOfLastWord("Hello World google "));
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

const addTwoNumbers = (l1, l2) => {
  let carry = 0;
  let result = [];
  let i = 0;

  while (i < l1.length || i < l2.length || carry) {
    const sum = (l1[i] || 0) + (l2[i] || 0) + carry;
    result.push(sum % 10);
    carry = Math.floor(sum / 10);
    i++;
  }

  return result;
}
// console.log(addTwoNumbers([2, 4, 3], [5, 6, 4]));
// 

// Practice leet code
// transform matrix
const transformMatrix = (matrix) => {
  // reverse the rows of the matrix
  const newMatrix = matrix.reverse()

  // filter out columns with odd indexes
  const result = newMatrix.map(row => (
    row.filter((_, index) => index % 2 === 0)
  ))

  return result
}
// console.log(transformMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
