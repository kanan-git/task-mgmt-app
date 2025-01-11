function CustomOnLoadEvent() {
    var created_img = document.createElement('img')
    // created_img.src = "{% static 'img/magnifier-svgrepo-com.svg' %}"
    created_img.src = "static/img/magnifier-svgrepo-com.svg"
    created_img.alt = 'search'
    created_img.style.width = '30px'
    created_img.style.height = '30px'
    var search_button = document.getElementById('search_btn')
    search_button.parentNode.replaceChild(created_img, search_button)
    // console.log("JavaScript file is loading")
}

CustomOnLoadEvent()
