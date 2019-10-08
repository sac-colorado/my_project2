document.addEventListener('DOMContentLoaded', () => {

  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // When connected, configure buttons
  socket.on('connect', () => {

    // Each button should emit a "submit vote" event
  document.querySelectorAll('button').forEach(button => {
      button.onclick = () => {
          const send_message = "Someone is requesting that messages be sent";
          socket.emit('message', {'my_message': send_message});
      };
    });
  });

  // When a new message announced, send out the message
  socket.on("announce_message", data => {
      const li = document.createElement('li');
      li.innerHTML = '${data.my_message}';
      document.querySelector
  })