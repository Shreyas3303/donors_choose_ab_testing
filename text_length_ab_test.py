#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text Length Optimization A/B Testing for DonorsChoose

This script implements an A/B test to optimize text length requirements 
for DonorsChoose project approval.

Background:
From our EDA, we found that approved projects have longer essays 
(1,015 vs 962 characters) and summaries. This A/B test will explore 
whether implementing minimum text length requirements improves project 
approval rates and quality.

Test Hypothesis:
- Null Hypothesis: Text length requirements have no effect on project approval rates
- Alternative Hypothesis: Minimum text length requirements improve project approval rates

Test Design:
- Control Group (A): Current text requirements (no minimum length)
- Treatment Group (B): Minimum essay length of 1,000 characters
- Treatment Group (C): Minimum essay length of 1,200 characters
- Treatment Group (D): Minimum essay length of 800 characters
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, ttest_ind, norm
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('default')
sns.set_palette("husl")

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', 1000)

def main():
    """Main function to run the A/B test analysis"""
    
    print("=" * 60)
    print("TEXT LENGTH OPTIMIZATION A/B TESTING")
    print("=" * 60)
    
    # 1. Load and prepare data
    print("\n1. Loading and preparing data...")
    df = load_and_prepare_data()
    
    # 2. Analyze current text length patterns
    print("\n2. Analyzing current text length patterns...")
    analyze_current_patterns(df)
    
    # 3. Design A/B test
    print("\n3. Designing A/B test...")
    sample_size_analysis(df)
    
    # 4. Implement A/B test
    print("\n4. Implementing A/B test...")
    test_groups, df_with_test = implement_ab_test(df)
    
    # 5. Analyze results
    print("\n5. Analyzing A/B test results...")
    analyze_results(df_with_test, test_groups)
    
    # 6. Statistical testing
    print("\n6. Performing statistical significance tests...")
    statistical_tests(df_with_test)
    
    # 7. Business impact analysis
    print("\n7. Analyzing business impact...")
    business_impact_analysis(df_with_test)
    
    # 8. Generate recommendations
    print("\n8. Generating recommendations...")
    generate_recommendations(df_with_test)
    
    print("\n" + "=" * 60)
    print("A/B TEST ANALYSIS COMPLETE")
    print("=" * 60)

def load_and_prepare_data():
    """Load the dataset and calculate text lengths"""
    # Load the dataset
    df = pd.read_csv('donors_choose_data.csv')
    
    # Calculate text lengths
    df['title_length'] = df['cleaned_titles'].str.len()
    df['essay_length'] = df['cleaned_essays'].str.len()
    df['summary_length'] = df['cleaned_summary'].str.len()
    df['total_text_length'] = df['title_length'] + df['essay_length'] + df['summary_length']
    
    print(f"Dataset shape: {df.shape}")
    print(f"Current approval rate: {df['project_is_approved'].mean()*100:.2f}%")
    
    return df

def analyze_current_patterns(df):
    """Analyze current text length distributions"""
    # Create visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Essay length distribution by approval status
    sns.boxplot(data=df, x='project_is_approved', y='essay_length', ax=ax1)
    ax1.set_title('Essay Length by Approval Status')
    ax1.set_xlabel('Project Approved (1=Yes, 0=No)')
    ax1.set_ylabel('Essay Length (characters)')
    
    # Summary length distribution by approval status
    sns.boxplot(data=df, x='project_is_approved', y='summary_length', ax=ax2)
    ax2.set_title('Summary Length by Approval Status')
    ax2.set_xlabel('Project Approved (1=Yes, 0=No)')
    ax2.set_ylabel('Summary Length (characters)')
    
    # Total text length distribution by approval status
    sns.boxplot(data=df, x='project_is_approved', y='total_text_length', ax=ax3)
    ax3.set_title('Total Text Length by Approval Status')
    ax3.set_xlabel('Project Approved (1=Yes, 0=No)')
    ax3.set_ylabel('Total Text Length (characters)')
    
    # Essay length histogram
    sns.histplot(data=df, x='essay_length', hue='project_is_approved', bins=50, alpha=0.6, ax=ax4)
    ax4.set_title('Essay Length Distribution')
    ax4.set_xlabel('Essay Length (characters)')
    ax4.set_ylabel('Count')
    ax4.legend(['Rejected', 'Approved'])
    
    plt.tight_layout()
    plt.show()
    
    # Print statistics
    text_stats = df.groupby('project_is_approved')[['essay_length', 'summary_length', 'total_text_length']].agg(['mean', 'median', 'std'])
    print("\nText length statistics by approval status:")
    print(text_stats.round(2))

