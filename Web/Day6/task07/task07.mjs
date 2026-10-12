export function objectsDeeplyEqual(cmp1, cmp2){

    if (cmp1 === cmp2) return true;
    if (typeof cmp1 !== "object" || typeof cmp2 !== "object" || cmp1 === null || cmp2 === null) {
        return false;
    }
    const keys1 = Object.keys(cmp1);
    const keys2 = Object.keys(cmp2);
    // if the key counts differ, return false
    if (keys1.length !== keys2.length){
        return false
    }
    // loop over keys1; for each key k, return false if !(k in cmp2)
    for (const k of keys1) {
        // if cmp2 doesn't have key k, return false
    if (!(k in cmp2)) {
        return false;
    }
    // if objectsDeeplyEqual(cmp1[k], cmp2[k]) is false, return false

    if (!objectsDeeplyEqual(cmp1[k], cmp2[k])) {
        return false;
    }
}

    // after the loop, return true
    return true;

}