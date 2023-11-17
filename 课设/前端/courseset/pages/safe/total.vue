<template>	
	<div class="body">
		<div class="pad"></div>
		<div class="real">
			
			<div class="parts" @click="handleClick('sys')">
				系统管理信息权限
			</div>
			<div class="parts" @click="handleClick('write')">
				行文撰写
			</div>
			<div class="parts" @click="handleClick('alter')">
				行文修改与发送(本部)
			</div>
			<div class="parts" @click="handleClick('recive')">
				行文接收(本部)
			</div>
			<div class="parts"  @click="handleClick('select')">
				行文查询
			</div>
			<div class="parts" @click="handleClick('help')">
					帮助
			</div>
			


			<div class="parts" style="width: 30vh;float:left ;background-color: #55ffff;">
					当前登录管理人员：{{id}}部门
			</div>
			<div class="parts"  @click="exit()">
					注销
			</div>
		</div>
		<div class="pad"></div>		
	</div>

</template>

<script>
export default{
	data() {
		return {
			id:""
		}
	},
	methods:{
		handleClick(item) {
		      this.$router.push('./parts/'+item);

		},
		exit(){
				localStorage.removeItem('writing_system_token');
				localStorage.removeItem('writing_system_Id');
				window.location.href = 'http://localhost:8080/#/pages/login';
				
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
	background-color: white;	
	height: 100vh;
	display: flex;
	 
	
	
}
.real{
	display: flex;
	flex: 5;
	background-color: #ffffff;
	flex-wrap: wrap;
	background-image:url("../../static/下载 (1).jpg")
/* 	background-color: antiquewhite; */
}
.pad{
	display: flex;
	flex: 1;
	background-image:url("../../static/下载 (1).jpg")
}
.parts{
	width: 20vh;
	height: 20vh;
	background-color:#55ff7f;
	margin-left: 10px;
	display: flex;
	margin-top: 50px;
	border: 1px solid black ;
	border-radius: 20%;
	justify-content: center;
	align-items: center;
	cursor: pointer;
	
}

.parts:hover{
	background-color: #dddddd;
}
</style>