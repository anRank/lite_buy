import axios from '@/utils/request'

//获取列表信息（GET）
export const queryCompanys = (params) => {
  return axios.post('/api/companys', { _method: 'GET', _args: params })
}

//删除单条信息
export const deleteCompany = (id) => {
  return axios.delete(`/api/companys/${id}`)
}

//更细单条信息
export const updateCompany = (id, params) => {
  return axios.put(`/api/companys/${id}`, params)
}

//获取单条信息
export const getCompany = (id) => {
  return axios.get(`/api/companys/${id}`)
}

//新增一条数据（POST）
export const createCompany = (params) => {
  return axios.post('/api/companys', params)
}
