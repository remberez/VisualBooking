import axios from 'axios'

axios.get('https://fortnite-api.com/v1/banners').then(response => {
    alert(response.data + "- данные")
  })
  .catch(error => {
    alert("error");
  })