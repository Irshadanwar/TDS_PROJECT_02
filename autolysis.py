import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import argparse

# Set your OpenAI API key (you can also set it in the environment or config file)
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

def analyze_dataset(file_path):
    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None, None

    # Perform generic analysis
    analysis = {
        "columns": list(df.columns),
        "dtypes": df.dtypes.apply(str).to_dict(),
        "summary_stats": df.describe(include='all').to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }
    return df, analysis

def generate_visualizations(df, output_dir):
    # Generate a correlation heatmap if applicable
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 1:
        corr = df[numeric_columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
        plt.close()

    # Create a distribution plot for the first numeric column
    if len(numeric_columns) > 0:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[numeric_columns[0]], kde=True)
        plt.title(f"Distribution of {numeric_columns[0]}")
        plt.savefig(os.path.join(output_dir, f"{numeric_columns[0]}_distribution.png"))
        plt.close()

def narrate_story(analysis, output_dir):
    # Start with a brief overview
    story = "# Dataset Analysis Report\n\n"
    story += "This document provides an analysis of the dataset, including its structure, statistical summary, and visualizations.\n\n"
    
    # Dataset Overview
    story += "## Dataset Overview\n"
    row_count = analysis['summary_stats'].get('count', {}).get('count', 'N/A')
    column_count = len(analysis['columns'])
    story += f"The dataset contains {column_count} columns and {row_count} rows.\n\n"
    
    story += "### Columns in the dataset:\n"
    for col in analysis['columns']:
        story += f"- {col}\n"
    
    story += "\n### Data Types:\n"
    for col, dtype in analysis['dtypes'].items():
        story += f"- {col}: {dtype}\n"
    
    # Summary Statistics
    story += "\n## Summary Statistics\n"
    for stat, values in analysis['summary_stats'].items():
        story += f"\n### {stat}:\n"
        for column, value in values.items():
            story += f"- {column}: {value}\n"
    
    # Missing Values
    story += "\n## Missing Values\n"
    for col, missing in analysis['missing_values'].items():
        story += f"- {col}: {missing} missing values\n"
    
    # Visualizations
    story += "\n## Visualizations\n"
    story += "The following visualizations were generated to help understand the dataset better:\n"
    story += "- **Correlation Heatmap**: Shows relationships between numeric features.\n"
    story += "- **Distribution Plot**: Displays the distribution of the first numeric feature.\n"
    
    story += "\nThe visualizations have been saved as image files in this directory.\n"
    
    # Conclusion
    story += "\n## Conclusion\n"
    story += "This report provides a foundational understanding of the dataset. You can further delve into the data for deeper insights or model building.\n"

    # Save the generated story
    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write(story)

def analyze_and_generate_output(file_path):
    # Define output directory based on file name
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(".", base_name)
    os.makedirs(output_dir, exist_ok=True)

    # Analyze dataset
    df, analysis = analyze_dataset(file_path)

    if df is None:
        return None

    # Generate visualizations
    generate_visualizations(df, output_dir)

    # Narrate the story
    narrate_story(analysis, output_dir)

    return output_dir

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Analyze CSV files and generate reports.")
    parser.add_argument('files', nargs='*', help='List of CSV files to analyze')
    args = parser.parse_args()

    # Process each dataset file
    output_dirs = []
    for file_path in args.files:
        if os.path.exists(file_path):
            output_dir = analyze_and_generate_output(file_path)
            if output_dir:
                output_dirs.append(output_dir)
        else:
            print(f"File {file_path} not found!")

    print(f"Analysis completed. Results saved in directories: {', '.join(output_dirs)}")

if __name__ == "__main__":
    main()
