# altinbas-university-gdsc
![altınbaş-gdsc](https://github.com/seymasa/altinbas-university-gdsc/assets/8446004/0348ea09-ac12-4b4b-8f8c-c15f6cb5a46f)

![image](https://github.com/seymasa/altinbas-university-gdsc/assets/8446004/3a425976-7361-43f4-b57f-1b766b77a386)

### Description
As an example for LLMs, search for a user on a web developed by Altınbaş University, and with the help of agents, gather insights from sources like LinkedIn and Instagram, and then summarize based on these insights.

### Architecture
![app architech](https://github.com/Teknofest-Nane-Limon/automate-backend/assets/8446004/03b6adaa-9d64-47e2-a3a8-aed88f1b0055)


### Environment Setup

Please set your Python version to Python 3.11.6:

```bash
python --version
```

- Installation of Virtualenv:

```bash
pip install virtualenv
```
- Creating a Virtualenv:

```bash
virtualenv venv
```
- Activating the Virtualenv:
```bash
source venv/bin/activate
```
- Installing libraries:
```bash
pip install -r requirements.txt
```
- Define Environment Variables.

```
# GPT-3-Turbo API
OPENAI_API_KEY=cok-gizli-bisi

#SerpApi: Google Search API
SERPAPI_API_KEY=cok-gizli-bisi
```

## Running the Application

```python
python app.py
```

--- 
