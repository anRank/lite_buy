import os
from flask import Flask
from flask_cors import CORS
from app.config import Config
import app.handler as handler


app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'),
        static_folder=os.path.join(os.getcwd(), 'static'))

# 利用flask-cors解决跨域问题，/*允许所有域外请求通过
cors = CORS(app, resources={r"/*": {"origins": "*"}})
cors.init_app(app)  # 跨域初始化
app.config.from_object(Config)

#注册各个模块蓝图
app.register_blueprint(handler.kind_bp)
app.register_blueprint(handler.company_bp)
app.register_blueprint(handler.results_bp)
