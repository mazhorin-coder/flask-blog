from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    topics_data = [
        {
            "title": "Тема 1. Основы Flask", 
            "progress": "100%", 
            "hw": "100%", 
            "comment": "Изучены основы Flask, приложение успешно запущено."
            },
        {
            "title": "Тема 2. HTML & CSS", 
            "progress": "100%", 
            "hw": "100%", 
            "comment": "Шаблоны и стили полностью настроены."},
        {
            "title": "Тема 3. Шаблоны и формы в Flask", 
            "progress": "0%", 
            "hw": "0%", 
            "comment": ""
        },
        {
            "title": "Тема 4. Основы Flask-SQLAlchemy...", 
            "progress": "0%", 
            "hw": "0%", 
            "comment": ""
        },
        {
            "title": "Тема 5. Авторизация в Flask", 
            "progress": "0%", 
            "hw": "0%", 
            "comment": ""
        },
        {
            "title": "Тема 6. Работа с REST API", 
            "progress": "0%", 
            "hw": "0%", 
            "comment": ""
        },
        {
            "title": "Тема 7. Итоговый проект", 
            "progress": "0%", 
            "hw": "-", 
            "comment": ""
        },
        {
            "title": "Итоговая аттестация", 
            "progress": "0%", 
            "hw": "0%", 
            "comment": ""
        }
    ]
    
    return render_template('index.html', topics=topics_data)

if __name__ == "__main__":
    app.run(debug=True)