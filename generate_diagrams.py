import os
import re
import subprocess
import json

def extract_mermaid_diagrams(flowchart_file):
    with open(flowchart_file, 'r') as f:
        content = f.read()
    
    # Extract diagrams between mermaid code blocks
    pattern = r'```mermaid\n(.*?)\n```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    return diagrams

def save_diagram_to_file(diagram, file_name):
    # Create a temporary mermaid file
    with open('temp.mmd', 'w') as f:
        f.write(diagram)
    
    # Convert to SVG using mmdc (Mermaid CLI)
    try:
        subprocess.run([
            'cmd', '/c', 
            'npx', '-p', '@mermaid-js/mermaid-cli', 'mmdc',
            '-i', 'temp.mmd',
            '-o', f'diagrams/{file_name}.svg'
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error generating diagram: {e}")
    
    # Clean up temporary file
    os.remove('temp.mmd')

def main():
    # Ensure diagrams directory exists
    if not os.path.exists('diagrams'):
        os.makedirs('diagrams')
    
    # File names for each diagram
    diagram_files = [
        'data_ingestion',
        'embedding',
        'model_api',
        'streamlit_app',
        'system_architecture'
    ]
    
    # Extract and convert diagrams
    diagrams = extract_mermaid_diagrams('flowchart.txt')
    
    for diagram, file_name in zip(diagrams, diagram_files):
        save_diagram_to_file(diagram, file_name)
        print(f'Generated {file_name}.svg')

if __name__ == '__main__':
    main()
