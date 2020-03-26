
from app.handler.file import *
from app import controller

kind_bp = Blueprint(name='kinds', import_name='kinds', url_prefix='')


class KindHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.KindController


easyapi.register_api(app=kind_bp, view=KindHandler, endpoint='kind_api', url='/kinds')



company_bp = Blueprint(name='companys', import_name='companys', url_prefix='')


class CompanyHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.CompanyController


easyapi.register_api(app=company_bp, view=CompanyHandler, endpoint='company_api', url='/companys')




results_bp = Blueprint(name='retuls', import_name='retuls', url_prefix='')


class ResultHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.ResultController


easyapi.register_api(app=results_bp, view=ResultHandler, endpoint='result_api', url='/results')
