function milestone_percentage(card_id) {
    var value_start = document.getElementById(`hidden_start_tag_${card_id}`).innerText
    var value_end = document.getElementById(`hidden_end_tag_${card_id}`).innerText
    var bar = document.getElementById(`progression_bar_${card_id}`)
    var bar_status = document.getElementById(`bar_stat_${card_id}`)
    var result = (value_start/value_end)*100
    bar.style.width = `${result}%`
    if(result < 100) {
        bar_status.style.background = `linear-gradient(to right, rgba(255,255,128,1.0), rgba(255,200,50,1.0))`
    } else {
        bar_status.style.background = `radial-gradient(rgba(0,200,0,1.0), rgba(128,255,128,1.0))`
    }
    // console.log(`Card ID: ${card_id}`, '←—→', `Done: ${value_start}`, '←—→', `Total: ${value_end}`)
}
