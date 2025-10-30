# Jhas_optimality
The python code implementation for the Research Paper : "Assignment problem (maximization): A new approach"

# Publication

Title: Assignment Problem (Maximization): A New Approach
Link : https://www.mathsjournal.com/archives/2025/vol10/issue10/PartA/10-9-20
Journal: International Journal of Statistics and Applied Mathematics
Volume: 10, Issue 10
Year: 2025
Pages: 29-32

# The Traditional Challenge
The standard Hungarian algorithm for maximization problems requires:

1) Construction and manipulation of loss matrices
2) Complex marking and unmarking of entries
3) Row and column cancellation operations
4) Multiple transformation steps before reaching optimality

# Our Approach: Swap-Based Optimization
This algorithm takes a fundamentally different approach by:

1) Starting with a Greedy Solution and constuct an initial basic feasible solution
2) Iteratively select the maximum available value from the cost matrix
3) Assign each row to a column, ensuring no row or column is used twice
4) This provides a good starting point but not necessarily the optimal solution
5) now building upon this Iterative Swap-Based Refinement, Examine all possible swaps between current assignments
6) For each potential swap, calculate the profit:
Gain: Improvement in value for the row being reassigned
Loss: Reduction in value for the row being displaced
Net Profit: Gain minus Loss
7) Execute swaps that yield positive profit
8) Continue until no profitable swaps remain (optimality criterion)


Final Goal : Reaching Optimality

The algorithm converges when no swap can improve the total assignment value
This convergence guarantees an optimal solution
The approach is intuitive and requires minimal bookkeeping 
