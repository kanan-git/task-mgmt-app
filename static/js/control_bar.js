function CustomOnLoadEvent() {
    var created_img = document.createElement('img')
    created_img.src = "static/img/icons/magnifier-svgrepo-com.svg"
    created_img.alt = 'search'
    created_img.style.width = '30px'
    created_img.style.height = '30px'
    var search_button = document.getElementById('search_btn')
    search_button.parentNode.replaceChild(created_img, search_button)
}
CustomOnLoadEvent()


function ToggleFilterPanel() {
    current_style_value = document.getElementById('filter_panel').style.display
    if(current_style_value == `block`) {
        document.getElementById('filter_panel').style.display = `none`
        document.getElementById('filter_panel').style.visibility = `hidden`
        document.getElementById('filter_panel').style.opacity = `0%`
    }
    else if(current_style_value == `none`) {
        document.getElementById('filter_panel').style.display = `block`
        document.getElementById('filter_panel').style.visibility = `visible`
        document.getElementById('filter_panel').style.opacity = `100%`
    }
}


function SearchForTasks() {
    var search_input = document.getElementById('search_input')
    var search_btn = document.getElementById('search_btn')
}


function SortDirection() {
    var sort_direct_img = document.getElementById('sort_direct_ico')
    console.log(sort_direct_img.src)
    if(sort_direct_img.src == 'http://127.0.0.1:8000/static/img/icons/sort-from-bottom-to-top-svgrepo-com.svg') {
        document.getElementById('sort_direct_ico').src = 'http://127.0.0.1:8000/static/img/icons/sort-from-top-to-bottom-svgrepo-com.svg'
    }
    else if(sort_direct_img.src == 'http://127.0.0.1:8000/static/img/icons/sort-from-top-to-bottom-svgrepo-com.svg') {
        document.getElementById('sort_direct_ico').src = 'http://127.0.0.1:8000/static/img/icons/sort-from-bottom-to-top-svgrepo-com.svg'
    }
}


function SortTasksBy() {
    var sort_select = document.getElementById('sort_by')
}


function SelectView() {
    var view_img = document.getElementById('select_view_ico')
    var sort_direct_img = document.getElementById('sort_direct_ico')
    console.log(sort_direct_img.src)
    if(view_img.src == 'http://127.0.0.1:8000/static/img/icons/grid-view-svgrepo-com.svg') {
        document.getElementById('select_view_ico').src = 'http://127.0.0.1:8000/static/img/icons/view-list-bullet-rtl-svgrepo-com.svg'
    }
    else if(view_img.src == 'http://127.0.0.1:8000/static/img/icons/view-list-bullet-rtl-svgrepo-com.svg') {
        document.getElementById('select_view_ico').src = 'http://127.0.0.1:8000/static/img/icons/grid-view-svgrepo-com.svg'
    }
}
