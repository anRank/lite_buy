<template>
  <div class="app-container">


    <div class="app-container">
      <!-- <div>模板列表</div> -->
        <el-row :gutter="20">
          <el-tabs v-model="activeName" type="card">
            <el-tab-pane v-for="kind in  ['灯光','音响', '舞台']" :label="kind" :name="kind"></el-tab-pane>
          </el-tabs>
        </el-row>

      <el-row :gutter="20" style="min-height: 500px">
        <el-col :span="6" v-for="company in data" :key="company.id" style="padding-top: 20px">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="company.img" class="image" height="125px" width="125px">
            <div style="padding: 14px;">
              <span>公司名称：{{company.name}}公司</span>
              <div class="bottom clearfix">
                <time class="time">{{ company.detail }}</time>
                <div style="float: right">
                    <el-button type="text" >选取</el-button>
                    <el-button style="padding-left: 20px" type="text">租赁</el-button>
                </div>

              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <Sticky stickyTop="800px">
      <el-col :span="24" class="toolbar">
        <el-pagination
          @current-change="onPageChange"
          :current-page="pages._page"
          :page-size="pages._per_page"
          background
          layout="total, prev, pager, next"
          :total="total"
          style="float:right;">
        </el-pagination>
      </el-col>
        <pick_company :companys="data" style="position: absolute; bottom:250px; right: 0px" @click="show=!show"></pick_company>
      </Sticky>


    </div>
  </div>
</template>

<script>
  //mixin
  //视频接口
  import commonTable from '@/mixins/table'
  import { queryCompanys} from '@/api/company'
  import Sticky from '@/components/Sticky'
  import pick_company from '@/views/components/pick_company'


  export default {
    mixins: [commonTable],
    components: {  Sticky, pick_company},
    data() {
      return {
        //配置minxin种curd api方法：
        queryMethod: queryCompanys,

        //配置resource_name
        resource_name: 'company',
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

  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>
