# Plagiarism Checker

Plagiarism is being a critical part of every report or blogs. But some online websites are really not completely able to find out the actual *percentages* of the texts.

## In the Repo:
There are 3 main files for you:
1. The file with Flask [app.py](https://github.com/wavesoumen/Plagiarism-Checker/blob/main/app.py) with complet code.
2. The only python script for Plagiarism Checker [check_plagiarism.py](https://github.com/wavesoumen/Plagiarism-Checker/blob/main/check_plagiarism.py) for fast use with the command:
```bash
python check_plagiarism.py
```
3. The API for it [plagiarism_api.py](https://github.com/wavesoumen/Plagiarism-Checker/blob/main/plagiarism_api.py), uses:
Install uvicorn for run api:
```bash
pip install uvicorn
```
Run the api:
```bash
uvicorn plagiarism_api:app --reload
```
## Speciality of this function:
There are 3 parts of the python script.
Some features of the function are:
- It shows the _percentages_ of the input text passage.
- It shows that which sentences & words are plagiarized.
- Displays the *Source Links* of the plagiarism.

# 
## -Soumen Kayal.
