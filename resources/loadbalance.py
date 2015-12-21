from storage_api.resources.base import Base

class Loadbalances(Base):
  def get(self):
    print self.queue('loadbalance', 'list', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202

  def post(self):
    print self.queue('loadbalance', 'create', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202


class Loadbalance(Base):
  def get(self,loadbalance):
    print self.queue('loadbalance', 'info', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202

  def delete(self, loadbalance):
    print self.queue('loadbalance', 'delete', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202


# class LoadbalanceName(Base):
#   def put(self, volume):
#     self.reqparse.add_argument('new_name', type=str, required=True)
#     print self.queue('volume', 'rename', self.reqparse.parse_args())
#     return {'task_id': self.uuid}, 202


# class Servers(Base):
#   def put(self, server):
#     self.reqparse.add_argument('volume_size', type=netapp_size, required=True)
#     print self.queue('volume', 'resize', self.reqparse.parse_args())
#     return {'task_id': self.uuid}, 202


class Server(Base):
  def get(self, server):
    print self.queue('server', 'list', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202

  def put(self, server):
    print self.queue('server', '', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202

  def delete(self, server):
    print self.queue('server', 'delete', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202


class Services(Base):
  def get(self, service):
    print self.queue('service', '', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202

  def post(self, service):
    print self.queue('server', '', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202


class Service(Base):
  def delete(self, service):
    print self.queue('service', '', self.reqparse.parse_args())
    return {'task_id': self.uuid}, 202

