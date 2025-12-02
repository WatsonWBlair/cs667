#!/usr/bin/env python3
"""
Enhanced Data Validation Script
Validates statistical compliance and Benford's Law effectiveness
"""

import pandas as pd
import numpy as np
from scipy import stats

def validate_enhanced_dataset():
    # Load enhanced dataset
    df = pd.read_csv('./data/enhanced_raw_data.csv')
    print(f'Enhanced dataset loaded: {len(df):,} transactions')
    
    # Check Benford's Law compliance
    amounts = df['Amount'].values
    first_digits = [int(str(amount)[0]) for amount in amounts if str(amount)[0].isdigit()]
    
    # Expected Benford's distribution
    expected_benford = [np.log10(1 + 1/d) for d in range(1, 10)]
    print('\nExpected Benford proportions:', [f'{p:.3f}' for p in expected_benford])
    
    # Observed distribution
    digit_counts = {d: first_digits.count(d) for d in range(1, 10)}
    total_count = len(first_digits)
    observed_props = [digit_counts[d]/total_count for d in range(1, 10)]
    print('Observed proportions:     ', [f'{p:.3f}' for p in observed_props])
    
    # Chi-squared test
    expected_counts = [p * total_count for p in expected_benford]
    observed_counts = [digit_counts[d] for d in range(1, 10)]
    
    chi2, p_value = stats.chisquare(observed_counts, expected_counts)
    print(f'\nBenford Law Chi-squared: {chi2:.2f}')
    print(f'P-value: {p_value:.4f}')
    
    if p_value > 0.05:
        print('✅ Dataset follows Benford\'s Law (natural distribution)')
    else:
        print('⚠️  Dataset deviates from Benford\'s Law (investigate further)')
    
    # Dataset summary
    print(f'\nDataset Summary:')
    print(f'Total transactions: {len(df):,}')
    print(f'Amount range: ${df["Amount"].min():.2f} - ${df["Amount"].max():.2f}')
    print(f'Average amount: ${df["Amount"].mean():.2f}')
    print(f'Unique merchants: {df["Merchant"].nunique()}')
    print(f'Unique accounts: {df["AccountID"].nunique()}')
    
    # Check fraud metadata
    try:
        fraud_df = pd.read_csv('./data/fraud_patterns_metadata.csv')
        print(f'\nFraud Patterns Injected: {len(fraud_df):,} patterns')
        
        fraud_types = fraud_df['type'].value_counts()
        print('Fraud pattern distribution:')
        for fraud_type, count in fraud_types.items():
            print(f'  {fraud_type}: {count} instances')
            
    except FileNotFoundError:
        print('No fraud metadata found')
    
    return df, chi2, p_value

if __name__ == "__main__":
    enhanced_data, chi2_stat, benford_p = validate_enhanced_dataset()