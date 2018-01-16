/**
 * Created by jhbai on 15/01/2018.
 */
$(document).ready(function(){
	/*
	 *全选和全不选
	 */
	$(".selected-btu").click(function(){
	    var checked = this.checked;
       //$("input[name=id[]]:checkbox").attr("checked",this.checked);
        $("input[name='id[]']:checkbox").each(function (index, domEle) {
            $(domEle).attr("checked",checked);
    	 });
    });

   /*
    *删除数据
    *
    *e.preventDefault();阻止默认行为，不让提交
    * 获取url;
    */
   $(".delete-btu").click(function(e){
	    e.preventDefault();
        var url = $(this).attr("href");
        submit_form(url);
   });

   function submit_form(url){
       var count = 0;
       var id = "",step=""
       $("input[name='id[]']:checkbox").each(function (index, domEle) {
    	   if($(domEle).is(':checked') ){
               count++;
               id += step + $(domEle).val()
               step = ","
            }
    	 });

       if(count <= 0 ){
            alert("请选择删除记录");
            return ;
       }
       $("#ids").val( id )
       var form =$("#data-form").get(0);
       form.action = url;
       form.submit();
  }
});