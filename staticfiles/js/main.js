let todoListItem = document.querySelectorAll('.todo-list')
for (let i = 0; todoListItem.length > i; i++){
    todoListItem[i].addEventListener("change", function() {
        if(this.checked){
            window.location = "http://127.0.0.1:8000/check/" + todoListItem[i].dataset.id
        }else{
            window.location = "http://127.0.0.1:8000/uncheck/" + todoListItem[i].dataset.id
        }
    })
}
