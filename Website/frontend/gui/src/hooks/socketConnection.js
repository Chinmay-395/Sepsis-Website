import { share } from 'rxjs/operators'; // new
import { webSocket } from 'rxjs/webSocket'; // new

let _socket; // new
export let messages; 

export const connect_ws = () => {
  console.log("THE WEBSOCKET CONNECTED")
  if (!_socket || _socket.closed) {
    _socket = webSocket(`ws://localhost:8000/sepsisDynamic/?token=${localStorage.getItem('token')}`);
    messages = _socket.pipe(share());
    messages.subscribe(message => console.log("The message",message));
  }
};