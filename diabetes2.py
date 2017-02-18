import numpy as np
import pandas as pd

def load_data(file):
    df = pd.read_csv(file, sep=',',
        na_values='?', low_memory=False)

    # Edit columns
    df.columns.str.strip().str.lower()
    df = df.replace({
        # gender
        'Male': 0,
        'Female': 1,
        # race
        'Caucasian':0,
        'AfricanAmerican': 1,
        'Asian': 2,
        'Hispanic': 3,
        'Other': 4,
        # age
        '[0-10)': 0,
        '[10-20)': 1,
        '[20-30)': 2,
        '[30-40)': 3,
        '[40-50)': 4,
        '[50-60)': 5,
        '[60-70)': 6,
        '[70-80)': 7,
        '[80-90)': 8,
        '[90-100)': 9,
        # diagnostics
        'No': 0,
        'NO': 0,
        'None': 0,
        'Steady': 1,
        'Yes': 1,
        'Ch': 1,
        '>30': 1,
        '<30': 2,
        'Up': 2,
        'Down': 3,
        # max_glu_serum, A1CResult
        'Norm': 1,
        '>7': 2,
        '>8': 3,
        '>200': 2,
        '>300': 3,
    })
    df = df.replace({
        # diag_# (ignore weird values?)
        r'V[0-9]+': np.nan,
        r'E[0-9]+': np.nan,
    }, regex=True)

    # Remove garbage columns
    del df['payer_code']
    del df['weight']
    del df['medical_specialty']
    del df['glyburide-metformin']
    del df['glipizide-metformin']
    del df['glimepiride-pioglitazone']
    del df['metformin-rosiglitazone']
    del df['metformin-pioglitazone']

    # Convert all values to numeric
    df = pd.to_numeric(df, errors='coerce')

    # Store the parsed array
    df.to_csv('parsed.csv', sep=',', encoding='utf-8')

load_data('diabetes-training.csv')
# load_data('compile.csv')
