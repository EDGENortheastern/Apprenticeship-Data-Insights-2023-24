# Apprenticeship-Data-Insights-2023-24

Code and analysis for an AI and Data Science apprenticeship dissertation, focusing on government data for the UK apprenticeship provision in the 2023/24 academic year.

## Technical Documentation

### Virtual Environment (venv)

A virtual environment (venv) is a way to keep project dependencies separate from other Python projects and the system (global) installations. This helps avoid conflicts and ensures everyone working on the project has the same setup. Each project gets its own virtual environment (venv), making it easier to manage packages and versions.

For example, if one project needs `matplotlib` version 3.5 and another needs version 3.8, installing both on the same system would probably cause errors. With `venv`, each project can have the exact version it needs without interfering with the other.

Using `venv` also means that if you install a package for one project, it won’t affect your other Python work. This is useful when working in teams because everyone will use the same versions of tools and libraries, preventing unexpected issues.

Using a virtual environment means:

- You don’t accidentally install packages globally.  
- You can work on multiple projects without dependency issues.  
- You can easily recreate the same environment on another machine.

For more details, see the [Python venv documentation](https://docs.python.org/3/library/venv.html).

### Setting Up a Virtual Environment

#### 1. Create a Virtual Environment  

Run this in the project folder:  
`python -m venv venv`

#### 2. Activate the Virtual Environment

- macOS/Linux:

```bash
source venv/bin/activate
```

- Windows (Command Prompt):

```bash
venv\Scripts\activate
```

- Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```

#### 3. Install Dependencies

First, make sure `pip` is up to date, then install the required packages:  

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

#### 4. Check if venv is active

On macOS/Linux run

```bash
which python
```

On Windows run

```bash
where python
```

The above should point to the `venv` folder.

#### 5. Deactivate venv when done

```bash
deactivate
```

### Important Notes

- The `venv/` folder is ignored by Git, so each person must create it on their own machine.  
- If you reclone the repository, you must set up `venv` again and reinstall dependencies.  
