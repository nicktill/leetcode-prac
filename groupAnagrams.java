import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

//GroupAnagrams (medium)
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]

public class groupAnagrams {
    class Solution {
        public List<List<String>> groupAnagrams(String[] strs) {
            List<List<String>> groupedAnagrams = new ArrayList<>(); //list of anagrams used for returning
            HashMap<String, List<String>> map = new HashMap<>(); //hashmap that maps sorted string (keys) to its anagrams list (values)
            for(String current: strs){ //iterate among the strings
                char[] characters = current.toCharArray();  //map them to a character array 
                Arrays.sort(characters); //sort the character array
                String sortedKey = new String(characters); //set it back to a string thats now sorted
                if(!map.containsKey(sortedKey)){ //if hashMap doesnt contain this key, add it along with a empty arrayList
                    map.put(sortedKey, new ArrayList<>());
                }

                map.get(sortedKey).add((current)); //adds the current unsorted string to the associated listString values of anagram key
            }
            //add the values (from the k,v of hashmap into the )
            groupedAnagrams.addAll(map.values());
            return groupedAnagrams;
            
            
        }
    }
    
}
