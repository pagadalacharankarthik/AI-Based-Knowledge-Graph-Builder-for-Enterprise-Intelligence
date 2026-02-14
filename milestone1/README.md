Milestone 1 — Dataset Selection & Data Ingestion
================================================

Dataset Used: Enron Email Dataset
---------------------------------

This project uses the Enron Email Dataset, a large collection of real corporate emails exchanged between employees of Enron Corporation.It is one of the most popular datasets used in NLP research for working with **unstructured email communication**.

🎯 Objective of This Milestone
------------------------------

The goal of this milestone is to:

*   Select a suitable real-world dataset
    
*   Load the dataset into the environment
    
*   Extract useful email content
    
*   Clean and prepare the data for NLP processing
    
*   Save a cleaned version for the next milestone
    

❓ Problem Statement
-------------------

Corporate emails are unstructured text. It is difficult to answer questions like:

*   Who discussed energy contracts?
    
*   Which employees communicated frequently?
    
*   What organizations were mentioned?
    

To solve this, we must first **ingest and clean** the raw email data.

📥 Data Ingestion Steps
-----------------------

### Step 1 — Import Required Libraries

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   import pandas as pd   `

### Step 2 — Load the Dataset

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   df = pd.read_csv("emails.csv")  df.head()   `

### Step 3 — Inspect Dataset Columns

Different versions of this dataset use different column names like message, text, or body.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   df.columns   `

### Step 4 — Extract Email Body Column

(For this dataset, the email content is present in the body column.)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   emails = df['body']   `

### Step 5 — Basic Cleaning

*   Remove null emails
    
*   Limit text length for faster processing
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   emails = emails.dropna()  emails = emails.str.slice(0, 1000)   `

### Step 6 — Save Cleaned Emails

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   emails.to_csv("cleaned_emails_stage1.csv", index=False)   `

This file will be used in the next milestone for NLP tasks.

✅ Output of Milestone 1
-----------------------

*   Dataset successfully loaded
    
*   Email body extracted
    
*   Noise reduced
    
*   Clean dataset saved for further processing
    

🧠 Key Understanding
--------------------

Even though the dataset is in CSV format, the email text is still unstructured.Data ingestion prepares it for NLP and AI processing.


📚 References
-------------

*   Original dataset — https://huggingface.co/datasets/corbt/enron-emails

*   Carnegie Mellon University — Enron Email Corpus Archive
    

**Author:** Charan Karthik**Project:** Email Intelligence using NLP & Knowledge Graph