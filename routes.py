from flask import request, jsonify
from models import db, Student

def register_routes(app):

    # ADD student
    @app.route('/students', methods=['POST'])
    def add_student():
        data = request.get_json()

        if not data.get("name"):
            return jsonify({"error": "Name is required"}), 400

        new_student = Student(
            name=data["name"],
            age=data.get("age"),
            course=data.get("course")
        )

        db.session.add(new_student)
        db.session.commit()

        return jsonify(new_student.to_dict()), 201


    # GET all students
    @app.route('/students', methods=['GET'])
    def get_students():
        students = Student.query.all()
        return jsonify([s.to_dict() for s in students])


    # GET student by ID
    @app.route('/students/<int:id>', methods=['GET'])
    def get_student(id):
        student = Student.query.get(id)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        return jsonify(student.to_dict())


    # UPDATE student
    @app.route('/students/<int:id>', methods=['PUT'])
    def update_student(id):
        student = Student.query.get(id)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        data = request.get_json()

        student.name = data.get("name", student.name)
        student.age = data.get("age", student.age)
        student.course = data.get("course", student.course)

        db.session.commit()

        return jsonify(student.to_dict())


    # DELETE student
    @app.route('/students/<int:id>', methods=['DELETE'])
    def delete_student(id):
        student = Student.query.get(id)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        db.session.delete(student)
        db.session.commit()

        return jsonify({"message": "Deleted successfully"})