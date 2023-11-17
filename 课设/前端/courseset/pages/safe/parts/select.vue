<template>
	<view class="body">
		<div class="pad"></div>
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
				        </tr>
				      </thead>
				      <tbody>
				        <tr v-for="item in tableData" :key="item.id">
				          <td>{{ item.id }}</td>
				          <td>{{ item.title }}</td>
				          <td>{{ item.writer }}</td>
				          <td>{{ item.time }}</td>
				          <td>{{ item.xwcontent }}</td>
						  <td>{{item.fla}}</td>
						  
				        </tr>
				      </tbody>
				</table>
			</div>
			<div class="options">
				<button @click="allinfo('all')" style="margin-bottom: 5px;"> 查询所有行文</button>
				<button @click="allinfo('y')" style="margin-bottom: 5px;"> 查询已发送行文</button>
				<button @click="allinfo('w')" style="margin-bottom: 5px;"> 查询未发送行文</button>
			</div>
		</div>
		<div class="pad"></div>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tableData: []
			}
		},
		methods: {
			allinfo(status){
				const url = 'http://127.0.0.1:3000/api/select';
				const data = { 
					type:status
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
				    this.tableData = data; 
				    })
				    .catch(error => {
						console.error('Error fetching data:', error);
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
	margin-top: 10vh;
	border: 1px solid grey;
	overflow: auto;


}
.options{
	height: 20vh;
	margin-top: 10px;
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
  width: 40vh; /* 调整宽度大小为适合的值 */
  word-wrap: break-word; /* 允许自动换行 */
}

</style>
