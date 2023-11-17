<template>
	<view class="body">
		<div class="pad" style="display: flex;justify-content: center;align-items: center;">
			<div style="font-size: 30px;color: red;">{{id}}部门</div>
		</div>
		<div class="real">
			<div class="ouput">
				 <table>
				      <thead>
				        <tr>
				          <th>行文号</th>
				          <th>行文标题</th>
				          <th>行文作者员工号</th>
				          <th>时间</th>
				          <th class="wide-cell">行文内容</th>
						  <th>是否发送</th>
						  <th>操作选项</th>
				        </tr>
				      </thead>
				      <tbody>
				        <tr v-for="item in tableData" :key="item.id">
				          <td>{{ item.id }}</td>
<!-- 				          <td>
				            <span v-if="!item.editable">{{ item.title }}</span>
							<textarea v-else v-model="item.updatedtitle"></textarea>
						  </td> -->
						  <td>{{ item.title }}</td>
				          <td>{{ item.writer }}</td>
				          <td>{{ item.time }}</td>
				          <td>
				            <span v-if="!item.editable">{{ item.xwcontent }}</span>
				            <textarea v-else v-model="item.updatedContent"></textarea>
				          </td>
						  <td>{{item.fla}}</td>
						  <td style="display: flex;flex-direction: row;">
							  <button @click="edit(item)" style="margin-right: 8px ;">编辑</button>
							  <button @click="save(item)">保存</button>
						  </td>
						  
						  
				        </tr>
				      </tbody>
				</table>
			</div>
			<div class="options">

				<button @click="info('all')" style="margin-bottom: 5px;"> 查询本部行文</button>
				<button @click="info('y')" style="margin-bottom: 5px;"> 查询本部已发行文</button>
				<button @click="info('w')" style="margin-bottom: 5px;"> 查询本部未发行文</button>
				
				<div style="display: flex;flex-direction: column;">
					<input placeholder="请输入要发送的行文编号" v-model="xw_id" style="border: 1px solid black; margin-top:10px;"/>
					<input placeholder="请输入要发送的部门编号" v-model="dp_id" style="border: 1px solid black;margin-top:10px;"/>
				</div>
				<button @click="sent()">发送行文</button>
			</div>
		</div>
		<div class="pad" style="display: flex;justify-content: center;align-items: center;">
			<div style="font-size: 30px;color: red;">{{id}}部门</div>
		</div>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tableData: [],
				dp:"",
				id:"",
				dp_id:"",
				xw_id:""
			}
		},
		methods: {
			info(status){
				const dpId=localStorage.getItem('writing_system_dpId')
				const url = 'http://127.0.0.1:3000/api/alter';
				const data = { 
					type:status,
					dpid:dpId
				};
				const options = {
				  method: 'POST',
				  headers: {
					'Content-Type': 'application/json'
				  },
				  body: JSON.stringify(data)
				};
				fetch(url, options)
				.then(response => response.json())
				.then(data => {
					console.log(data); 
					data.forEach((item) => {
					          this.$set(item, 'editable', false);
					        });
				    this.tableData = data; 
				    })
				    .catch(error => {
						console.error('Error fetching data:', error);
				    });

			},
			edit(item) {
			      this.$set(item, 'editable', true);
			      this.$set(item, 'updatedContent', item.xwcontent);
			},
			save(item){
				this.$set(item, 'editable', false);
				
				console.log('Saving row:', item);
				      
				item.xwcontent = item.updatedContent;
				const updatedContent = item.updatedContent;
				
				  // 构建请求数据
				  const data = {
				    xwid: item.id, // 你可能还需要发送一些其他标识符
				    newcontent: updatedContent,
				  };
				
				  // 构建请求选项
				  const options = {
				    method: 'POST',
				    headers: {
				      'Content-Type': 'application/json',
				    },
				    body: JSON.stringify(data),
				  };
				
				  // 发送请求
				  fetch('http://127.0.0.1:3000/api/save', options)
				    .then(response => response.json())
				    .then(data => {
				      console.log('Updated content successfully:', data);
				      item.editable = false;
					  const result=data.code
					  if(result=='200'){
						  alert("保存成功")
					  }
					  else{
						  alert('保存失败')
					  }
				    })
				    .catch(error => {
				      console.error('Error updating content:', error);
				      // 这里你可以处理错误的情况，比如显示错误消息。
				    });
			},
			sent(){
				const url = 'http://127.0.0.1:3000/api/sent';
				const data = { 
					xwid:this.xw_id,
					dpid:this.dp_id
				};
				const options = {
				  method: 'POST',
				  headers: {
					'Content-Type': 'application/json'
				  },
				  body: JSON.stringify(data)
				};
				fetch(url, options)
				.then(response => response.json())
				.then(data => {
					console.log(data); 
					const result=data.code
					if(result=='200'){
						alert("发送成功")
					}
					else{
						alert("发送失败")
					}
				})
				.catch(error => {
					console.error('Error fetching data:', error);
				});
			}
		},
		created() {
		  const token = localStorage.getItem('writing_system_token');
		  if (token){} 
		  else
		  {
			  alert("用户未进行登录！")
		    window.location.href = 'http://localhost:8080/#/pages/login';
		}
		
		},
		mounted(){
			
			const Id = localStorage.getItem('writing_system_Id');
			if(Id){
				this.id=Id
			}
		}
	}
</script>

<style>
.body{
	/* background-image: url("../../../static/下载.jpg"); */
	background-color: white;	
	height: 100vh;
	display: flex;
	 
	
	
}
.real{
	display: flex;
	flex: 3;
	background-color: #ffffff;
	flex-direction: column; 
	

}
.pad{
	display: flex;
	flex: 1;
}
.ouput{
	height: 60vh;
	margin-top: 5vh;
	border: 1px solid grey;
	overflow: auto;


}
.options{
	height: 10vh;
	margin-top: 10px;
	display: flex;
/* 	background-color: aqua; */
}
table {
  border-collapse: collapse;
  width: 100%;
}

table th,
table td {
  border: 1px solid gray;
  padding: 8px;
}
.wide-cell {
  width: 50vh; /* 调整宽度大小为适合的值 */
  word-wrap: break-word; /* 允许自动换行 */
}

</style>
