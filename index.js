const list1 = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"];
// for(let i of list1){
//     console.log(i)
// }
// for(let i = 0; i < list1.length; i++){
//     console.log(list1[i])
// }
// for(let i in list1){
//     console.log(list1[i])
// }
// const price = 25
// console.log(price > 10 || price < 20);

// const getEvenNumbers = (arr) => {
//     let evenNumbers = []
//    for (let index = 0; index < arr.length; index++) {
//     const number = arr[index];
//     if(number % 2 == 0){
//             evenNumbers.push(number)
//         }

//     }
//     return evenNumbers
// }
// console.log(getEvenNumbers([1,2,3,4,5,6,7,8,9,10]));

// object oriented in Javascript
// list = [1,2,3,4]
// const list = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
// list.forEach(item => console.log(item * 2))

// remove dublicates from list
const list = [1, 2, 2, 3, 4, 4, 6, 7, 7];
const uniques = [];
for (let i of list) {
  if (!uniques.includes(i)) {
    uniques.push(i);
  }
}
// console.log(uniques)
// console.log(uniques.sort((number, index) => index - number));
// console.log(uniques.filter(number => number > 2))
// console.log(uniques.map(num => num**2));
// OOP in javascript
// class Person{
//     constructor(name){
//         this.name = name
//     }
//     talk(){
//         console.log(`Hello my name is ${this.name}`);
//     }
// }

// const person1 = new Person("wallace")
// person1.talk()
// console.log(person1.name);

// class TikTok{
//     constructor(){
//         this.name = ""
//         this.followers = 0
//         this.bio = ""
//     }
//     setName(name){
//         this.name = name
//     }
//     getName(){
//         return `Hello my name is ${this.name}`
//     }
//     addFollowers(){
//         this.followers += 1
//     }
//     removeFollowers(){
//         this.followers -= 1
//     }
//     getFollowers(){
//         return `My number of followers are: ${this.followers}`
//     }
//     setBio(bio){
//         this.bio = bio
//     }
//     getBio(){
//         return this.bio
//     }
// }

// const tiktok = new TikTok()

// tiktok.setName("wallace")
// console.log(tiktok.getName());
// tiktok.setBio("I am the best programmer ever.")
// console.log(tiktok.getBio());
// tiktok.addFollowers()
// tiktok.addFollowers()
// tiktok.addFollowers()
// tiktok.addFollowers()
// tiktok.removeFollowers()
// console.log(tiktok.getFollowers());
// random
// list = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
// randomDay = Math.floor(Math.random() * list.length)
// console.log(list[randomDay])

// const list1 = [1,2,3,4,5]
// const filter = list1.filter(item => item < 2)
// console.log(filter);
// const map = list1.map(item => item **2)
// console.log(map)
// async function fetchData(){

// }
// const fetchData = async function(){

// }
// const fetchData = async () => {
//   try {
//     const response = await fetch("https://jsonplaceholder.typicode.com/posts");
//     const data = await response.json();
//     for (let post of data){
//         if (post.id === 2){
//             for(let key in post){ 
//                 console.log(`${key}: ${post[key]}`)
//             }
//         }
//     }
//   } catch (error) {
//     console.log(error);
//   }
// };
// fetchData()
// function compareDifferences(arr) {
//   const result = [];

//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < i; j++) {
//       result[i] += Math.abs(arr[i] - arr[j]);
//       if (arr[j] > arr[i]) {
//         result[i] -= Math.abs(arr[i] - arr[j]); // Subtract if element to left is greater
//       }
//     }
//   }

//   return result;
// }

// // Test case
// const arr = [5, 1, 2, 3, 1, 2];
// const result = compareDifferences(arr);
// console.log(result); // Output: [0, 1, 3, 6, 10]
