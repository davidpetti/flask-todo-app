from flask import Flask, render_template, request
from todo import todoItem

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
    )

todo_items = []

@app.route('/')
def index():
    return render_template('index.html', todo_items=todo_items)

@app.route('/addItem', methods = ["POST", "GET"])
def add_item():
    if request.method == 'POST':
        item_data = request.form
        todo_items.append(todoItem(item_data['itemName'], item_data['itemDate'], item_data['itemTime']))
    return render_template('addItem.html')
    

if __name__ == '__main__':
    app.run()