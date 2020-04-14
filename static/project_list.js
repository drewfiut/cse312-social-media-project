// Socket for likes
var likes_socket = io('/likes');
likes_socket.on('connect', function () {
    likes_socket.send('connected');
});

likes_socket.on('update', function (data) {
    text = document.querySelector('#like_count_' + data.project_id);
    text.textContent = data.likes;
});

function sendLike(project_id) {
    let user_id = 1;
    let data = { 'user_id': user_id, 'project_id': parseInt(project_id) };
    likes_socket.emit('like', data);
}
// Socket for new Posts
var posts_socket = io('/posts');
posts_socket.on('connect', function () {
    posts_socket.send('connected');
});

posts_socket.on('update', function (data) {
    text = document.querySelector('#new-post');
    text.innerHTML += `<div class="project_deck container">

        <div class="card mb-3 project_card">
            <div class="row">
                <div class="col-sm-1 align-self-center">
                    <button type="button" class="like_btn btn px-3"
                        onclick="sendLike('` + data.id + `'); return false;"><i class="fas fa-fire-alt"></i><span
                            id="like_count_` + data.id + `">0</span></button>
                </div>
                <div class="col-sm-4  align-self-center">
                    <img src="data:;base64,` + data.image + `" class="card-img" alt="...">
</div>
                    <div class="col-sm">
                        <div class="card-body">
                            <h5 class="card-title pink">` + data.title + `</h5>
                            <p class="card-text" id="descroption">` + data.description + `</p>
                            <p class="card-text" id="skills"><strong>Type: </strong>` + data.type + `</p>
                            <p class="card-text" id=""><i class="fas fa-users"></i> ` + data.count + ` collaborators needed
        </p>
                            <a href="/project/` + data.id + `"
                                class="btn my-2 my-sm-0 nav_button_primary btn-lg" type="button">View Project</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>`;
});