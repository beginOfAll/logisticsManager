var jz = {
	load:function(url,callback){
		$.ajax(url,{
			type:"get",
			async:false,
			cache:false,
			contentType:"application/json;charset=utf-8",
			data:"",
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	},
	getAsync:function(url,callback){
		$.ajax(url,{
			type:"get",
			async:true,
			cache:false,
			contentType:"application/json;charset=utf-8",
			data:"",
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	},
	getByPara:function(url,para,callback){
		$.ajax(url,{
			type:"get",
			async:false,
			cache:false,
			contentType:"application/json;charset=utf-8",
			data:para,
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	},
	getByParaAsync:function(url,para,callback){
		$.ajax(url,{
			type:"get",
			async:true,
			cache:false,
			contentType:"application/json;charset=utf-8",
			data:para,
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	},
	postByPara:function(url,para,callback){
		$.ajax(url,{
			type:"post",
			async:false,
			cache:false,
			data:para,
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	},
	postFileByPara:function(url,para,callback){
		$.ajax(url,{
			type:"POST",
			async:false,
			data:para,
			contentType:false,
			processData: false,
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	},
	postByParaAsync:function(url,para,callback){
		$.ajax(url,{
			type:"post",
			async:true,
			cache:false,
			data:para,
			success:function(result){
				if($.isFunction(callback)){
					callback(result);
				}
			},
			error:function(xhr,status,error){
				alert(error);
			}
		});
	}
}