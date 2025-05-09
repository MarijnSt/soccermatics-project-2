# Project statement

1. Write code to identify passes made within 15 seconds of a shot
2. Use logistic regression to look at how the start and end coordinates of these passes determines the probability that it will be followed by a shot within 15 seconds. Think about how to transform the variables and use non-linear
3. Now do linear regression to look at how the start and end coordinates of the pass determine the probability that the shot is a goal
4. Combine these to give probability of a goal given the start and end coordinates of a pass
5. Rank players (grouped by position) in terms of their Expected Danger per 90. Compare that ranking to number of danger passes made per 90.

## Definitions
**Danger Passes**

Passes that end in a shot within a 15 second period.


**Expected Danger (xD)**

How much danger a player is contributing in attacking moves. This figure is based on the location of the passes a player makes and how likely those passes are going to lead to a goal.



## Distribution of Expected Danger and Danger Passes per 90


![Distribution of xD and Danger Passes per 90](./distribution_of_metrics_by_role.png)

In terms of danger on the ball the distribution does make a lot of sense: goalkeepers are not very dangerous and neither are most defenders. The more dangerous players are in midfield and in attack. With midfielders edging out the attackers as they are often the players creating the opportunities for attackers to finish.