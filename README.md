
Auto Generated README File
--------------------------
Wrangling with Python

	 -- Just a bunch of katas with Python

	 -- Algorithms + data structures + whatever else the mind wants to play with

	 -- Some recursive code uses rcviz for visualization of a recursive tree - cool stuff! see the rcviz fork.

	 -- Some code uses non-standard libraries



10bit10mil.py : Given 10 million 10 bit ints, sort these efficiently

2sum.py : Given an array of integers, find two numbers such that they add up to a specific target number.

3sum.py : Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

__init__.py : so Imports can work inside this directory

alt_pn.py : Take a list of positive and negative integers, and return a list with negative numbers on left and positive numbers on right while also mantaining the order of numbers in input list

array_product.py : for an input array [1,2,3] return back an array where each i is a product of elements before i and after i, excluding i. In this example the output is: [6, 3, 2]

binary_search.py : Binary Search!

bloomfilter.py : a bloom filter of /usr/share/dict/words

brackets.py : http://stackoverflow.com/questions/727707/finding-all-combinations-of-well-formed-brackets

buildingMinCost.py : There are N buildings with variable number of floors, and we want to build additional floors so that at least m buildings are of the same height.  Minimize the cost of building the floors.

BuildTree_PreorderInorder.py : Given the inorder and preorder traversal's of a tree in an array, build a tree . : http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

cake_thief.py : Maximize stealing cakes, in a bag of capacity C, where cakes are tuples of weight,profit

candies.py : Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line ( their positions are fixed), and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies given to the children.

cloneBinaryTree.py : Clone a binary tree and return the root of the cloned tree

closest_sum.py : Given a sorted array and a number x, find the pair in array whose sum is closest to x

cmd_example.py : How to build a Shell-esque Prompt interface using python

coin.py : how many ways to make change of k, given a set of coins

coinchange.py : Given N coins make change, C with the minimum number of coins. Output the coins used to make the Change. If there are more than one such sets, output them all. The same coin can be used repeatedly

coinplay.py : you and your friend are playing a game with coins, such that each coin has a value, and you can pick a coin from the start of a list or end of a list. If you begin first, and your friend is equally competent as you, what is the best choice you can make?

combinationSum.py :  Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.  All numbers (including target) will be positive integers. The solution set must not contain duplicate combinations. For example, given candidate set [2, 3, 6, 7] and target 7, A solution set is: [[7], [2, 2, 3]]

countbits.py : count the bits set in a value n

diameter_binTree.py : The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.The max diameter need not pass through the root. see: http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

dict_editdistance.py : Edit distance dicitonary problem: given a dictionary of words : {cat, bat, hat, bad, had} and two strings a, b: a = bat, b = had how to convert a->b by changing only 1 char at a time

dictPattern.py : http://www.geeksforgeeks.org/find-all-strings-that-match-specific-pattern-in-a-dictionary/

edit_distance_dynamic_rec.py : Edit distance using Dynamic programming

edit_distance_exhaustive_rec.py : Edit distance using Exhaustive Search

exp_creator.py : Given some number eg n= 222 and k=24 and a set of operations: Join, Add, Multiply, verify if k can be formed by applying the operations on n. The combination of operatsion on N leads to : 222 (all joins), 2+22(Add, Join), 2*22(Multiple,Join), 22+2,22*2 and so on..

find_majority.py : Find the majority element in a list/array if the majority element appears atleast more than half the number of times

findMinInRotatedArray.py : Find the minimum element in a sorted array that has been rotated (rotated from the right end any number of times)

genPrimes.py : Generate some Primes using a bit array - a cool technique I learnt

getMaxQueue.py : How to build a Shell-esque Prompt interface using python

graph.py : Build your own graph using this Graph Library

graph_cycle.py : detect if a graph has a cycle or not

graph_dfs.py : graph dfs traversal

hanoi.py : tower of haoi

interleave.py : Given strings ab, cd and cadb, verify that cadb is an interleaved string of ab and cd. interleaved strings can be formed by choosing one element from each of the input strings, while mantaining the original order.cadb is a valid interleave, since the elements appear in the original order of the inputs ab and cd

inverted_index_trie.py : Build an inverted index using a Trie

isBST.py : Given a binary tree is it a Binary search tree?

