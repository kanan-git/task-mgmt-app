function CustomOnLoadEvent() {
    //===== START UP SEARCH INPUT DATA =====//
    const searchParamData = new URL(window.location.href).searchParams.get('search')
    if(searchParamData) {
        document.getElementById('search_input').value = searchParamData
    }

    //===== START UP SEARCH BUTTON ICON =====//
    // var created_img = document.createElement('img')
    // created_img.src = "static/img/icons/magnifier-svgrepo-com.svg"
    // created_img.alt = 'search'
    // created_img.style.width = '30px'
    // created_img.style.height = '30px'
    // created_img.style.cursor = `pointer`
    // var search_button = document.getElementById('search_btn')
    // search_button.parentNode.replaceChild(created_img, search_button)

    //===== START UP SORT DIRECTION ICON =====//
    if(new URL(window.location.href).searchParams.get('direction') == 'ascending') {
        document.getElementById('sort_direct_ico').src = 'http://127.0.0.1:8000/static/img/icons/sort-from-top-to-bottom-svgrepo-com.svg'
    } else if(new URL(window.location.href).searchParams.get('direction') == 'descending') {
        document.getElementById('sort_direct_ico').src = 'http://127.0.0.1:8000/static/img/icons/sort-from-bottom-to-top-svgrepo-com.svg'
    } else {
        document.getElementById('sort_direct_ico').src = 'http://127.0.0.1:8000/static/img/icons/sort-from-top-to-bottom-svgrepo-com.svg'
    }

    //===== START UP VIEW MODES ICON =====//
    if(new URL(window.location.href).searchParams.get('view') == 'grid') {
        document.getElementById('select_view_ico').src = 'http://127.0.0.1:8000/static/img/icons/grid-view-svgrepo-com.svg'
    } else if(new URL(window.location.href).searchParams.get('view') == 'list') {
        document.getElementById('select_view_ico').src = 'http://127.0.0.1:8000/static/img/icons/view-list-bullet-rtl-svgrepo-com.svg'
    } else {
        document.getElementById('select_view_ico').src = 'http://127.0.0.1:8000/static/img/icons/grid-view-svgrepo-com.svg'
    }

    //===== START UP SORT BY VALUE =====//
    var sortByParam = new URL(window.location.href).searchParams.get('sortby')
    if(sortByParam) {
        document.getElementById('sort_by').value = sortByParam
    }
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
    var search_input_value = document.getElementById('search_input').value
    var current_url = new URL(window.location.href)
    current_url.searchParams.set('search', search_input_value)
    window.history.pushState({}, '', current_url)
    window.relaod()
}


function SortDirection() {
    // var sort_direct_img = document.getElementById('sort_direct_ico')
    const current_url = new URL(window.location.href)
    // const sortDirection = current_url.searchParams.get('direction')

    if(current_url.searchParams.get('direction') == null) {
        current_url.searchParams.set('direction', 'descending')
    } else if(current_url.searchParams.get('direction') == 'ascending') {
        current_url.searchParams.set('direction', 'descending')
    } else if(current_url.searchParams.get('direction') == 'descending') {
        current_url.searchParams.set('direction', 'ascending')
    } else {
        // handle possible error scenario
    }
    
    window.history.pushState({}, '', current_url)
    window.location.reload()
}


function SortTasksBy() {
    var sort_select_data = document.getElementById('sort_by').value
    const current_url = new URL(window.location.href)
    current_url.searchParams.set('sortby', sort_select_data)
    // document.getElementById('sort_by').value = sort_select_data
    // FIX THE PROBLEM ABOUT, WHEN PAGE RELOADS, SELECT OPTION CLAIMS DEFAULT, FIRST OPTION AS VALUE SO SORT BY URL DOESNT WORK!
    // https://www.w3schools.com/django/django_queryset_filter.php
    window.history.pushState({}, '', current_url)
    window.location.reload()
}


function SelectView() {
    const current_url = new URL(window.location.href)
    if(current_url.searchParams.get('view') == null) {
        current_url.searchParams.set('view', 'list')
    } else if(current_url.searchParams.get('view') == 'grid') {
        current_url.searchParams.set('view', 'list')
    } else if(current_url.searchParams.get('view') == 'list') {
        current_url.searchParams.set('view', 'grid')
    }
    window.history.pushState({}, '', current_url)
    window.location.reload()
}
