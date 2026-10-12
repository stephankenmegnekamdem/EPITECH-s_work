export function arrayFiltering(array, test){
    const new_array=[]
for(let i=0; i<=(array.length-1); i++){

    if (test(array[i])){
        new_array.push(array[i])
    }
}

return new_array;
}
