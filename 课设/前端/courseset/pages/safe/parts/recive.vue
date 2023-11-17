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
				          <th>行文接受部门号</th>
				          <th class="wide-cell">行文内容</th>
						  <th>时间</th>
						  <th>描述</th>
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
						  <td>{{item.title}}</td>
						  <td>{{item.writer}}</td>
						  <td>{{ item.reciver }}</td>
				          <td>{{ item.xwcontent}}</td>
				          <td>{{ item.time }}</td>
				          <td>
				            <span v-if="!item.editable">{{ item.dcp }}</span>
				            <textarea v-else v-model="item.newcontent"></textarea>
				          </td>
						  <td style="display: flex;flex-direction: row;">
							  <button @click="edit(item)" style="margin-right: 8px ;">编辑</button>
							  <button @click="save(item)">保存</button>
						  </td>
						  
						  
				        </tr>
				      </tbody>
				</table>
			</div>
			<div class="options">

				<button @click="recive()" style="margin-bottom: 5px;"> 接收行文</button>
			
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
				id:""
			}
		},
		methods: {
			recive(){
				const url = 'http://127.0.0.1:3000/api/recive';
				const dpId=localStorage.getItem('writing_system_dpId')
				const data = { 

					id:dpId
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
			      this.$set(item, 'newcontent', item.dcp);
			},
			save(item){
				this.$set(item, 'editable', false);
				
				console.log('Saving row:', item);
				      
				item.dcp = item.newcontent;
				const updatedContent = item.dcp; 
				
				  // 构建请求数据
				  const data = {
				    id: item.id, // 你可能还需要发送一些其他标识符
				    content: updatedContent,
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
				  fetch('http://127.0.0.1:3000/api/edit', options)
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
	margin-top: 20px;

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
