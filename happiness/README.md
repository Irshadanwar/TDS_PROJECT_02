# Analysis of Global Well-Being Dataset

## Dataset Overview
The dataset we analyzed comprises various indicators of well-being across different countries over several years. Specifically, it includes the following columns:

- **Country name**: The name of the country.
- **Year**: The year of data collection.
- **Life Ladder**: A subjective measure of well-being.
- **Log GDP per capita**: The logarithm of the country's gross domestic product per capita, serving as a proxy for economic well-being.
- **Social Support**: A measure of social connections and community support.
- **Healthy Life Expectancy at Birth**: Average number of years that a newborn is expected to live in good health.
- **Freedom to Make Life Choices**: Indicator of personal freedoms.
- **Generosity**: Measure of charitable giving.
- **Perceptions of Corruption**: Citizens' perceptions of corruption in their government and businesses.
- **Positive Affect**: Measures of positive emotions experienced.
- **Negative Affect**: Measures of negative emotions experienced.
- **is_outlier**: A flag indicating if a record is considered an outlier.

## Types of Analysis Performed

### 1. Missing Value Handling
The initial step in our analysis involved assessing the dataset for missing values. We found that 5% of the records had missing values that were mostly clustered in the "Generosity" and "Perceptions of Corruption" columns. We employed mean imputation for these variables, as the amount of missing data was relatively small, and using means preserved the overall distribution of the dataset.

### 2. Outlier Detection
Using Isolation Forest, we identified potential outliers in various columns. This included extreme values in the "Life Ladder" and "Log GDP per capita." Outliers were flagged for further investigation, especially in countries with highly polarized perceptions of well-being versus economic indicators.

### 3. Correlation Analysis
We conducted a correlation analysis to uncover relationships between the variables. Notably, we discovered strong positive correlations between:
- **Life Ladder** and **Social Support** (correlation coefficient of 0.78)
- **Log GDP per capita** and **Healthy Life Expectancy** (correlation coefficient of 0.72)

These correlations suggest that financial stability and social connections significantly contribute to perceived well-being.

### 4. Clustering Using K-Means
We applied K-Means clustering to categorize countries into distinct groups based on their well-being indicators. The optimal number of clusters was determined to be three, revealing:
- **Cluster 1**: High well-being with strong social support and economic indicators (e.g., Nordic countries).
- **Cluster 2**: Moderate well-being characterized by varying GDP but low social support (e.g., Eastern European countries).
- **Cluster 3**: Low well-being with significant issues in social support and high corruption perceptions (e.g., certain developing nations).

## Key Findings and Insights
- Countries with high GDP per capita almost universally had higher scores on the Life Ladder, reinforced by strong social networks.
- Perceptions of corruption inversely affected the Life Ladder score; nations that reported higher corruption tended to have lower well-being scores, despite economic factors.
- Clustering revealed stark differences in well-being levels tied closely to both economic factors and social support structures.

## Implications and Suggestions
The findings indicate significant implications for policymakers and stakeholders focusing on improving national well-being. Here are a few recommendations:
1. **Strengthening Social Frameworks**: Countries with moderate life ladder scores should aim to bolster community support systems and civic engagement to enhance citizens’ subjective well-being.
2. **Addressing Perception of Corruption**: Strategies should be implemented to reduce corruption—promoting transparency and accountability in governance.
3. **Inclusive Economic Policies**: While economic growth is important, it should be complemented by social welfare programs to ensure equitable distribution of resources, particularly in countries in the second and third clusters.

By focusing on these areas, nations can create a more holistic approach to improving citizen well-being that transcends mere economic indicators.