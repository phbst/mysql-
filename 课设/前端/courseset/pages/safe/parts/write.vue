	<template>
		<view class="body">
			<div class="pad"></div>
			<div class="real">
				<div class="label">
					<div>行文编号:</div>
					<div>
						<input placeholder="" class="input" v-model="id" />
					</div>
				</div>
				<div class="label">
					<div>行文标题:</div>
					<div>
						<input placeholder="" class="input" v-model="title"/>
					</div>
				</div>
				<div class="label">
					<div>行文作者:</div>
					<div>
						<input placeholder="" class="input" v-model="writer"/>
					</div>
				</div>

				<div class="label">
					<div>行文日期:</div>
					<div>
						<input placeholder="" class="input" v-model="time"/>
					</div>
				</div>
				<div class="label" style="height:18vh;margin-bottom: 5vh;">
					<div>行文正文:</div>
					<div>
						<textarea v-model="xwcontent" class="text"></textarea>
					</div>
				</div>
				<div class="btn">
					<button @click="xwsave">保存行文</button>
					<button @click="dele">清除</button>
				</div>

			</div>
			<div class="pad"></div>
			
		</view>
	</template>

	<script>
		export default {
			data() {
				return {
					id:"",
					title:"",
					writer:"",
					time:"",
					xwcontent:"",
					
				}
			},
			methods: {
				dele(){
					this.id="",
					this.title="",
					this.writer="",
					this.time="",
					this.xwcontent=""
				},
				xwsave(){
					const url = 'http://127.0.0.1:3000/api/write';
					const data = { 
						id:this.id,
						title:this.title,
						writer:this.writer,
						time:this.time,
						xwcontent:this.xwcontent
					};
					const options = {
					  method: 'POST',
					  headers: {
						'Content-Type': 'application/json'
					  },
					  body: JSON.stringify(data)
					};
					fetch(url,options)
					.then(response => response.json())
					.then(data => {
							console.log(JSON.stringify(data));
									
							if(data.code==='error'){
								alert("保存失败")
							}
							else if(data.code==='success'){
								alert("保存成功")
							}
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
			// mounted(){
				
			// 	const Id = localStorage.getItem('writing_system_Id');
			// 	if(Id){
			// 		this.id=Id
			// 	}
			// }
					
			
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
	.input{
		border: 1px solid black;
		width: 50vh;
	}
	.label{
		display: flex;
		flex-direction: row;
		height: 5vh;

		width: 100vh;
		justify-content: center;
		align-items: center;
		margin-top: 20px;
		
	}
	.text{
		border: 1px solid black;
		width: 50vh;
	}
	.btn{
		
		display: flex;
		flex-direction: row;
		height: 5vh;
		width: 100vh;
		justify-content: center;
		align-items: center;
		margin-top: 20px;
		margin-left: 20px;
			}
	</style>
