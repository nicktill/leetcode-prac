function compressedString(message) {
    var output = ''; //return output initalize to empty
    var letterCount =1; //letter count initalized to 1 to signify how many letters there are    
    for(var i =0; i< message.length-1; i++){ //loop through message
        if(message[i] == message[i+1]){ //if an index is the same as next
            letterCount++; //increase letterCount
            //if there are mulltiple in a row, it will keep checking how many letters
            //there are in a row and update letter count
        }
        else{
            output+=message[i]; //if index is not equal to next, then add those letters before to output
            if(letterCount!= 1){ //if there was more than one letter
                output+=letterCount;
            }
            letterCount=1; //reset the counter back to 1
        }
    } 
    output+=message[i]  //adding last letter
    if(letterCount>1){  //if multiple letters adding that
        output+=letterCount;
    }
    
    return output //return
}
