function fetch_from_own_api() {
    var url = 'http://127.0.0.1:8000/api'

    fetch(url)
    .then(response => {
        if(!response.ok) {
            throw new Error('Network response was not ok')
        }
        return response.json()
    })
    .then(data => {
        const taskList = document.getElementById('container')
        data.forEach(task => {
            const listItem = document.createElement('li')
            listItem.textContent = `Task: ${task.todo}, Status: ${task.todo_status}`
            taskList.appendChild(listItem)
        })
    })
    .catch(error => {
        console.log('There was a problem with the fetch operation: ', error)
    })
}

fetch_from_own_api()