def sample_size_analysis(df):
    """Calculate required sample sizes for different effect sizes"""
    def calculate_sample_size(alpha=0.05, power=0.8, p1=0.8486, p2=0.87):
        """Calculate required sample size for A/B test"""
        z_alpha = norm.ppf(1 - alpha/2)  # Two-tailed test
        z_beta = norm.ppf(power)
        
        p_avg = (p1 + p2) / 2
        
        n = 2 * ((z_alpha * np.sqrt(2 * p_avg * (1 - p_avg)) + z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) / (p2 - p1))**2
        
        return int(np.ceil(n))
    
    # Calculate sample sizes for different effect sizes
    current_rate = df['project_is_approved'].mean()
    effect_sizes = [0.01, 0.02, 0.03, 0.05]  # 1%, 2%, 3%, 5% improvement
    
    print("Sample size requirements for different effect sizes:")
    print(f"Current approval rate: {current_rate:.4f}")
    print("\nEffect Size | Required Sample Size per Group")
    print("-" * 45)
    
    for effect in effect_sizes:
        new_rate = current_rate + effect
        sample_size = calculate_sample_size(p1=current_rate, p2=new_rate)
        print(f"{effect:.2f} ({effect*100:.0f}%) | {sample_size:,}")
    
    # Choose a reasonable sample size
    target_sample_size = 5000  # 5,000 projects per group
    print(f"\nSelected sample size per group: {target_sample_size:,}")
    print(f"Total test size: {target_sample_size * 4:,} (4 groups)")

def implement_ab_test(df):
    """Implement the A/B test with different text length requirements"""
    np.random.seed(42)  # For reproducibility
    
    # Define test groups
    test_groups = {
        'A': {'name': 'Control', 'min_essay_length': 0},
        'B': {'name': 'Treatment 1', 'min_essay_length': 800},
        'C': {'name': 'Treatment 2', 'min_essay_length': 1000},
        'D': {'name': 'Treatment 3', 'min_essay_length': 1200}
    }
    
    # Randomly assign projects to test groups
    df['test_group'] = np.random.choice(['A', 'B', 'C', 'D'], size=len(df), p=[0.25, 0.25, 0.25, 0.25])
    
    # Simulate the effect of text length requirements
    def simulate_text_length_effect(row):
        """Simulate how text length requirements would affect approval"""
        group = row['test_group']
        min_length = test_groups[group]['min_essay_length']
        
        if min_length == 0:  # Control group - no change
            return row['project_is_approved']
        
        # If essay is too short, reduce approval probability
        if row['essay_length'] < min_length:
            # Reduce approval probability by 30% for short essays
            if row['project_is_approved'] == 1:
                return np.random.choice([0, 1], p=[0.3, 0.7])
        
        return row['project_is_approved']
    
    # Apply the treatment effect
    df['ab_test_approved'] = df.apply(simulate_text_length_effect, axis=1)
    
    print("A/B Test Groups Created:")
    for group, config in test_groups.items():
        group_data = df[df['test_group'] == group]
        approval_rate = group_data['ab_test_approved'].mean() * 100
        print(f"Group {group} ({config['name']}): {len(group_data):,} projects, {approval_rate:.2f}% approval rate")
    
    return test_groups, df

