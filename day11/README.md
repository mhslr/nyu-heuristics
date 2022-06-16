# review of topics discussed (6/16)

# Problems & solutions
## The splitting problem
A group of students at NYU is taking N classes.
The i-th class is T[i] hours long.
Millenials have a short attention span.
You are in charge of splitting these classes,
by introducing at most B breaks.
Your goal to minimize the longest time M they would spend between breaks.

Example
```
N = 5
B = 4
T = 1 5 3 4 2
Answer
M = 2
T = 1 2+2+1 2+1 2+2 2
```

Solutions:

- Greedy (incorrect): While we have spare breaks, split the longest period evenly. Counter example:
```
T = [6], B = 2
Break 1: T = 3+3
Break 2: T = 1+2+3
-> M = 3, but 2+2+2 was possible
```

- Brute force: Try distributing the number of breaks among all classes, in all possible ways, and break each class evenly. Correct but very slow.
- Smarter brute force: Notice that in the optimal solution a longer class should have at least as many breaks as a shorter one. Sort the classes by duration and try all non-decreasing sequences of breaks that sum to B. This should reduce the number of possibilities by a large factor.
- Correct greedy. Let's assign to each class a priority: the duration of its longest period. Now we can iteratively pick the top priority class, add one break to its break count BC, recompute the longest period: (T[i]+BC-1)//BC, and reinsert it with the updated priority. M is the top priority at the end. Correctness: Any break that has been set was because the class had the top priority at some point. Removing it would make put the class' priority >= M, so we cannot remove any breaks and decrease M.
- Clever solution. For any M', it is easy to compute B', the minimum number of breaks needed. It is also clear that B'(M') is a non-increasing function. So our goal is to find the smallest M' such that B'(M') <= B. This can be achieved by binary search over M'.

## Nim game
You are given N stacks of pancakes. The i-th stack has S[i] pancakes.
Your friend challenges you to the following game: You will take turns, pick a stack and remove one or more pancakes from this stack. The player that clears the last stack wins.

Example
```
N = 3
S = 3 4 5
round 1 P1: 1 4 5
round 2 P2: 1 4 4
round 3 P1: 0 4 4
round 4 P2: 0 2 4
round 5 P1: 0 2 2
round 6 P2: 0 2 1
round 7 P1: 0 1 1
round 8 P2: 0 0 1
round 9 P1: 0 0 0
-- P1 wins
```
From this example, we can see that at round 3, P1 left two equal piles,
and was then able to mirror all his opponent's moves.
The optimal strategy takes this idea further, by answering the question:
What's an invariant that [player] can maintain, by cancelling every [opponent]'s moves?
The answer is a 0 [XOR-sum](https://en.wikipedia.org/wiki/Exclusive_or) of the piles' values. Let's go through our example again:
```
3 = 011 base 2
4 = 100 base 2
5 = 101 base 2
XOR 010 : same as carry-less addition
```

- If XOR is 0, the current player will change it to some positive integer. (since we are modifying one number in the sum)
- Otherwise, it is always possible to bring it back to 0 (winning strategy):
Some number has to have the leftmost set bit of XOR set to 1 as well. XORing this number with XOR will decrease its value and make XOR = 0.

You can check that this was P1's strategy.

## Minimax: Tic Tac Toe
Implemented in `tictactoe.py`.
Let's compute the expected score of a board, assuming both players have optimal strategies. In the file, `score` is 1 if X is sure to win, -1 if O is sure to win, and 0 if the game will end in a draw. X will maximize score, while O will try to minimize it. At every stage, a player picks its best move, by taking either `max` or `min` over the best score their opponent can get after a given move.
We also kept track of the history. The current implementation will find the best sequence of moves to make from a starting board to win or avoid defeat, if possible, assuming the other player has the optimal strategy.

## Numeric methods

- [Simpson's 1/3 rule](https://en.wikipedia.org/wiki/Simpson%27s_rule)
is a technique for numerical integration, which gives a second order estimate of an integral, yielding better results that box or trapezoid estimations for fewer sample points.
- [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method)
is a technique for finding the root of a function (x | f(x)=0). It converges fast, but requires the initial guess to be sufficently close (or the function to have a small 2nd order derivative). Starting from some x0, we iterate using `x[n+1] = x[n] + f(x[n]) / f'(x[n])`. PS: f' can be approximated using (f(x)-f(x+h)) / h.
- [Ternary search](https://en.wikipedia.org/wiki/Ternary_search). Suppose you have f, a function that increases on (l,x) and decreases on (x,r). You know l,r and want to find x and its maximum f(x). With ternary search, you will split (l,r) in three at ml and mr.
If f(ml) > f(mr), you know that x < mr (and f(ml) < f(mr) implies x > ml). You can reduce the search space and repeat this process to find tight bounds on x (after n steps, rn-ln = (r-l)\*(2/3)^n).
- The [Lotka-Volterra equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) are a pair of nonlinear differential equations (hard to solve/integrate by hand in general) that model the evolution of prey and predator's population.
We can simulate the evolution of this model and approximate the continuous change in these variables by stepping by small time steps: `x[n+1] = x[n] + dxdt[n] * dT`. You can see the impact of varying dT in seeing how much the solution diverges (this process is known to be cyclic).
This formula is called the [Euler forward method](https://en.wikipedia.org/wiki/Euler_method). Better approximations are possible using [Runge-Kutta methods](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods).

## ML: Text processing and classification
We did not review this, some common text classification techniques are used in this [Colab notebook](https://colab.research.google.com/drive/1yZow-GIh7eKv-3smR1mFisqPVppOw82a?usp=sharing).
Feel free to skip the first part, where the dataset is downloaded and prepared for the task.
Our model will essentially look at the word counts as features (this representation is called Bag-of-Words or BoW) to predict the category.
But first we apply some transformations:

- splitting and counting the words (part of TfidfVectorizer).
- re-weighting words, to value rare ones more than the common ones (Tfidf), as they might be more specific to one category.
- for our model to train faster, we reduce the dimension of our features from vocabulary size (140'000 distinct words) to 100, using a Singular Value Decomposition, very similar to Principal Component Analysis.

Finally, we use a Gaussian Naive Bayes model to fit our data and predict the 20 classes.
Similar results can be obtained using a Logistic Regression.
64% accuracy is not too bad, considering that some classes were quite similar, but better results can be achieved using [Language Models/Transformers](https://huggingface.co/docs/transformers/quicktour) (recent advances in ML).
