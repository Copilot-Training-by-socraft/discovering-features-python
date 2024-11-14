# Discovering features

Use of GitHub Copilot in Python

## Requirements

- Python 3

In **requirements.txt**

- PyTest

## Create a virtual environment

```shell
python3 -m venv venv
```

Activate the virtual environment on macOS and Linux
```shell
source venv/bin/activate
```

Activate the virtual environment on Windows

```shell
.\venv\Scripts\activate
```

Install the requirements

```shell
pip install -r requirements.txt
```

## Run tests  

```shell
pytest
```

## Exercices

Open the provided Python project and generate suggestion from Copilot with

### 1. a comment

```python
# method to compute a bubble sort
```

### 2. a function signature

```python
def calcul_sum(number_list):
```

### 3. the in-line prompt in code

Select the previous method, open in-line prompt, and ask: _"refactor to use the stream API"_

### 4. multiple suggestions

Open the suggestions pane, and then prompt for:

```python
# memoized fibonacci function
```

### 5. chat

Open the chat, and ask: _"write parameterized tests with five examples for a generic sorting function"_

### 6. contextual menu

Select the bubble sort and in the contextual menu, click _"Simplify This"_ and then _"Generate Docs"_ or _“/docs”_ directly in prompt