def analyze_results(df, test_groups):
    """Analyze A/B test results"""
    # Create visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Approval rates by test group
    group_results = df.groupby('test_group')['ab_test_approved'].agg(['count', 'mean']).reset_index()
    group_results['approval_rate'] = group_results['mean'] * 100
    group_results['group_name'] = group_results['test_group'].map({k: v['name'] for k, v in test_groups.items()})
    
    sns.barplot(data=group_results, x='group_name', y='approval_rate', ax=ax1)
    ax1.set_title('Approval Rates by Test Group')
    ax1.set_xlabel('Test Group')
    ax1.set_ylabel('Approval Rate (%)')
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for i, (_, row) in enumerate(group_results.iterrows()):
        ax1.text(i, row['approval_rate'] + 0.5, f"{row['approval_rate']:.2f}%", 
                 ha='center', va='bottom', fontweight='bold')
    
    # Essay length distribution by test group
    sns.boxplot(data=df, x='test_group', y='essay_length', ax=ax2)
    ax2.set_title('Essay Length Distribution by Test Group')
    ax2.set_xlabel('Test Group')
    ax2.set_ylabel('Essay Length (characters)')
    
    # Projects that would be affected by minimum length requirements
    affected_projects = {}
    for group, config in test_groups.items():
        if config['min_essay_length'] > 0:
            group_data = df[df['test_group'] == group]
            affected = (group_data['essay_length'] < config['min_essay_length']).sum()
            affected_projects[group] = affected
    
    if affected_projects:
        ax3.bar(affected_projects.keys(), affected_projects.values())
        ax3.set_title('Projects Affected by Minimum Length Requirements')
        ax3.set_xlabel('Test Group')
        ax3.set_ylabel('Number of Projects')
        
        # Add value labels
        for group, count in affected_projects.items():
            ax3.text(group, count + 50, f"{count:,}", ha='center', va='bottom', fontweight='bold')
    
    # Approval rate by essay length bins
    df['essay_length_bin'] = pd.cut(df['essay_length'], bins=[0, 500, 800, 1000, 1200, 1500, 2000, 3000], 
                                    labels=['0-500', '500-800', '800-1000', '1000-1200', '1200-1500', '1500-2000', '2000+'])
    length_approval = df.groupby('essay_length_bin')['ab_test_approved'].agg(['count', 'mean']).reset_index()
    length_approval['approval_rate'] = length_approval['mean'] * 100
    
    sns.barplot(data=length_approval, x='essay_length_bin', y='approval_rate', ax=ax4)
    ax4.set_title('Approval Rate by Essay Length Bins')
    ax4.set_xlabel('Essay Length (characters)')
    ax4.set_ylabel('Approval Rate (%)')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # Print detailed results
    print("\nA/B Test Results Summary:")
    print("=" * 50)
    for _, row in group_results.iterrows():
        print(f"{row['group_name']:15} | {row['count']:6,} projects | {row['approval_rate']:6.2f}% approval rate")

def statistical_tests(df):
    """Perform statistical significance tests"""
    def perform_ab_test(control_data, treatment_data, alpha=0.05):
        """Perform A/B test between control and treatment groups"""
        # Chi-square test for proportions
        control_approved = control_data.sum()
        control_total = len(control_data)
        treatment_approved = treatment_data.sum()
        treatment_total = len(treatment_data)
        
        # Create contingency table
        contingency_table = np.array([
            [control_approved, control_total - control_approved],
            [treatment_approved, treatment_total - treatment_approved]
        ])
        
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
        
        # Calculate effect size (difference in proportions)
        control_rate = control_approved / control_total
        treatment_rate = treatment_approved / treatment_total
        effect_size = treatment_rate - control_rate
        
        # Calculate confidence interval
        pooled_se = np.sqrt(control_rate * (1 - control_rate) / control_total + 
                           treatment_rate * (1 - treatment_rate) / treatment_total)
        ci_95 = 1.96 * pooled_se
        
        return {
            'control_rate': control_rate,
            'treatment_rate': treatment_rate,
            'effect_size': effect_size,
            'p_value': p_value,
            'significant': p_value < alpha,
            'ci_lower': effect_size - ci_95,
            'ci_upper': effect_size + ci_95
        }
    
    # Test each treatment group against control
    control_data = df[df['test_group'] == 'A']['ab_test_approved']
    results_summary = []
    
    print("Statistical Significance Tests:")
    print("=" * 60)
    print(f"Control Group (A) approval rate: {control_data.mean():.4f}")
    print()
    
    for group in ['B', 'C', 'D']:
        treatment_data = df[df['test_group'] == group]['ab_test_approved']
        result = perform_ab_test(control_data, treatment_data)
        
        print(f"Treatment Group {group} vs Control:")
        print(f"  Treatment approval rate: {result['treatment_rate']:.4f}")
        print(f"  Effect size: {result['effect_size']:.4f} ({result['effect_size']*100:.2f}%)")
        print(f"  P-value: {result['p_value']:.6f}")
        print(f"  95% CI: [{result['ci_lower']:.4f}, {result['ci_upper']:.4f}]")
        print(f"  Statistically significant: {'Yes' if result['significant'] else 'No'}")
        print()
        
        results_summary.append({
            'group': group,
            'treatment_rate': result['treatment_rate'],
            'effect_size': result['effect_size'],
            'p_value': result['p_value'],
            'significant': result['significant']
        })
    
    return results_summary

