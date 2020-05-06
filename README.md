# CS 3353 Algorithms Final Project for Mitch Morrison <br>

Number paritioning is a practice largely used in processor scheduling and disk space partitioning. Number partitioning entails dividing a group of tasks (knowing time required for each) with the goal of producing multiple subsets that each have the same or similar sums.

# <b>Two Approaches:</b><br>
In this project, I will be demonstrating two approaches to a simple two-way number partitioning problem. Both will take the same input, a set of 20 unique numbers ranging from 0-1000. I will partition the set so that each set's sum is equal or very close to the others. 

# <b>First Approach: Trivial Implementation </b><br>
This approach will find all possible sets that exist and return the parted 2 arrays with the sum difference closest to 0. This approach is extremely slow O(n(Combination(n,k))), but will find the best possible answer because it finds the sums of every set that could exist from the initial list.

# <b>Second Approach: Greedy Heuristic </b><br>
This heuristic approach pre-processes the set of elements to the complexity of the problem. It will organize all elements in descending order and place the top two elements into one of two sets depending on which has a higher sum at the time, attempting to minimize the difference in sum of the two sets. This approach is not considered 'complete' as it does not always find the best answer. This algorithm has a time complexity of O(nlogn) as sorting is the most expensive operation.

----------------------------------------------------------------------------------------

# <b>Running the project</b><br>
All code for this project is inside the file NumPart.py and can be executed from the terminal using 
<br>```python NumPart.py``` <br>
Output from the executable is printed to <i>OutputFile.txt</i>

----------------------------------------------------------------------------------------
<b>Project Source</b><br>

Korf, Richard E. “A Complete Anytime Algorithm for Number Partitioning.” Artificial Intelligence, <br> vol. 106, no. 2, 1998, pp. 181–203., doi:10.1016/s0004-3702(98)00086-1.
