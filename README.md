# Clarina: AI super charged chatbot
**A Chatbot that will help users answer questions about Clarins products**

![](https://github.com/noeljbasil/clarina_chatbot/blob/main/src/App%20gif.gif)

Steps to run this program locally:

1. clone the repo
```sh
git clone https://github.com/noeljbasil/clarina_chatbot.git
```
2. Navigate to the folder
```
cd my_project
```
3. Set the python version for the virtual environment
```
pyenv local 3.8
```
4. Create a virtual environment for the project
```
python -m venv ./venv
```
5. Activate the virtual environment
```
venv\Scripts\activate.bat
```
6. Instal dependencies
```python
pip install -r requirements.txt
```
7. Create and update .env file with your OpenAI key. Refer .env.example for the format
```
type nul > .env
```
8. Run the app
```python
streamlit run main.py
```
