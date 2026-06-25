from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Поесть блинчиков', 'done': False},
    {'id': 2, 'title': 'Поспать', 'done': False},
    {'id': 3, 'title': 'Поиграть в первый сезон WOW MIDNIGHT', 'done': False},
]


next_id = 4


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)



@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({'error': 'Задача не найдена'}), 404



@app.route('/api/tasks', methods=['POST'])
def create_task():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({'error': 'Данные не заполнены'}), 400

    if 'title' not in data:
        return jsonify({'error': 'Поле title обязательно'}), 400

    new_task = {
        'id': next_id,
        'title': data['title'],
        'done': data.get('done', False)
    }

    tasks.append(new_task)
    next_id += 1

    return jsonify(new_task), 201



@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Данные не заполнены'}), 400

    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['done'] = data.get('done', task['done'])
            return jsonify(task)

    return jsonify({'error': 'Задача не найдена'}), 404



@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Задача удалена'})

    return jsonify({'error': 'Задача не найдена'}), 404


if __name__ == '__main__':
    app.run(debug=True)