def business_impact_analysis(df):
    """Analyze business impact of A/B test results"""
    def calculate_business_impact(control_rate, treatment_rate, total_projects, avg_project_cost=298.12):
        """Calculate business impact of A/B test results"""
        # Calculate additional approved projects
        additional_approved = (treatment_rate - control_rate) * total_projects
        
        # Calculate additional funding
        additional_funding = additional_approved * avg_project_cost
        
        # Calculate projects that would be rejected due to length requirements
        projects_rejected = 0
        if treatment_rate < control_rate:
            projects_rejected = (control_rate - treatment_rate) * total_projects
        
        return {
            'additional_approved': additional_approved,
            'additional_funding': additional_funding,
            'projects_rejected': projects_rejected,
            'net_impact': additional_funding - (projects_rejected * avg_project_cost)
        }
    
    # Get results from statistical tests
    results_summary = statistical_tests(df)
    control_rate = df[df['test_group'] == 'A']['ab_test_approved'].mean()
    total_projects_per_year = 100000  # Estimated annual projects
    avg_project_cost = 298.12
    
    print("Business Impact Analysis:")
    print("=" * 50)
    print(f"Control group approval rate: {control_rate:.4f}")
    print(f"Estimated annual projects: {total_projects_per_year:,}")
    print(f"Average project cost: ${avg_project_cost:.2f}")
    print()
    
    for result in results_summary:
        impact = calculate_business_impact(
            control_rate, 
            result['treatment_rate'], 
            total_projects_per_year,
            avg_project_cost
        )
        
        print(f"Treatment Group {result['group']}:")
        print(f"  Additional approved projects: {impact['additional_approved']:,.0f}")
        print(f"  Additional funding: ${impact['additional_funding']:,.2f}")
        print(f"  Projects rejected due to length: {impact['projects_rejected']:,.0f}")
        print(f"  Net funding impact: ${impact['net_impact']:,.2f}")
        print()

def generate_recommendations(df):
    """Generate recommendations based on A/B test results"""
    # Get results from statistical tests
    results_summary = statistical_tests(df)
    results_df = pd.DataFrame(results_summary)
    
    # Add group names
    test_groups = {
        'B': 'Treatment 1 (800 chars)',
        'C': 'Treatment 2 (1000 chars)', 
        'D': 'Treatment 3 (1200 chars)'
    }
    results_df['group_name'] = results_df['group'].map(test_groups)
    
    print("A/B Test Recommendations:")
    print("=" * 40)
    
    # Find the best performing treatment group
    best_treatment = results_df.loc[results_df['treatment_rate'].idxmax()]
    worst_treatment = results_df.loc[results_df['treatment_rate'].idxmin()]
    
    print(f"\n1. BEST PERFORMING TREATMENT:")
    print(f"   Group: {best_treatment['group_name']}")
    print(f"   Approval rate: {best_treatment['treatment_rate']:.4f} ({best_treatment['treatment_rate']*100:.2f}%)")
    print(f"   Improvement: {best_treatment['effect_size']:.4f} ({best_treatment['effect_size']*100:.2f}%)")
    print(f"   Statistical significance: {'Yes' if best_treatment['significant'] else 'No'}")
    
    print(f"\n2. WORST PERFORMING TREATMENT:")
    print(f"   Group: {worst_treatment['group_name']}")
    print(f"   Approval rate: {worst_treatment['treatment_rate']:.4f} ({worst_treatment['treatment_rate']*100:.2f}%)")
    print(f"   Impact: {worst_treatment['effect_size']:.4f} ({worst_treatment['effect_size']*100:.2f}%)")
    
    print(f"\n3. RECOMMENDATIONS:")
    
    if best_treatment['significant']:
        print(f"   ✓ Implement {best_treatment['group_name']} as the new standard")
        print(f"   ✓ Expected improvement: {best_treatment['effect_size']*100:.2f}% in approval rate")
    else:
        print(f"   ⚠ No statistically significant improvement found")
        print(f"   ⚠ Consider running the test longer or with larger sample sizes")
    
    print(f"\n4. NEXT STEPS:")
    print(f"   • Run a longer-term test (3-6 months) to validate results")
    print(f"   • Monitor for any negative impacts on project quality")
    print(f"   • Consider segmenting by project type or teacher experience")
    print(f"   • Implement gradual rollout to minimize risk")
    
    print(f"\n5. RISK MITIGATION:")
    print(f"   • Provide clear guidelines to teachers about text length requirements")
    print(f"   • Offer writing assistance or templates for teachers")
    print(f"   • Monitor teacher feedback and satisfaction")
    print(f"   • Have a rollback plan if negative effects are observed")

if __name__ == "__main__":
    main() 