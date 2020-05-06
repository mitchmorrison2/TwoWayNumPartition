# CS 3353 Algorithms Final Project for Mitch Morrison <br>

Number paritioning is a practice largely used in processor scheduling and disk space partitioning. Number partitioning entails dividing a group of tasks (knowing time required for each) with the goal of producing multiple subsets that each have the same or similar sums.

<b>Two Approaches:</b><br>
In this project, I will be demonstrating two approaches to a simple two-way number partitioning problem. Both will take the same input, a set of 100 numbers ranging from 0-1000. I will (attempt) to find the best way to parition the set of 100 numbers so that each set's sum is equal or very close to the others. 

<b>First Approach: Trivial Implementation </b><br>
This approach will find all possible sets that exist and return the parted 2 arrays with the sum difference closest to 0. This approach is extremely slow O(n(Combination(n,k))), but will find the best possible answer because it finds the sums of every set that could exist from the initial list.

<b>Second Approach: Greedy Heuristic </b><br>
This heuristic approach preprocesses the set of elements in order to reduce time complexity to solve the problem. It will organize all elements in descending order and place the top two elements into one of two sets depending on which has a higher sum at the time, attempting to minimize the difference in sum of the two sets. This approach is not considered 'complete' as it does not always find the best answer. This algorithm has a time complexity of O(nlogn) as sorting is the most expensive operation.

----------------------------------------------------------------------------------------

<b>Running the project</b><br>
All code for this project is inside the file NumPart.py and can be executed from the terminal using 
<br>```python NumPart.py``` <br>
Output from the executable is printed to <i>OutputFile.txt</i>
