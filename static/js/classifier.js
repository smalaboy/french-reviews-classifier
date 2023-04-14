$(
    function () {
        // Le loader et les résultats sont initialement cachés
        $("#loader").hide();
        $("#results").hide();

        /**
         * Soumettre le formulaire avec ajax et afficher les résultats
         */
        $("#classifier-form").on('submit', function (evt) {
           evt.preventDefault();
           // Afficher le loader
           $("#loader").show();
           $("#results").hide();
           $.ajax(
               {
                   'url': '/api/classify',
                   'method': 'GET',
                   'data': $(this).serialize()
               }
           ).done(function (response) {
               // Afficher les résultats
               $("#loader").hide();
               $("#results").show();

               $("#results #prediction").text(response.prediction);
               $("#results #probability").text(response.probability + "%");
           });
        });

        /**
         * Effacer les résultats en cas de changement du texte pour éviter un affichage incohérent
         */
        $("#classifier-form").on('change', function (evt) {
            $("#results #prediction").text('-');
            $("#results #probability").text('-');
        });
    }
);
