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


function change_language(active_option, selection) {
    language_btn = document.getElementById('select_language')

    option_en = document.getElementById('lang_en')
    option_az = document.getElementById('lang_az')
    option_tr = document.getElementById('lang_tr')
    option_ru = document.getElementById('lang_ru')

    if(selection == 1) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        option_az.style.backgroundColor = `rgb(255,255,255)`
        option_tr.style.backgroundColor = `rgb(255,255,255)`
        option_ru.style.backgroundColor = `rgb(255,255,255)`
        language_btn.innerHTML = 'EN'
    } else if(selection == 2) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        option_en.style.backgroundColor = `rgb(255,255,255)`
        option_tr.style.backgroundColor = `rgb(255,255,255)`
        option_ru.style.backgroundColor = `rgb(255,255,255)`
        language_btn.innerHTML = 'AZ'
    } else if(selection == 3) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        option_en.style.backgroundColor = `rgb(255,255,255)`
        option_az.style.backgroundColor = `rgb(255,255,255)`
        option_ru.style.backgroundColor = `rgb(255,255,255)`
        language_btn.innerHTML = 'TR'
    } else if(selection == 4) {
        active_option.style.backgroundColor = `rgb(128,128,128)`
        option_en.style.backgroundColor = `rgb(255,255,255)`
        option_az.style.backgroundColor = `rgb(255,255,255)`
        option_tr.style.backgroundColor = `rgb(255,255,255)`
        language_btn.innerHTML = 'RU'
    }
}
