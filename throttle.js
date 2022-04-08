// Assume that you are given an expensive function lets say
// const expensive= function(){
//   console.log("this makes some expensive api call")
// }
// And it is attached onto a click listener of some button lets say:
// <button onclick="expensive()">Expensive button</button>
// Now currently everytime we hit the button we make the expensive API call so I want you to write a function that will make the call after a delay of T milliseconds only and ignores any calls that are made in between
// --0 time-- newFunc() (this one executes) newFunc() newFunc() --T time passes-- newFunc() (this one executes) .....


const betterFunction = function (func, T) {
    let isExecutable = true;
    return function () {
        let args = arguments
        let context = this
        if (isExecutable) {
            func.apply(context, args)
            isExecutable = false
            setTimeout(() => {
                isExecutable = true
            }, T)
        }
    }
}
