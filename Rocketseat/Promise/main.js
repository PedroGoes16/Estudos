
axios.get('https://api.github.com/users/pedrogoes16')
    .then(function(response){
        console.log(response)
    })
    .catch(function(error){
        console.warn(error)
    })