import uuid
from datetime import datetime
from flask_restful import Resource, reqparse, fields, marshal_with
from netscaler_api.common.queue import Queue

class Base(Resource):
  fields = {
      'task_id': fields.String,
      'task_uri': fields.Url('task')
  }
  decorators = [marshal_with(fields)]

  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('loadbalance', type=str, required=True)
    self.uuid = str(uuid.uuid4())
    self.user = 'joebloggs' # FIXME
    url = 'amqp://test:test@127.0.0.1:5672/%2F' # FIXME
    self.mq = Queue(url, key='loadblance') #api input
    super(Base, self).__init__()

  def queue(self, name, action, args):
    body = {
      'task_id': self.uuid,
      'user': self.user,
      'creation_time': datetime.utcnow().isoformat(),
      'loadbalance': args.pop('loadbalance'),
      'action': action,
      'object': name,
      'arguments': args
    }
    self.mq.send_message(body)
    return body
