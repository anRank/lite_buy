import os
import easyapi
from flask import Blueprint, request, jsonify, send_file
# from flask_jwt import jwt_required, current_identity
import app.controller as controller
from app.config import Config


file_bp = Blueprint(name='files', import_name='files', url_prefix='/files')

# 上传文件
@file_bp.route('/upload/<string:source_type>', methods=['POST'])  # 不写,methods=['GET','POST'] 默认是get
def file_upload(source_type):
    try:
        file = request.files['file']
        origin_file_path = ''
        if source_type == 'image':
            origin_file_path = controller.FileController.upload(file=file, file_path=Config.UPLOAD_IMAGE_PATH)
        elif source_type == 'audio':
            origin_file_path = controller.FileController.upload(file=file, file_path=Config.UPLOAD_AUDIO_PATH)
        elif source_type == 'video':
            origin_file_path = controller.FileController.upload(file=file, file_path=Config.UPLOAD_VIDEO_PATH)

    except easyapi.BusinessError as e:
        return jsonify(**{
            'msg': e.err_info,
            'code': e.code,
        }), e.http_code
    return jsonify(**{
        'msg': '上传成功',
        'code': 200,
        'file_path': origin_file_path
    })

#下载文件
@file_bp.route('/download/<string:source_type>/<string:file_name>', methods=['GET'])
def file_download(source_type,file_name):
    """
    :param file_name: 文件名称 "**********.jpg"
    :return:
    """
    try:
        origin_file_path = ''
        if source_type == 'image':
            origin_file_path = os.path.join(Config.UPLOAD_IMAGE_PATH, file_name)
        if source_type == 'audio':
            origin_file_path = os.path.join(Config.UPLOAD_AUDIO_PATH, file_name)
        if source_type == 'video':
            origin_file_path = os.path.join(Config.UPLOAD_VIDEO_PATH, file_name)

        return send_file(origin_file_path)  #向api返回文件
    except easyapi.BusinessError as e:
        return jsonify(**{
            'msg': e.err_info,
            'code': e.code,
        }), e.http_code

#删除文件
@file_bp.route('/delete/<string:source_type>/<string:file_name>', methods=['DELETE'])
def file_delete(source_type ,file_name):
    """
    :param file_name: 文件名称 "**********.jpg"
    :return:
    """
    try:
        result = ''
        if source_type == 'image':
            result = controller.FileController.delete( file_path=Config.UPLOAD_IMAGE_PATH, file_name=file_name)
        if source_type == 'audio':
            result = controller.FileController.delete(file_path=Config.UPLOAD_AUDIO_PATH, file_name=file_name)
        if source_type == 'video':
            result = controller.FileController.delete(file_path=Config.UPLOAD_VIDEO_PATH, file_name=file_name)

    except easyapi.BusinessError as e:
        return jsonify(**{
            'msg': e.err_info,
            'code': e.code,
        }), e.http_code
    if result:
        return jsonify(**{
            'msg': '删除成功',
            'code': 200,
            'res': result
        })
    else:
        return jsonify(**{
            'msg': '删除失败',
            'code': 200,
            'res': result
        })
