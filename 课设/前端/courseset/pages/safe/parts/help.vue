<template>
	<view class="body">
		<div class="pad"></div>
		<div class="real">
			<image class="img" src="../../../static/e8226e1dff023755975445083a078c9.png" ></image>
		</div>
		<div class="pad"></div>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		},
		created() {
		  const token = localStorage.getItem('writing_system_token');
		  if (token){} 
		  else
		  {
			  alert("用户未进行登录！")
		    window.location.href = 'http://localhost:8080/#/pages/login';
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

}
.pad{
	display: flex;
	flex: 1;
}
	.img{
		width: 80%; /* 设置图像的宽度，根据需要调整 */
		  height: 80%; /* 设置图像的高度，根据需要调整 */
		  /* 图像完整显示，保持纵横比，可能会留有空白边 */
		  /* object-fit: cover; */ /* 图像完整显示，填充容器，可能会裁剪部分图像 */
		  /* object-fit: fill; */ /* 图像拉伸以填充容器，可能会扭曲纵横比 */
		  /* object-fit: none; */ /* 图像原始大小，可能会溢出容器 */
	}

</style>
