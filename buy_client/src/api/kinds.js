import axios from '@/utils/request'

//获取列表信息（GET）
export const queryKinds = (params) => {
  return axios.post('/api/kinds', { _method: 'GET', _args: params })
}

//删除单条信息
export const deleteKind = (id) => {
  return axios.delete(`/api/kinds/${id}`)
}

//更细单条信息
export const updateKind = (id, params) => {
  return axios.put(`/api/kinds/${id}`, params)
}

//获取单条信息
export const getKind = (id) => {
  return axios.get(`/api/kinds/${id}`)
}

//新增一条数据（POST）
export const createKind = (params) => {
  return axios.post('/api/kinds', params)
}
