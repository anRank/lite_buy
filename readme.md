<!--
 * @Author: your name
 * @Date: 2020-03-26 16:40:29
 * @LastEditTime: 2020-03-26 16:40:40
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 
 * @FilePath: /buy_company/readme.md
 -->


新增公司

```
POST /companys HTTP/1.1
Host: 0.0.0.0:5000
Content-Type: application/json

{
	"name": "A 公司",
	"owner": "测试",
	"tele": "15311070339",
	"detail": "详情",
	"type": "采购",
	"production_kind": ["灯光", "舞台"]
}
```

