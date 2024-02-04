```
q8
```
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    document.getElementById('hello').innerText = data.hello;
  })
  .catch(error => {
    console.log('An error occurred:', error);
  });