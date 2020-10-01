    boolean hasPathWithGivenSum(Tree<Integer> t, int s) {
        if (t == null) // if tree Null retrun false
            return false; 
        if (t.left == null && t.right == null){ //if at last node, check if  s == t.value
            return(s == t.value); //only return true if the integer S == currValue, because recursion passed in the int S with newly updated value by removing
            //all the previous values prior so that it calculates the branchSum and checks if the value is = to the last value after subtracting all previous 
        }
        //pass in either left or right where int S, is actually updated                                                           
        return hasPathWithGivenSum(t.left, s-t.value) || hasPathWithGivenSum(t.right, s-t.value); 
    }
    
