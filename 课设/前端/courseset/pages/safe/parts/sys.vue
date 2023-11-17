<template>
	<view class="body">
		<div class="pad"></div>
		<div class="real">
			<div style="align-items: center;justify-content: center; font-size: 6ex;">
				当前登录人员：{{ID}}行文管理员{{dpid}}
			</div>
			<div class="ouput">

				<div>
					<table>
					     <thead>
					       <tr>
					         <th>员工号</th>
					         <th>姓名</th>
					         <th>部门编号</th>
							 <th>性别</th>
					         <th>手机号</th>
					         <th>邮箱</th>
					       </tr>
					     </thead>
					     <tbody>
					       <tr v-for="item in tableData" :key="item.id">
					         <td>{{ item.id }}</td>
					         <td>{{ item.name }}</td>
					         <td>{{ item.dpid }}</td>
							 <td>{{item.sex}}</td>
					         <td>{{ item.phone }}</td>
					         <td>{{ item.email }}</td>
							
					       </tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
		<div class="pad"></div>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				ID:"",
				tableData:[],
				dpid:""
			}
		},
		methods: {
			
		},
		created() {
		    const token = localStorage.getItem("writing_system_token");
		    if (token) {
		      // 用户已登录，获取数据
		      const url = "http://127.0.0.1:3000/api/sys";
		      const data = {
		        type: status, // 你需要定义status的值
		      };
		      const options = {
		        method: "POST",
		        headers: {
		          "Content-Type": "application/json",
		        },
		        body: JSON.stringify(data),
		      };
		
		      fetch(url, options)
		        .then((response) => response.json())
		        .then((data) => {
		          console.log(data);
		          this.tableData = data;
		        })
		        .catch((error) => {
		          console.error("Error fetching data:", error);
		        });
		    } else {
		      alert("用户未进行登录！");
		      window.location.href = "http://localhost:8080/#/pages/login";
		    }
		  },
		mounted(){
			const Id = localStorage.getItem('writing_system_Id');
			if(Id){
				this.ID=Id
			}
			const dpId = localStorage.getItem('writing_system_dpId');
			if(dpId){
				this.dpid=dpId
			}
			
		}
	}
</script>

<style>
.body{
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
table {
  border-collapse: collapse;
  width: 100%;
}

table th,
table td {
  border: 1px solid gray;
  padding: 8px;
}
.ouput{
	height: 60vh;
	margin-top: 10vh;
	border: 1px solid grey;
	overflow: auto;
}
</style>
