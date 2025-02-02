async function fetch_from_own_api() {
    const url = 'http://127.0.0.1:8000/api'
    
    try {
        const response = await fetch(url)
        if(!response.ok) {
            throw new Error(`Response status: ${response.status}`)
        }
        const json = await response.json()
        // console.log(json.data)

        var taskList = document.getElementById('container')

        var number_of_element = 1
        for(var i=0; i<json.data.length; i++) {
            // console.log(json.data[i])
            const listItem = document.createElement('li')
            const currentTask = json.data[i]
            listItem.textContent = `#(${number_of_element})# • ID:${currentTask.id} → Categories: ${currentTask.category_of_task} | Task: ${currentTask.todo} | Priority Level: ${currentTask.priority_level} | Status: ${currentTask.todo_status}`
            taskList.appendChild(listItem)
            number_of_element++
        }
    } catch(error) {
        console.log(error.message)
    }

    // fetch(url)
    // .then(response => {
    //     if(!response.ok) {
    //         throw new Error('Network response was not ok')
    //     }
    //     return response.json()
    // })
    // .then(data => {
    //     const taskList = document.getElementById('container')
    //     data.forEach(task => {
    //         const listItem = document.createElement('li')
    //         listItem.textContent = `Task: ${task.todo}, Status: ${task.todo_status}`
    //         taskList.appendChild(listItem)
    //     })
    // })
    // .catch(error => {
    //     console.log('There was a problem with the fetch operation: ', error)
    // })

    // const myHeaders = new Headers();
    // myHeaders.append("Content-Type", "application/json");
    
    // const response = await fetch("https://example.org/post", {
    //   method: "POST",
    //   body: JSON.stringify({ username: "example" }),
    //   headers: myHeaders,
    // });

    // fetch('https://api.example.com/data')  // The URL you want to fetch from
    // .then(response => {
    //     if (!response.ok) {
    //     throw new Error('Network response was not ok');
    //     }
    //     return response.json();  // Parse the JSON data from the response
    // })
    // .then(data => {
    //     console.log(data);  // Handle the data you get back
    // })
    // .catch(error => {
    //     console.error('There was a problem with the fetch operation:', error);
    // });
}

fetch_from_own_api()
