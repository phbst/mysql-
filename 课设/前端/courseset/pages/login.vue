<template>
	<view>
		<view class="head">
			<image class="src" src="../static/googlePalmAvatar.5ca326b0.webp"></image>

		</view>
	
		<view style="height: 75px;"></view>
		
		<view class="password-biginput">
			<input type="safe-password" class="password-input"  v-model="user" placeholder="请输入账号...." />
		</view>
		
		<view style="height: 45px;"></view>
		
		<view class="password-biginput">
			<input type="safe-password" password="true" class="password-input" v-model="password"  placeholder="请输入密码...." />
		</view>
		
		<view style="height: 100px;"></view>
		
		<view>
			<button class="login-button" @click="login" >登录</button>
		</view>
		


		
	</view>
</template>
<script>
	import VueRouter from 'vue-router'
	export default{
		data(){
			return {
				user:"",
				password:""
			}
		},
		methods:{
			login() {
			const url = 'http://127.0.0.1:3000/api/login';
			const data = { "username": this.user, "password": this.password ,"type":"login"};
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
				console.log(JSON.stringify(data));
				
				if(data.message==='error'){
					alert("密码错误或用户不存在")
				}
				else if(data.message==='success'){
					localStorage.setItem('writing_system_token', data.token);
					localStorage.setItem('writing_system_Id', data.id);
					let dpid = '';
					if (data.id == '人事') {
					  dpid = '3';
					} else if (data.id == '销售') {
					  dpid = '2';
					} else if (data.id == '技术') {
					  dpid = '1';
					}
					localStorage.setItem('writing_system_dpId', dpid);
					alert("登录成功！")
					
					this.$router.push('./safe/total');
					
				}

				//在这里处理响应数据
			  })
			  .catch(error => {
				console.error(error);
				// 在这里处理请求错误
			  });  
			}
			
		},
		created() {
				  const token = localStorage.getItem('writing_system_token');
				  if (token){
					  alert("已经登录过了！")
					   window.location.href = 'http://localhost:8080/#/pages/safe/total';
				  } 
				  else{}
				
		}
	}
</script>

<style>
.head{
	display: flex;
	justify-content: center;
	align-items: center;
	height: 125px;
}
.src{
	width: 80px;
	height: 75px;
}
.password-biginput{
	border: 1px solid black;
	border-radius: 30px;
	
}
.password-input{
	padding: 10px;
}
.login-button{
	height: 43px;
	border: 1px solid skyblue;
	background-color:grey;
}
</style>