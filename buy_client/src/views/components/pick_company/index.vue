<template>
    <div>
      <el-button icon="el-icon-files" type="primary"  @click="()=>{this.drawer = true}">随机选取</el-button>
      <el-drawer
        title="我是标题"
        :visible.sync="drawer"
        direction="rtl">
        <span slot="title">随机抽选</span>
        <div>
          <ul style="list-style-type:none">
           <li v-for="company in companys" >
             <el-button type="danger" icon="el-icon-delete" circle ></el-button>
             {{company.name}}公司
           </li>
          </ul>
          <el-button type="primary" style="float: right;">随机选取</el-button>
        </div>
      </el-drawer>
    </div>
</template>

<script>
    export default {
        name: "index",
        props: {
          companys: {type: Array, default:[]}
        },
        data: function () {
          return {
            drawer: false,
          }
        }
    }
</script>

<style scoped>
  ul li{margin:0;padding:0}
</style>
