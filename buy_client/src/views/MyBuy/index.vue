<template>
  <div class="app-container">


    <div class="app-container">
      <!-- <div>模板列表</div> -->



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
          prop="company_name"
          label="公司名称"
        >
          <template slot-scope="scope">
            {{ scope.row.company_name }}公司
          </template>
        </el-table-column>

        <el-table-column
          prop="bus"
          label="中标类型"
        >
          <template slot-scope="scope">
            <el-tag >租赁</el-tag>
          </template>
        </el-table-column>

        <el-table-column
          prop="bus"
          label="类别"
        >
          <template slot-scope="scope">
            <el-tag >灯光</el-tag>
          </template>
        </el-table-column>

        <el-table-column
          prop="created_at"
          label="时间"
        >
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
  import { queryResults, deleteResult, updateResult, getResult, createResult } from '@/api/results'

  import CreatorDialog from './components/newDialog.vue'

  export default {
    mixins: [commonTable],
    components: { CreatorDialog },
    data() {
      return {
        //配置minxin种curd api方法：
        newMethod: createResult,
        deleteMethod: deleteResult,
        updateMethod: updateResult,
        getMethod: getResult,
        queryMethod: queryResults,

        //配置resource_name
        resource_name: 'result',

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
