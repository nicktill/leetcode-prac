class Solution:
#[1,3] [2,6] => [1,6]
      def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: 
            return [] 
        intervals.sort() 
        stack = [intervals[0]] #push the first element into the stack
        #fair pair pushed to stack, i.e [1,3]  
        for current in intervals[1:]: #start from second index (since first pair is in stack)
            # if our curr starter element, I.E for [2,6] elem would be 2
            #is LESS OR EQUAL to our stack end elem, I.E for stack =[1,3] would be 3
            if current[0] <= stack[-1][1]:  #first case: if 2 <= 3:
               #update end of stack index to be maxOf(currEnd, nextEnd)
                stack[-1][1] = max(current[1], stack[-1][1])
            else:  #otherwise the current interval cannot be merged and add it
                stack.append(current)
        return stack
