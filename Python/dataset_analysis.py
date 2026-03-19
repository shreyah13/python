import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Read the training dataset from current directory
df = pd.read_csv("archive_csv/UNSW_NB15_training-set.csv")

print("Dataset loaded successfully!")

# Exploratory Data Analysis
print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Last 5 Rows ===")
print(df.tail())

print("\n=== Shape (Rows, Columns) ===")
print(df.shape)

print("\n=== Column Names ===")
print(df.columns.tolist())

print("\n=== Data Types & Info ===")
print(df.info())

print("\n=== Missing Values ===")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# Handle missing values
df = df.fillna(0)  # Using fillna instead of dropna to preserve data

print("\n=== Statistical Summary ===")
print(df.describe())

# ============================================
# VISUALIZATION 1: Missing Values Bar Chart
# ============================================
print("\n[Generating Visualization 1: Missing Values]")

missing_data = df.isnull().sum()
missing_data = missing_data[missing_data > 0].sort_values(ascending=False)

if len(missing_data) > 0:
    plt.figure(figsize=(12, 6))
    missing_data.plot(kind='bar', color='coral')
    plt.title('Missing Values by Column', fontsize=16, fontweight='bold')
    plt.xlabel('Columns', fontsize=12)
    plt.ylabel('Number of Missing Values', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('1_missing_values.png', dpi=300, bbox_inches='tight')
    plt.show()
else:
    print("No missing values found!")

# ============================================
# VISUALIZATION 2: Attack vs Normal Traffic Distribution
# ============================================
print("\n[Generating Visualization 2: Attack vs Normal Distribution]")

if 'label' in df.columns:
    plt.figure(figsize=(10, 6))
    label_counts = df['label'].value_counts()

    # Bar plot
    plt.subplot(1, 2, 1)
    label_counts.plot(kind='bar', color=['green', 'red'])
    plt.title('Distribution of Normal vs Attack Traffic', fontsize=14, fontweight='bold')
    plt.xlabel('Label (0=Normal, 1=Attack)', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=0)

    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(label_counts, labels=['Normal', 'Attack'], autopct='%1.1f%%',
            colors=['green', 'red'], startangle=90, explode=(0.05, 0.05))
    plt.title('Percentage Distribution', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('2_attack_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

    print(f"\nNormal Traffic: {label_counts[0]} ({label_counts[0] / len(df) * 100:.2f}%)")
    print(f"Attack Traffic: {label_counts[1]} ({label_counts[1] / len(df) * 100:.2f}%)")

# ============================================
# VISUALIZATION 3: Attack Categories Distribution
# ============================================
print("\n[Generating Visualization 3: Attack Categories]")

if 'attack_cat' in df.columns:
    plt.figure(figsize=(14, 6))
    attack_counts = df['attack_cat'].value_counts()

    # Bar plot
    plt.subplot(1, 2, 1)
    attack_counts.plot(kind='bar', color='steelblue')
    plt.title('Distribution of Attack Categories', fontsize=14, fontweight='bold')
    plt.xlabel('Attack Type', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    # Pie chart (top 8 categories)
    plt.subplot(1, 2, 2)
    top_attacks = attack_counts.head(8)
    plt.pie(top_attacks, labels=top_attacks.index, autopct='%1.1f%%', startangle=90)
    plt.title('Top 8 Attack Categories', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('3_attack_categories.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\nAttack Category Distribution:")
    print(attack_counts)

# ============================================
# VISUALIZATION 4: Protocol Distribution
# ============================================
print("\n[Generating Visualization 4: Protocol Distribution]")

if 'proto' in df.columns:
    plt.figure(figsize=(10, 6))
    proto_counts = df['proto'].value_counts().head(10)

    sns.barplot(x=proto_counts.values, y=proto_counts.index, palette='viridis')
    plt.title('Top 10 Network Protocols Used', fontsize=14, fontweight='bold')
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Protocol', fontsize=12)

    # Add value labels on bars
    for i, v in enumerate(proto_counts.values):
        plt.text(v + 100, i, str(v), va='center')

    plt.tight_layout()
    plt.savefig('4_protocol_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 5: Service Distribution
# ============================================
print("\n[Generating Visualization 5: Service Distribution]")

if 'service' in df.columns:
    plt.figure(figsize=(12, 6))
    service_counts = df['service'].value_counts().head(15)

    plt.barh(range(len(service_counts)), service_counts.values, color='coral')
    plt.yticks(range(len(service_counts)), service_counts.index)
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Service', fontsize=12)
    plt.title('Top 15 Services Used', fontsize=14, fontweight='bold')

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('5_service_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 6: State Distribution
# ============================================
print("\n[Generating Visualization 6: Connection State Distribution]")

if 'state' in df.columns:
    plt.figure(figsize=(10, 6))
    state_counts = df['state'].value_counts()

    plt.bar(range(len(state_counts)), state_counts.values, color='teal')
    plt.xticks(range(len(state_counts)), state_counts.index, rotation=45, ha='right')
    plt.xlabel('Connection State', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title('Connection State Distribution', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('6_state_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 7: Correlation Heatmap
# ============================================
print("\n[Generating Visualization 7: Correlation Heatmap]")

# Select only numeric columns for correlation
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Remove ID columns if present
numeric_cols = [col for col in numeric_cols if 'id' not in col.lower()]

if len(numeric_cols) > 2:
    plt.figure(figsize=(20, 16))

    # Calculate correlation
    correlation = df[numeric_cols].corr()

    # Create heatmap
    sns.heatmap(correlation, annot=False, cmap='coolwarm', center=0,
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Heatmap of Numeric Features', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('7_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 8: Top Correlated Features with Label
# ============================================
print("\n[Generating Visualization 8: Features Correlated with Label]")

if 'label' in df.columns and len(numeric_cols) > 1:
    correlation_with_label = df[numeric_cols].corr()['label'].abs().sort_values(ascending=False)
    correlation_with_label = correlation_with_label.drop('label').head(15)

    plt.figure(figsize=(12, 6))
    plt.barh(range(len(correlation_with_label)), correlation_with_label.values, color='darkgreen')
    plt.yticks(range(len(correlation_with_label)), correlation_with_label.index)
    plt.xlabel('Absolute Correlation with Label', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.title('Top 15 Features Correlated with Attack Label', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()

    plt.tight_layout()
    plt.savefig('8_label_correlation.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\nTop features correlated with attack label:")
    print(correlation_with_label)

# ============================================
# VISUALIZATION 9: Distribution of Key Numeric Features
# ============================================
print("\n[Generating Visualization 9: Key Feature Distributions]")

# Select some key numeric features (adjust based on your dataset)
key_features = ['dur', 'sbytes', 'dbytes', 'sttl', 'dttl', 'sload', 'dload', 'spkts', 'dpkts']
available_features = [f for f in key_features if f in df.columns]

if len(available_features) >= 4:
    fig, axes = plt.subplots(3, 3, figsize=(18, 12))
    axes = axes.flatten()

    for idx, feature in enumerate(available_features[:9]):
        axes[idx].hist(df[feature], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'Distribution of {feature}', fontsize=12, fontweight='bold')
        axes[idx].set_xlabel(feature, fontsize=10)
        axes[idx].set_ylabel('Frequency', fontsize=10)
        axes[idx].grid(alpha=0.3)

    # Hide empty subplots
    for idx in range(len(available_features), 9):
        axes[idx].axis('off')

    plt.tight_layout()
    plt.savefig('9_feature_distributions.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 10: Box Plots for Attack vs Normal
# ============================================
print("\n[Generating Visualization 10: Attack vs Normal Feature Comparison]")

if 'label' in df.columns and len(available_features) >= 4:
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    axes = axes.flatten()

    for idx, feature in enumerate(available_features[:4]):
        sns.boxplot(x='label', y=feature, data=df, ax=axes[idx], palette='Set2')
        axes[idx].set_title(f'{feature} by Label', fontsize=12, fontweight='bold')
        axes[idx].set_xlabel('Label (0=Normal, 1=Attack)', fontsize=10)
        axes[idx].set_ylabel(feature, fontsize=10)

    plt.tight_layout()
    plt.savefig('10_attack_vs_normal_boxplots.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 11: Scatter Plot Matrix (Sample)
# ============================================
print("\n[Generating Visualization 11: Scatter Plot Matrix]")

if len(available_features) >= 3:
    sample_df = df.sample(n=min(1000, len(df)), random_state=42)

    selected_features = available_features[:4]
    if 'label' in df.columns:
        selected_features.append('label')

    plt.figure(figsize=(14, 14))
    pd.plotting.scatter_matrix(sample_df[selected_features],
                               alpha=0.5, figsize=(14, 14),
                               diagonal='hist', c=sample_df['label'] if 'label' in sample_df.columns else None,
                               cmap='coolwarm')
    plt.suptitle('Scatter Plot Matrix (Sample of 1000 records)', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('11_scatter_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================
# VISUALIZATION 12: Time-based Analysis (if applicable)
# ============================================
print("\n[Generating Visualization 12: Records Distribution]")

plt.figure(figsize=(12, 6))
plt.plot(range(len(df)), df.index, linewidth=0.5, color='navy')
plt.fill_between(range(len(df)), df.index, alpha=0.3, color='lightblue')
plt.title('Record Index Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Record Number', fontsize=12)
plt.ylabel('Index', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('12_record_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# VISUALIZATION 13: Data Type Distribution
# ============================================
print("\n[Generating Visualization 13: Data Types]")

plt.figure(figsize=(10, 6))
dtype_counts = df.dtypes.value_counts()

plt.pie(dtype_counts.values, labels=dtype_counts.index, autopct='%1.1f%%',
        startangle=90, colors=sns.color_palette('pastel'))
plt.title('Distribution of Data Types in Dataset', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('13_data_types.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# Summary Statistics
# ============================================
print("\n" + "=" * 60)
print("VISUALIZATION COMPLETE!")
print("=" * 60)
print(f"\nTotal Records: {len(df):,}")
print(f"Total Features: {len(df.columns)}")
print(f"Numeric Features: {len(numeric_cols)}")
print(f"Categorical Features: {len(df.select_dtypes(include=['object']).columns)}")
print("\nAll visualizations saved as PNG files in the current directory!")
print("=" * 60)