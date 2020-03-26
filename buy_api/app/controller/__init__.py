
from app import dao
import easyapi
from easyapi import EasyApiContext



TYPE_MAPPING = {
    0: '租赁',
    1: '采购'
}

TYPE_MAPPING_REV = {v:k for k, v in TYPE_MAPPING.items()}


class KindController(easyapi.BaseController):
    __dao__ = dao.KindDao


class CompanyController(easyapi.BaseController):
    __dao__ = dao.CompanyDao

    #formatter是out   reformatter是in 进入db
    @classmethod
    def formatter(cls, ctx: EasyApiContext , data: dict):
        data['production_kind'] = [k[1:-1] for k in  data.get('production_kind', '').split(',')]
        data['type'] = TYPE_MAPPING[data.get('type', 0)] 
        return data

    @classmethod
    def reformatter(cls, ctx: EasyApiContext , data: dict):
        if 'production_kind' in data:
            data['production_kind'] = ','.join('|{}|'.format(k) for k in   data['production_kind'])
        if 'type' in data:
            data['type'] = TYPE_MAPPING_REV[data['type']]
        return data


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
