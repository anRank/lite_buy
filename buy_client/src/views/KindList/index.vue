<template>
  <div class="app-container">


    <div class="app-container">
      <!-- <div>模板列表</div> -->

      <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
        <el-form :inline="true" v-model="query">
          <el-form-item label="类目名称：">
            <el-input v-model="query._like_name" placeholder="类目名称"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSearch">查询</el-button>
          </el-form-item>
          <el-form-item>
            <el-button plain @click="onReset">重置</el-button>
          </el-form-item>

          <el-form-item style="float: right">
            <el-button type="success"  @click="onNewClick">添加类目</el-button>
          </el-form-item>
        </el-form>
      </el-col>


      <el-table
        :data="data"
        v-loading="tableLoading"
        @sort-change="onSort">

        <el-table-column
          prop="id"
          label="id"
          sortable
          width="80">
        </el-table-column>
        <el-table-column
          prop="name"
          label="类目名称"
        >
          <template slot-scope="scope">
            {{ scope.row.name }}
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="danger"
              @click="onDeleteClick(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>

      <el-col :span="24" class="toolbar">
        <el-pagination
          @current-change="onPageChange"
          :current-page="pages._page"
          :page-size="pages._per_page"
          layout="total, prev, pager, next"
          :total="total"
          style="float:right;">
        </el-pagination>
      </el-col>

      <CreatorDialog
        :visible="newDialogShow"
        @onOK="onNewOK"
        @onCancel="onNewCancel">
      </CreatorDialog>

    </div>
  </div>
</template>

<script>
  //mixin
  import commonTable from '@/mixins/table'
  //视频接口
  import { queryKinds, deleteKind, updateKind, getKind, createKind } from '@/api/kinds'

  import CreatorDialog from './components/newDialog.vue'

  export default {
    mixins: [commonTable],
    components: { CreatorDialog },
    data() {
      return {
        //配置minxin种curd api方法：
        newMethod: createKind,
        deleteMethod: deleteKind,
        updateMethod: updateKind,
        getMethod: getKind,
        queryMethod: queryKinds,

        //配置resource_name
        resource_name: 'kind',

        //配置mixin query
        query: {  //条件查询 dict  //api查询条件dict
          _like_name: undefined
        },

        data: [],  //列表

      }
    },
    created() {
    },
    methods: {
      //Rewrite minxin onReset()  查询条件重置
      onReset() {
        this.query = {  //条件查询 dict
          _like_name: undefined
        }
        this.order = { _order_by: 'id', _desc: true } //order 在
        this.pages._page = 1
        this.fetchData()
      },



    },
    mounted() {
      // window.vue = this

    }

  }
</script>
<style scoped>
  .toolbar {
    background: #f2f2f2;
    padding: 10px;
    margin: 10px 0px;
  }

  .toolbar .el-form-item {
    margin-bottom: 10px;
  }
</style>
