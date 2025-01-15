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
    }
    else if(current_style_value == `none`) {
        document.getElementById('filter_panel').style.display = `block`
    }
}


function SearchForTasks() {
    var search_input = document.getElementById('search_input')
    var search_btn = document.getElementById('search_btn')
}


function SortDirection() {
    var sort_direct_btn = document.getElementById('sort_direction_btn')
    var sort_direct_img = document.getElementById('sort_direct_ico')
    var btn_descending_src = 'static/img/icons/sort-from-bottom-to-top-svgrepo-com.svg'
    var btn_descending_alt = 'sort_descending'
    var btn_ascending_src = 'static/img/icons/sort-from-top-to-bottom-svgrepo-com.svg'
    var btn_ascending_alt = 'sort_ascending'
}


function SortTasksBy() {
    var sort_select = document.getElementById('sort_by')
}


function SelectView() {
    var view_btn = document.getElementById('select_view')
    var view_img = document.getElementById('select_view_ico')
}
