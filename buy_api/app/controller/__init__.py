
from app import dao
import easyapi
from easyapi import EasyApiContext



class KindController(easyapi.BaseController):
    __dao__ = dao.KindDao


class CompanyController(easyapi.BaseController):
    __dao__ = dao.CompanyDao


class ResultController(easyapi.BaseController):
    __dao__ = dao.ResultDao

    @classmethod
    def formatter(cls, ctx: EasyApiContext , data: dict):
        data = cls.formatter(ctx, data)
        data['company'] = dao.CompanyDao.get(ctx=ctx, query={
            "id": data["company_id"]
        })
        return data

from app.controller.file import *
