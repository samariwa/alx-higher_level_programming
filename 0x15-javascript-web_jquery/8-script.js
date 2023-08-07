$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){
    $('UL#list_movies').html(data);
    data.results.forEach(result => {
        $('UL#list_movies').append(`<li>${result.title}</li>`);
    });
});
