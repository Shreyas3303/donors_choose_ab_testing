# 📊 DonorsChoose Text Length Optimization A/B Testing

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Scipy](https://img.shields.io/badge/Scipy-1.7+-orange.svg)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-yellow.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Optimizing project approval rates through data-driven text length requirements**

## 🎯 Project Overview

This project implements a comprehensive **A/B testing framework** to optimize text length requirements for DonorsChoose project approval. Based on exploratory data analysis, we discovered that approved projects tend to have longer essays (1,015 vs 962 characters) and summaries. This A/B test explores whether implementing minimum text length requirements improves project approval rates and overall quality.

### 📈 Key Insights from EDA
- **Approved projects** have longer essays (1,015 characters vs 962 characters)
- **Current approval rate**: 84.86%
- **Dataset size**: 109,248 projects
- **Text length correlation** with approval rates

## 🏗️ Project Structure

```
donors_ab_testing_analysis/
├── 📊 text_length_ab_test.py          # Main A/B testing script
├── 📋 text_length_ab_test.ipynb       # Jupyter notebook version
├── 🔍 donors_choose_eda.ipynb         # Exploratory data analysis
├── 📥 get_data.py                     # Data retrieval script
├── 📚 README.md                       # This file
├── 📖 README_AB_Testing.md           # Detailed documentation
├── 🗂️ donors_choose_data.csv         # Dataset (126MB)
└── 🐍 venv/                          # Virtual environment
```

## 🧪 A/B Test Design

### 📋 Hypothesis
- **Null Hypothesis (H₀)**: Text length requirements have no effect on project approval rates
- **Alternative Hypothesis (H₁)**: Minimum text length requirements improve project approval rates

### 🎲 Test Groups
| Group | Description | Minimum Essay Length | Expected Impact |
|-------|-------------|---------------------|-----------------|
| **A (Control)** | Current requirements | No minimum | Baseline |
| **B (Treatment 1)** | Moderate requirement | 800 characters | +2-3% approval |
| **C (Treatment 2)** | Standard requirement | 1,000 characters | +3-5% approval |
| **D (Treatment 3)** | High requirement | 1,200 characters | +5-7% approval |

## 🚀 Quick Start

### Prerequisites
```bash
# Install Python dependencies
pip install pandas numpy matplotlib seaborn scipy

# Or install from requirements.txt (if available)
pip install -r requirements.txt
```

### Running the A/B Test
```bash
# Run the main analysis
python text_length_ab_test.py

# Or use the Jupyter notebook
jupyter notebook text_length_ab_test.ipynb
```

## 📊 What the Analysis Does

### 1. 📥 Data Loading & Preparation
- Loads the DonorsChoose dataset (109,248 projects)
- Calculates text lengths for titles, essays, and summaries
- Handles missing data and outliers

### 2. 📈 Current Pattern Analysis
- Analyzes text length distributions by approval status
- Creates visualizations of current patterns
- Identifies optimal length thresholds

### 3. 📐 Sample Size Calculation
- Calculates required sample sizes for different effect sizes
- Determines statistical power requirements
- Ensures reliable test results

### 4. 🎯 A/B Test Implementation
- Randomly assigns projects to test groups
- Simulates the effect of text length requirements
- Maintains statistical validity

### 5. 📊 Results Analysis
- Compares approval rates across test groups
- Identifies projects affected by length requirements
- Generates comprehensive visualizations

### 6. 🔬 Statistical Testing
- Performs chi-square tests for significance
- Calculates confidence intervals and effect sizes
- Determines practical significance

### 7. 💰 Business Impact Analysis
- Quantifies financial impact of different requirements
- Estimates additional funding and rejected projects
- Provides ROI calculations

### 8. 📋 Recommendations
- Identifies best performing treatment
- Provides actionable next steps
- Suggests implementation strategy

## 📈 Key Metrics & Results

### 📊 Statistical Metrics
- **Approval Rate**: Percentage of projects approved in each group
- **Effect Size**: Difference in approval rates between control and treatment
- **Statistical Significance**: P-value and confidence intervals
- **Power Analysis**: Probability of detecting true effects

### 💼 Business Metrics
- **Additional Funding**: Estimated increase in total funding
- **Project Count Impact**: Number of additional approved/rejected projects
- **ROI**: Return on investment for implementation
- **Risk Assessment**: Potential negative impacts

## 🎨 Sample Visualizations

The analysis generates several key visualizations:

### 📊 Text Length Distributions
```
Approved vs Rejected Projects by Essay Length
┌─────────────────────────────────────────┐
│  Approved Projects: 1,015 chars avg     │
│  Rejected Projects:  962 chars avg      │
│                                         │
│  ████████████████████████████████████   │
│  ████████████████████████████████████   │
└─────────────────────────────────────────┘
```

### 📈 A/B Test Results
```
Treatment Group Performance
┌─────────────────────────────────────────┐
│ Group A (Control):    84.86% approval   │
│ Group B (800 chars):  82.45% approval   │
│ Group C (1000 chars): 81.23% approval   │
│ Group D (1200 chars): 79.87% approval   │
└─────────────────────────────────────────┘
```

## 📋 Sample Output

```
============================================================
TEXT LENGTH OPTIMIZATION A/B TESTING
============================================================

📊 Dataset Statistics:
- Total projects: 109,248
- Current approval rate: 84.86%
- Average essay length: 1,015 chars (approved) vs 962 chars (rejected)

🎯 A/B Test Results:
- Group A (Control): 84.86% approval rate
- Group B (800 chars): 82.45% approval rate (-2.41%)
- Group C (1000 chars): 81.23% approval rate (-3.63%)
- Group D (1200 chars): 79.87% approval rate (-4.99%)

📈 Statistical Significance:
- All treatments show statistically significant differences (p < 0.001)
- Effect sizes range from -2.41% to -4.99%

💰 Business Impact:
- Treatment B: -$718,469 additional funding
- Treatment C: -$1,082,456 additional funding  
- Treatment D: -$1,487,234 additional funding

📋 Recommendations:
⚠️ No statistically significant improvement found
⚠️ Consider running longer-term tests or segmenting by project type
```

## 🔧 Customization Options

You can modify the script to:

- **Test different thresholds**: Adjust minimum length requirements
- **Segment analysis**: Analyze by project type, teacher experience, or school type
- **Change simulation parameters**: Modify approval rate assumptions
- **Add new metrics**: Include quality scores, funding amounts, or donor engagement
- **Extend test duration**: Run longer-term tests for more reliable results

## 📚 Files Description

| File | Description |
|------|-------------|
| `text_length_ab_test.py` | Main A/B testing script with comprehensive analysis |
| `text_length_ab_test.ipynb` | Jupyter notebook version for interactive analysis |
| `donors_choose_eda.ipynb` | Original exploratory data analysis |
| `get_data.py` | Script to retrieve and prepare the dataset |
| `donors_choose_data.csv` | Main dataset (109,248 projects, 18 features) |

## 🎯 Next Steps

1. **Run the analysis** with your actual data
2. **Review statistical significance** of results
3. **Consider implementing** the best performing treatment
4. **Monitor results** in a production environment
5. **Iterate based on** real-world feedback

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DonorsChoose** for providing the dataset
- **Data Science community** for best practices in A/B testing
- **Open source contributors** for the libraries used in this analysis

---

<div align="center">

**Made with ❤️ for data-driven decision making**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/donors_ab_testing_analysis?style=social)](https://github.com/yourusername/donors_ab_testing_analysis)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/donors_ab_testing_analysis?style=social)](https://github.com/yourusername/donors_ab_testing_analysis)

</div> 