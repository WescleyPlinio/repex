$(document).ready(function(){
    $(".toggle-professor").change(function(){
        let checkbox = $(this);
        let form = checkbox.closest("form");
        let url = form.data("url");
        let csrf_token = form.find("input[name='csrfmiddlewaretoken']").val();
        let is_checked = checkbox.is(":checked");

        $.ajax({
            url: url,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrf_token,
                is_professor: is_checked ? "on" : ""
            },
            success: function(){ console.log("Professor toggle atualizado!"); },
            error: function(){
                alert("Erro ao atualizar toggle.");
                checkbox.prop("checked", !is_checked);
            }
        });
    });

    $(".toggle-superuser").change(function(){
        let checkbox = $(this);
        let form = checkbox.closest("form");
        let url = form.data("url");
        let csrf_token = form.find("input[name='csrfmiddlewaretoken']").val();
        let is_checked = checkbox.is(":checked");

        $.ajax({
            url: url,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrf_token,
                is_superuser: is_checked ? "on" : ""
            },
            success: function(){ console.log("Superusuário toggle atualizado!"); },
            error: function(){
                alert("Erro ao atualizar toggle.");
                checkbox.prop("checked", !is_checked);
            }
        });
    });
});
