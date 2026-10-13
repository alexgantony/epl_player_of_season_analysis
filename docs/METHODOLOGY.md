# POTSI Methodology — Living Note

### Layer 1: Position-Specific Percentile

Standardize every raw statistic by comparing players only within the same position. 

**Question:**

> How **good** is the player in each individual statistic compared with players in the same position?

| | |
|---|---|
| **Input** | **Raw Statistics** |
| **Output** | **Feature Percentile Score** |

### Layer 2: Category Composite Scores

Combine related feature percentiles into broader football abilities using weighted averages.

**Question:**

> How good is the player in each core football skill?

Here related percentiles scores is combined into broader football concepts. 

| | |
|---|---|
| **Input** | **Feature Percentile Score** |
| **Output** | **Category Composite Score** |

### Layer 3: Position Performance Score

Aggregate the category scores into a single overall performance score for each player's position.

**Question:**

> How well did the player perform overall relative to others in the same position?

| | |
|---|---|
| **Input** | **Category Composite Scores** |
| **Output** | **Position Performance Score** |


### Layer 4: Context Adjustment Score

Adjust the position performance score to account for the player's influence on team success. 

**Question:**

> How much did the player's performances influence their team's success?

| | |
|---|---|
| **Input** | **Position Performance Score** |
| **Output** | **Context-Adjusted Performance Score** |

### Layer 5: Final POTSI Score

Apply availability and consistency adjustments to produce the final Player of the Season score. 

**Question:**

> How valuable was the player over the entire season?

| | |
|---|---|
| **Input** | **Context-Adjusted Performance Score** |
| **Output** | **Final POTSI Score** |


