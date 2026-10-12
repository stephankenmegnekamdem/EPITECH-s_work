export function fizzBuzz(num)
{let str = "";
    if(num>=1){
        for(let i = 1; i<=num; i++){
            if((i%3===0) && (i%5===0)){
                str=str+"FizzBuzz, ";
            }
            else if(i%3===0){
                str=str+"Fizz, ";
            }
            else if(i%5===0){
                str=str+"Buzz, ";
            }
            else{
                 str=str+i+", ";
            }

        }
    }
    str=str.slice(0, -2);
    console.log(str);

}