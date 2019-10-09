document.addEventListener('DOMContentLoaded', () => {

  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
 

  // When connected, configure buttons
  socket.on('connect', () => {

 
    // Each button should emit a "message" event
  document.querySelectorAll('button').forEach((button) => {
      button.onclick = () => {
          const send_message = "This_is_a_test_message";
          socket.emit('message', {'my_message': send_message});
      };
    });
  });

  // When a new message has been created, send out the message
  socket.on("announce_message", data => {
      const li = document.createElement('li');
      //li.innerHTML = "Test Message";
      li.innerHTML = data['my_message'];
      document.querySelector("#message_list").append(li);
  });
});