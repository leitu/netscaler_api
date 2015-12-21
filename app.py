from flask import Flask
from flask_restful import Api
from netscaler_api.resources.task import Task
from netscaler_api.resources.loadbalance import Loadbalances, Loadbalance, LoadbalanceName,Servers, Server, Services, Service

from netscaler_api.common.util import initialize_logging

initialize_logging('logging.conf')
app = Flask(__name__)
api = Api(app)

api.add_resource(Task, '/v1/task/<string:task_id>')

api.add_resource(Loadbalances, '/v1/lb/')
api.add_resource(Loadbalance, '/v1/lb/<string:lb>')
# api.add_resource(LoadbalanceName, '/v1/lb/<string:lb>/name')


api.add_resource(Servers, '/v1/lb/<string:lb>/server/')
api.add_resource(Server, '/v1/lb/<string:lb>/server/<string:server>')

api.add_resource(Services, '/v1/lb/<string:lb>/service/')
api.add_resource(Service, '/v1/lb/<string:lb>/service/<string:service>')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
