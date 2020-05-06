Number paritioning is a practice largely used in processor scheduling and disk space partitioning. Number partitioning entails dividing a group of tasks (knowing time required for each) with the goal of producing multiple subsets that each have the same or similar sums.

<b>Two Approaches:</b>

In this project, I will be demonstrating two approaches to a simple two-way number partitioning problem. Both will take the same input, a set of 100 numbers ranging from 0-1000. I will (attempt) to find the best way to parition the set of 100 numbers so that each set's sum is equal or very close to the others. 

First Approach: Trivial Implementation
This approach will find all 2^n possible sets that exist and return the parted 2 arrays with the sum difference closest to 0. This approach is extremely slow O(2^n), but will find the best possible answer as it exercises all sets that oculd exist.

Second Approach: Karmarkar-Karp Heuristic
This heuristic approach preprocesses the set of elements in order to reduce time complexity to solve the problem. It will organize all elements in descending order and place the top two elements into one of two sets depending on which has a higher sum at the time, attempting to minimize the difference in sum of the two sets. This approach is not considered 'complete' as it does not always find the best answer. This algorithm has a time complexity of O(nlogn) as sorting is the most expensive operation.
