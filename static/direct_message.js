// Socket for new messages
var message_socket = io('/message');
message_socket.on('connect', function () {
    message_socket.send('connected');
});


message_socket.on('update', function (data) {
    text = document.querySelector('#dm-card-body');
    text.innerHTML += ' <p class="sender"><strong>' + data.first_name + ': </strong> ' + data.message + '</p>';
});

function sendMessage(sender, receiver, message) {
    let data = {'sender': parseInt(sender), 'receiver': parseInt(receiver), 'message': message };
    message_socket.emit('message', data);
}

// Socket for new chats
var chat_socket = io('/chat');
chat_socket.on('connect', function () {
    chat_socket.send('connected');
});


message_socket.on('update', function (data) {
    text = document.querySelector('#chat-list');
    text.innerHTML += '<button type="button" class="btn btn-secondary" id="' + data.id + '">' + data.first_name + ' ' + data.last_name + '</button>';
});


