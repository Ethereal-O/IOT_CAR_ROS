import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

window.onerror = handleError
function handleError(msg, url, l) {
  var txt = "There was an error on this page. Please contact to administrators.\n\n"
  txt += "Error: " + msg + "\n\n"
  txt += "URL: " + url + "\n\n"
  txt += "Line: " + l + "\n\n"
  txt += "Click OK to continue.\n\n"
  alert(txt)
  return true
}