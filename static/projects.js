function sendLike(project_id) {
    var request = new XMLHttpRequest();
    request.open("POST", "/like");
    request.setRequestHeader("Content-Type", "application/json");
    let user_id = 1
    let data = {'user_id': user_id, 'project_id': parseInt(project_id)}
    request.send(JSON.stringify(data));

}