# Quarto tips for classes
_Please refer to the [Quarto documentation](https://quarto.org/)._
For course purposes we collected some tips that might be useful.

# GitHub Action (Continuous Integration)
Pdf report is generated with [`run.yml` workflow](.github/workflows/run.yml).

# Run Quarto locally
1. Install Quarto [https://quarto.org/docs/get-started/](https://quarto.org/docs/get-started/).
2. Render pdf from e.g. Jupyter Notebook ([https://quarto.org/docs/get-started/hello/jupyter.html](https://quarto.org/docs/get-started/hello/jupyter.html)).
```
quarto render hello.ipynb --to pdf
```
You can also use templates from several scientific journals.

# Tips for achieving report structure
## Title, author and other options
Define `raw` cell inside your file.

```
---
format:
  pdf:
    include-in-header: 
       text: |
         \usepackage{fvextra}
         \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
         \DefineVerbatimEnvironment{OutputCode}{Verbatim}{breaklines,commandchars=\\\{\}}
title: "title"
author: "author"
execute:
  enabled: true
  cache: false
date: last-modified
---
```

## Add $\LaTeX$ packages 
Add something like this in your `raw` cell:
```
---
format:
  pdf:
    include-in-header: 
       text: |
         \usepackage{mhchem}
---
```
1. Wrap code automatically in pdf file
```
---
format:
  pdf:
    include-in-header: 
       text: |
         \usepackage{fvextra}
         \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
         \DefineVerbatimEnvironment{OutputCode}{Verbatim}{breaklines,commandchars=\\\{\}}
---
```

## Insert variables in Markdown text
Inside text you can insert \`{python x}\`, where `x` is a variable with some value.

## Match Plot Font Size with PDF Text
When rendering to PDF, the default font size in plots (like Matplotlib) is often too small. To make the plot text match the document scale, set the global font size at the top of your notebook. For our template, size `22` works best for me.
```python
import matplotlib.pyplot as plt

# Set global font size for all plots in the notebook
plt.rcParams.update({'font.size': 22})
