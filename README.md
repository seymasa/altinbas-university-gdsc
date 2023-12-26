# altinbas-university-gdsc
![altınbaş-gdsc](https://github.com/seymasa/altinbas-university-gdsc/assets/8446004/0348ea09-ac12-4b4b-8f8c-c15f6cb5a46f)

![image](https://github.com/seymasa/altinbas-university-gdsc/assets/8446004/3a425976-7361-43f4-b57f-1b766b77a386)

### Description
As an example for LLMs, search for a user on a web developed by Altınbaş University, and with the help of agents, gather insights from sources like LinkedIn and Instagram, and then summarize based on these insights.
presentation link: https://www.canva.com/design/DAF4DfNHbBU/N60goLFNNkSKZfvk7PngSQ/edit?utm_content=DAF4DfNHbBU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

### Architecture
<img width="756" alt="Screenshot 2023-12-26 at 08 34 31" src="https://github.com/seymasa/altinbas-university-gdsc/assets/8446004/b4209d00-d816-48ea-a5cd-bd04a913983d">

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
