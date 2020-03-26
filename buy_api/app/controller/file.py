import os, uuid
from easyapi import EasyApiContext
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


class FileController():

    # ALLOW_TYPE = ['video/mp4', 'video/mpeg']

    @classmethod
    def upload(cls, file: FileStorage, file_path: str):
        """
        文件上传
        :param file: 文件对象
        :param file_path:  文件存储路径
        :return: 文件存储名称  *******.jpg
        """
        # if file.mimetype not in cls.ALLOW_TYPE:
        #     raise easyapi.BusinessError(code=500, http_code=200, err_info="不是允许的文件")
        # 没做规定的文件类型

        #防重复
        title, file_extension = os.path.splitext(secure_filename(file.filename))
        uuid_1 = str(uuid.uuid1().hex)
        file_name = uuid_1 + file_extension  # 存储的文件名
        origin_file_path = os.path.join(file_path, file_name)  # 文件存储路径
        file.save(origin_file_path)

        # filename = secure_filename(file.filename)
        # file.save(os.path.join(file_path, filename))

        # 返回的是存储路径
        return origin_file_path

    @classmethod
    def download(cls, file_path, file_name):
        """
        文件下载 逻辑不复杂 都在handler里面
        :return:
        """
        pass

    @classmethod
    def delete(cls,file_path, file_name):

        origin_file_path = os.path.join(file_path, file_name)  # 文件存储路径

        if os.path.exists(origin_file_path):
            os.remove(origin_file_path)
            return True
        else:
            return False

