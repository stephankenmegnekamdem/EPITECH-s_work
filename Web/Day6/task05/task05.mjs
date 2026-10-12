export function range(start, end, step){
    if (step === undefined){
        if(start<end){
            step=1;
        }
        else{
            step=-1;
        }
    }

    const arr=[];
    if (step>0){
         for(let i = start; i<=end; i+=step){
        arr.push(i);
    }
    }

   else{
       for(let i = start;i>=end; i+=step){
        arr.push(i);
    }
    }
    return(arr);
}
//let i = start; step > 0 ? i <= end : i >= end; i += step u can use this at for loop to have only one loop
