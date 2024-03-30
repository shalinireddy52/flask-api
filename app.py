from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulating a simple in-memory database
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build a REST API", "done": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()  # Get the JSON data from the request
    new_task = {
        "id": len(tasks) + 1,
        "title": task_data.get("title"),
        "done": task_data.get("done", False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_data = request.get_json()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["title"] = task_data.get("title", task["title"])
        task["done"] = task_data.get("done", task["done"])
        return jsonify(task)
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Task deleted"})
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