K_updates.py : You are given the length of an array filled with all zeros initially. Now additions(updations) will be performed over given ranges on this array. Each updation will include the range and the number to be added over that range and will be of the form: [start index, end index, increment]. You have to return the final updated array after all the updations are done. Note: The time complexity should be O(n+k) where k is the number of updations and space complexity should be O(1) [https://discuss.leetcode.com/topic/224/range-addition]

knights_tour_shortestpath.py : You are given two inputs: starting location and ending location. The goal is to then calculate and print the shortest path that the knight can take to get to the target location.

knightsTour.py : Knights tour

longestPalinpossible.py : http://www.geeksforgeeks.org/find-longest-palindrome-formed-by-removing-or-shuffling-chars-from-string/

longestRepeatedCharSubstr.py : find the longest repeated(char) substring in an input string. Eg: input = aabbbc;output = bbb , input = abc; output = a(or b or c), input=foofoofoo;output=oo

longestSubstring2chars.py : what is the size of Longest substring with at most 2 distinct characters eg: s = "eceba" output : 3 ("ece")

longestSubStrParanthesisMatch.py : find the longest substring with matching paranthesis. example: () is 2, ((()), is 4, ()(()) is 6, ((((( is 0, ()) is 2, ((((())(((() is 4

lru.py : a prototype LRU-style KV store

merge2arrs.py : Given 2 arrs: Short and Long of same size (n), that are already sorted return the sorted long array in linear time, merging the two arrays

mergeBST.py : Merge 2 BST's to form a merged balanced BST

minimumWindowSubstring.py : Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n). For example, S = "ADOBECODEBANC" T = "ABC" . Minimum window is "BANC".

minstack.py : implement a stack with the usual stack semantics but additionally also returns the Minimum value in the stack in O(1)

nearestNeighbor.py : http://stackoverflow.com/questions/20398799/find-k-nearest-points-to-point-p-in-2-dimensional-plane

nextPalin.py : Given a number what is the immediate next Palindrome number? Example, given 135, output should be 141

nqueens.py : nqueens problem

num_univalTrees.py : Given a binary tree, return the number of Unival trees . Example is here: https://crazycoderzz.wordpress.com/count-the-number-of-unival-subtrees-in-a-binary-tree/

numStairs_dyn_rec.py : How many ways can you climb N stairs, if you can take some [I, J, K...] steps? : Dynamic

numStairs_exhaustive.py : How many ways can you climb N stairs, if you can take some [I, J, K...] steps? : Exhaustive

orderString.py : https://www.careercup.com/question?id=5659201272545280

palindromeDecompisition.py : http://www.programcreek.com/2013/03/leetcode-palindrome-partitioning-java/

pascal.py : Print out the pascal triangle for value: n

pow.py : Implement the pow function efficiently

prime_factorize.py : Generate the list of prime factors for a given n. Example prime factors of 12: 2, 2, 3

printAllPathsTree.py : Given a binary tree, print out all of its root-to-leaf paths one per line

priorityQueue.py : A priority Queue

queue_using_doubly_linked.py : A queue using Linked list with forward and back pointers

queue_using_linkedlist.py : A Queue using Linked List style Nodes

queue_using_list.py : A Queue using Python Lists

quicksort.py : Quicksort!

rainfallChallenge.py : dat palantir Rain Fall Challenge

readmeGen.py : Built this README File

recursive_merge.py : a  merge sort with a recursive merge

regExMatcher.py : Build a regex Matcher for . (dot matches any single char) and * (asterix matches zero or more of the preceeding char). Given a string and a pattern(that contains dot and ansterix), output True or False if the string matches the pattern. Example : c*a*b matches aab and .* matches ab

reverse_wordsSentence.py : given a sentence like this: "Coding for Interviews contains too many gifs." Returns the sentence with the order of the words reversed, like so: "gifs. many too contains Interviews for Coding" The catch was: your function should use O(1) space.

revKlist.py : given a linked list and a value K, generate a linked list such that upto K elements are reversed. example for input 1,2,3,4,5,6,7,8 and k=5 the output list is: 5,4,3,2,1,8,7,6

robber.py : What houses must a robber steal from, to get max value, if houses are indicated by value and adjacent houses cannot be stolen

rope_cut.py : cut a rope of size n such that the product of the cuts is maximized atleast one cut must be made example: rope of size = 4 the best cut is 2,2 (2 * 2 = 4) as opposed to 3,1 (3* 1 = 3) or 1,3 or 1,2,1, 2,1,1, 1,1,1,1

search_concatenatedWords.py : given T = dogthecatcatthedog and A = ["the", "cat"] (n words of k length) output 3, 9 since the concatenation thecat and catthe is found in T at those indices. all n words should be part of the concatenation pattern, each word is size k and order does not matter

segment_tree.py : A segment tree of Min values

segmentExists.py : https://www.careercup.com/question?id=5101591666360320

skiplist.py : A skip list implemented in python borrowing from the fantastic explanation here: https://kunigami.wordpress.com/2012/09/25/skip-lists-in-python/

slidingWindowMax.py : http://articles.leetcode.com/sliding-window-maximum

snake.py : print a string sinusoidally

snake_ladder.py : snake & ladder game

sortedListToTree.py : take a sorted list, and build a binary search tree

split53.py : Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is the same, with these constraints: all the values that are multiple of 5 must be in one group, and all the values that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)

stack.py : Get a stack by using this Lib

stringPermutations.py : Write a recursive function for generating all permutations of an input string.  To start, assume every character in the input string is unique.

subsets.py : print all subsets of a given array/list

subtrees.py : what are the structurally unique binary trees that can be formed for size n?

sumString.py : http://www.geeksforgeeks.org/calculate-sum-of-all-numbers-present-in-a-string/

swallow.py : Generate Numeronyms for a word upto size 2: Example: "nailed" can be compressed to n4d, na3d, n3ed, n2led, na2ed, nai2d

tree_postOrder_iterative.py : Given a binary tree, print the post-order traversal without using recursion

tree_rightNext.py : Given a Full binary tree Populate the nextRight pointers in each node: http://www.geeksforgeeks.org/connect-nodes-at-same-level/

wildcard.py : Given a string of 0's, 1's and ?'s print out all the possible results where ?'s can be substituted for 0 or 1

