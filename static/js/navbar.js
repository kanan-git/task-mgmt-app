function NavbarCustomOnLoadEvent() {
    //===== START UP SET LANGUAGE DATA FROM LOCALSTORAGE =====//
    var local_lang_data = new URL(window.location.href).searchParams.get('lang')
    var portname = window.location.port
    if(local_lang_data == null) {local_lang_data = 'english'}
    var option_en = document.getElementById('lang_en')
    var option_az = document.getElementById('lang_az')
    var option_tr = document.getElementById('lang_tr')
    var option_ru = document.getElementById('lang_ru')
    var option_en_text = document.getElementById('lang_en_text')
    var option_az_text = document.getElementById('lang_az_text')
    var option_tr_text = document.getElementById('lang_tr_text')
    var option_ru_text = document.getElementById('lang_ru_text')
    option_en.style.backgroundColor = `rgb(255,255,255)`
    option_en_text.style.color = `rgb(0,0,0)`
    option_az.style.backgroundColor = `rgb(255,255,255)`
    option_az_text.style.color = `rgb(0,0,0)`
    option_tr.style.backgroundColor = `rgb(255,255,255)`
    option_tr_text.style.color = `rgb(0,0,0)`
    option_ru.style.backgroundColor = `rgb(255,255,255)`
    option_ru_text.style.color = `rgb(0,0,0)`
    if(local_lang_data == 'english') {
        option_en.style.backgroundColor = `rgb(128,128,128)`
        option_en_text.style.color = `rgb(255,255,255)`
        document.getElementById('select_language').innerHTML = `<img src="http://localhost:${portname}/static/img/flags/flag-us-svgrepo-com.svg" alt="english" name="english" id="flag_en" style="width: 30px;"> <span id="screen_lang" name="english"> EN </span>`
    } else if(local_lang_data == 'azerbaijani') {
        option_az.style.backgroundColor = `rgb(128,128,128)`
        option_az_text.style.color = `rgb(255,255,255)`
        document.getElementById('select_language').innerHTML = `<img src="http://localhost:${portname}/static/img/flags/flag-az-svgrepo-com.svg" alt="azerbaijani" name="azerbaijani" id="flag_az" style="width: 30px;"> <span id="screen_lang" name="azerbaijani"> AZ </span>`
    } else if(local_lang_data == 'turkish') {
        option_tr.style.backgroundColor = `rgb(128,128,128)`
        option_tr_text.style.color = `rgb(255,255,255)`
        document.getElementById('select_language').innerHTML = `<img src="http://localhost:${portname}/static/img/flags/flag-tr-svgrepo-com.svg" alt="turkish" name="turkish" id="flag_tr" style="width: 30px;"> <span id="screen_lang" name="turkish"> TR </span>`
    } else if(local_lang_data == 'russian') {
        option_ru.style.backgroundColor = `rgb(128,128,128)`
        option_ru_text.style.color = `rgb(255,255,255)`
        document.getElementById('select_language').innerHTML = `<img src="http://localhost:${portname}/static/img/flags/flag-ru-svgrepo-com.svg" alt="russian" name="russian" id="flag_ru" style="width: 30px;"> <span id="screen_lang" name="russian"> RU </span>`
    } else {
        option_en.style.backgroundColor = `rgb(128,128,128)`
        option_en_text.style.color = `rgb(255,255,255)`
        document.getElementById('select_language').innerHTML = `<img src="http://localhost:${portname}/static/img/flags/flag-us-svgrepo-com.svg" alt="english" name="english" id="flag_en" style="width: 30px;"> <span id="screen_lang" name="english"> EN </span>`
    }
}
NavbarCustomOnLoadEvent()

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


function change_language(prop_lang) {
    const new_url = new URL(window.location.href)
    new_url.searchParams.set('lang', prop_lang)
    window.history.pushState({}, '', new_url)
    window.reload()
}


function reloadCurrentPage() {
    window.reload()
}
