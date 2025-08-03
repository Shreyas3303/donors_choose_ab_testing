# Text Length Optimization A/B Testing

This project implements a comprehensive A/B test to optimize text length requirements for DonorsChoose project approval.

## Overview

Based on exploratory data analysis of the DonorsChoose dataset, we found that approved projects have longer essays (1,015 vs 962 characters) and summaries. This A/B test explores whether implementing minimum text length requirements improves project approval rates and quality.

## Files

- `text_length_ab_test.py` - Main A/B testing script
- `donors_choose_data.csv` - Dataset (required)
- `donors_choose_eda.ipynb` - Original exploratory data analysis

## Test Design

### Hypothesis
- **Null Hypothesis**: Text length requirements have no effect on project approval rates
- **Alternative Hypothesis**: Minimum text length requirements improve project approval rates

### Test Groups
- **Control Group (A)**: Current text requirements (no minimum length)
- **Treatment Group (B)**: Minimum essay length of 800 characters
- **Treatment Group (C)**: Minimum essay length of 1,000 characters
- **Treatment Group (D)**: Minimum essay length of 1,200 characters

## Usage

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Running the A/B Test
```bash
python text_length_ab_test.py
```

## What the Script Does

1. **Data Loading & Preparation**
   - Loads the DonorsChoose dataset
   - Calculates text lengths for titles, essays, and summaries

2. **Current Pattern Analysis**
   - Analyzes how text length currently relates to approval rates
   - Creates visualizations of text length distributions

3. **Sample Size Calculation**
   - Calculates required sample sizes for different effect sizes
   - Determines statistical power requirements

4. **A/B Test Implementation**
   - Randomly assigns projects to test groups
   - Simulates the effect of text length requirements on approval

5. **Results Analysis**
   - Compares approval rates across test groups
   - Identifies projects affected by length requirements

6. **Statistical Testing**
   - Performs chi-square tests for significance
   - Calculates confidence intervals and effect sizes

7. **Business Impact Analysis**
   - Quantifies financial impact of different requirements
   - Estimates additional funding and rejected projects

8. **Recommendations**
   - Identifies best performing treatment
   - Provides actionable next steps

## Key Metrics

- **Approval Rate**: Percentage of projects approved in each group
- **Effect Size**: Difference in approval rates between control and treatment
- **Statistical Significance**: P-value and confidence intervals
- **Business Impact**: Additional funding and project counts

## Output

The script provides:
- Visualizations of text length patterns and test results
- Statistical significance tests for each treatment group
- Business impact calculations
- Actionable recommendations

## Sample Output

```
============================================================
TEXT LENGTH OPTIMIZATION A/B TESTING
============================================================

1. Loading and preparing data...
Dataset shape: (109248, 18)
Current approval rate: 84.86%

2. Analyzing current text length patterns...
[Visualizations displayed]

3. Designing A/B test...
Sample size requirements for different effect sizes:
Current approval rate: 0.8486

Effect Size | Required Sample Size per Group
---------------------------------------------
0.01 (1%) | 15,234
0.02 (2%) | 3,809
0.03 (3%) | 1,693
0.05 (5%) | 610

4. Implementing A/B test...
A/B Test Groups Created:
Group A (Control): 27,312 projects, 84.86% approval rate
Group B (Treatment 1): 27,312 projects, 82.45% approval rate
Group C (Treatment 2): 27,312 projects, 81.23% approval rate
Group D (Treatment 3): 27,312 projects, 79.87% approval rate

5. Analyzing A/B test results...
[Visualizations displayed]

6. Performing statistical significance tests...
Statistical Significance Tests:
============================================================
Control Group (A) approval rate: 0.8486

Treatment Group B vs Control:
  Treatment approval rate: 0.8245
  Effect size: -0.0241 (-2.41%)
  P-value: 0.000000
  Statistically significant: Yes

7. Analyzing business impact...
Business Impact Analysis:
==================================================
Control group approval rate: 0.8486
Estimated annual projects: 100,000
Average project cost: $298.12

Treatment Group B:
  Additional approved projects: -2,410
  Additional funding: -$718,469.20
  Projects rejected due to length: 2,410
  Net funding impact: -$718,469.20

8. Generating recommendations...
A/B Test Recommendations:
========================================

1. BEST PERFORMING TREATMENT:
   Group: Control
   Approval rate: 0.8486 (84.86%)
   Improvement: 0.0000 (0.00%)
   Statistical significance: N/A

2. WORST PERFORMING TREATMENT:
   Group: Treatment 3 (1200 chars)
   Approval rate: 0.7987 (79.87%)
   Impact: -0.0499 (-4.99%)

3. RECOMMENDATIONS:
   ⚠ No statistically significant improvement found
   ⚠ Consider running the test longer or with larger sample sizes

4. NEXT STEPS:
   • Run a longer-term test (3-6 months) to validate results
   • Monitor for any negative impacts on project quality
   • Consider segmenting by project type or teacher experience
   • Implement gradual rollout to minimize risk
```

## Customization

You can modify the script to:
- Test different minimum length thresholds
- Adjust the simulation parameters
- Change the business impact calculations
- Add additional segmentation analysis

## Next Steps

1. Run the script with your actual data
2. Review the statistical significance of results
3. Consider implementing the best performing treatment
4. Monitor results in a production environment
5. Iterate based on real-world feedback 