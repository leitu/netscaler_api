from flask_restful import Resource
import random

class Task(Resource):
  def get(self, task_id):
    statuses = ['INIT', 'IN_PROGRESS', 'COMPLETE', 'FAILED']
    a = random.randint(0, 3)
    return {'task_id': task_id, 'status': statuses[a]}
