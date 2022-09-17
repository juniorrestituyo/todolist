let baseUrl = window.location.href

let todoListItem = document.querySelectorAll('.todo-list')
for (let i = 0; todoListItem.length > i; i++){
    todoListItem[i].addEventListener("change", function() {
        if(this.checked){
            window.location = baseUrl + "check/" + todoListItem[i].dataset.id
        }else{
            window.location = baseUrl + "uncheck/" + todoListItem[i].dataset.id
        }
    })
}
