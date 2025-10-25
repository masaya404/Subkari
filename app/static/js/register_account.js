console.log("register_account is loaded.");
const errorMes = {
    email: "メールを入力してください",
    password: "パスワードを入力してください",
    password_confirm: "確認用パスワードを入力してください",
};

$("#register_btn").on("click",function(){   
    console.log("check");
    
    $(".error").remove();
    const email = $("input[name='email']").val();
    const password = $("input[name='password']").val();
    const password_confirm = $("input[name='password_confirm']").val();
    
    // email check
    if(email === ""){
        $("input[name='email']").after(`<div class="error" style="color: red;">${errorMes.email}</div>`);
       
    }
    
    // password check
    if(password === ""){
        $("input[name='password']").after(`<div class="error" style="color: red;">${errorMes.password}</div>`);
       
    }
    
    // password_confirm check
    if(password_confirm === ""){
        $("input[name='password_confirm']").after(`<div class="error" style="color: red;">${errorMes.password_confirm}</div>`);
     
    }

});
