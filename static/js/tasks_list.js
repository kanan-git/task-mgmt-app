function HomePageOnLoad() {
    const pageNumber = new URL(window.location.href).searchParams.get('page')
    if(pageNumber == null) {
        document.getElementById('home_pg_btn_1').classList.add('active')
    } else {
        document.getElementById(`home_pg_btn_${pageNumber}`).classList.add('active')
    }
}
HomePageOnLoad()


function paginationHome(e) {
    const currentURL = new URL(window.location.href)
    var currentPgNum = currentURL.searchParams.get('page')
    const currentPageNumber = e.name

    currentURL.searchParams.set('page', currentPageNumber)
    window.history.pushState({}, '', currentURL)
    window.reload()
}
