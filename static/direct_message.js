// Socket for new messages
var message_socket = io('/message');
message_socket.on('connect', function () {
    message_socket.send('connected');
});


message_socket.on('update', function (data) {
    text = document.querySelector('#dm-card-body');
    text.innerHTML += ' <p class="sender"><strong>' + data.first_name + ': </strong> ' + data.message + '</p>';
});

function sendMessage(receiver) {
    message = document.getElementById('message_area').value;
    let data = {'receiver': parseInt(receiver), 'message': message };
    message_socket.emit('message', data);
}