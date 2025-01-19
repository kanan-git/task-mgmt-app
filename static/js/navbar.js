function profile_dropdown_show() {
    dropdown_menu = document.getElementById('profile_dropdown')
    dropdown_menu.style.display = `block`
}


function profile_dropdown_hide() {
    dropdown_menu = document.getElementById('profile_dropdown')
    dropdown_menu.style.display = `none`
}


function language_dropdown_show() {
    language_menu = document.getElementById('lang_dropdown')
    language_menu.style.display = `block`
}


function language_dropdown_hide() {
    language_menu = document.getElementById('lang_dropdown')
    language_menu.style.display = `none`
}


function elements_move(e) {
    e.style.marginLeft = `10px`
    e.style.color = `rgb(255,255,255)`
    e.style.filter = `drop-shadow(0px 0px 2px rgb(0,0,0))`
}


function elements_back(e) {
    e.style.marginLeft = `0px`
    e.style.color = `rgb(0,0,0)`
    e.style.filter = `drop-shadow(0px 0px 0px rgb(255,255,255))`
}


function change_language(active_option, selection) {
    language_btn = document.getElementById('select_language')

    option_en = document.getElementById('lang_en')
    option_az = document.getElementById('lang_az')
    option_tr = document.getElementById('lang_tr')
    option_ru = document.getElementById('lang_ru')

    if(selection == 1) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        active_option.style.color = `rgb(255,255,255)`
        option_az.style.backgroundColor = `rgb(255,255,255)`
        option_az.style.color = `rgb(0,0,0)`
        option_tr.style.backgroundColor = `rgb(255,255,255)`
        option_tr.style.color = `rgb(0,0,0)`
        option_ru.style.backgroundColor = `rgb(255,255,255)`
        option_ru.style.color = `rgb(0,0,0)`
        language_btn.innerHTML = '<img src="static/img/flags/flag-us-svgrepo-com.svg" alt="flag_en" style="width: 30px;"> EN'
    } else if(selection == 2) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        active_option.style.color = `rgb(255,255,255)`
        option_en.style.backgroundColor = `rgb(255,255,255)`
        option_en.style.color = `rgb(0,0,0)`
        option_tr.style.backgroundColor = `rgb(255,255,255)`
        option_tr.style.color = `rgb(0,0,0)`
        option_ru.style.backgroundColor = `rgb(255,255,255)`
        option_ru.style.color = `rgb(0,0,0)`
        language_btn.innerHTML = '<img src="static/img/flags/flag-az-svgrepo-com.svg" alt="flag_az" style="width: 30px;"> AZ'
    } else if(selection == 3) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        active_option.style.color = `rgb(255,255,255)`
        option_en.style.backgroundColor = `rgb(255,255,255)`
        option_en.style.color = `rgb(0,0,0)`
        option_az.style.backgroundColor = `rgb(255,255,255)`
        option_az.style.color = `rgb(0,0,0)`
        option_ru.style.backgroundColor = `rgb(255,255,255)`
        option_ru.style.color = `rgb(0,0,0)`
        language_btn.innerHTML = '<img src="static/img/flags/flag-tr-svgrepo-com.svg" alt="flag_tr" style="width: 30px;"> TR'
    } else if(selection == 4) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        active_option.style.color = `rgb(255,255,255)`
        option_en.style.backgroundColor = `rgb(255,255,255)`
        option_en.style.color = `rgb(0,0,0)`
        option_az.style.backgroundColor = `rgb(255,255,255)`
        option_az.style.color = `rgb(0,0,0)`
        option_tr.style.backgroundColor = `rgb(255,255,255)`
        option_tr.style.color = `rgb(0,0,0)`
        language_btn.innerHTML = '<img src="static/img/flags/flag-ru-svgrepo-com.svg" alt="flag_ru" style="width: 30px;"> RU'
    }
}
