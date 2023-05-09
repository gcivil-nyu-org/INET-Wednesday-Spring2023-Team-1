    $( function() {

      $( "#id_song1_disp" ).autocomplete({
        source: getSongList,
        select: saveTrkOnClick1,
        change: selectOnly,
      });

       $( "#id_song2_disp" ).autocomplete({
        source: getSongList,
        select: saveTrkOnClick2,
        change: selectOnly,
      });

       $( "#id_song3_disp" ).autocomplete({
        source: getSongList,
        select: saveTrkOnClick3,
        change: selectOnly,
      });
       $( "#id_song4_disp" ).autocomplete({
        source: getSongList,
        select: saveTrkOnClick4,
        change: selectOnly,
      });
       $( "#id_song5_disp" ).autocomplete({
        source: getSongList,
        select: saveTrkOnClick5,
        change: selectOnly,
      });

       $( "#id_album1_disp" ).autocomplete({
        source: getAlbumList,
        select: saveAlbOnClick1,
        change: selectOnly,
      });

      $( "#id_album2_disp" ).autocomplete({
        source: getAlbumList,
        select: saveAlbOnClick2,
        change: selectOnly,
      });

      $( "#id_album3_disp" ).autocomplete({
        source: getAlbumList,
        select: saveAlbOnClick3,
        change: selectOnly,
      });

      $( "#id_album4_disp" ).autocomplete({
        source: getAlbumList,
        select: saveAlbOnClick4,
        change: selectOnly,
      });

      $( "#id_album5_disp" ).autocomplete({
        source: getAlbumList,
        select: saveAlbOnClick5,
        change: selectOnly,
      });


      $( "#id_artist1_disp" ).autocomplete({
        source: getArtistList,
        select: saveArtOnClick1,
        change: selectOnly,
      });

      $( "#id_artist2_disp" ).autocomplete({
        source: getArtistList,
        select: saveArtOnClick2,
        change: selectOnly,
      });

      $( "#id_artist3_disp" ).autocomplete({
        source: getArtistList,
        select: saveArtOnClick3,
        change: selectOnly,
      });

      $( "#id_artist4_disp" ).autocomplete({
        source: getArtistList,
        select: saveArtOnClick4,
        change: selectOnly,
      });

      $( "#id_artist5_disp" ).autocomplete({
        source: getArtistList,
        select: saveArtOnClick5,
        change: selectOnly,
      });


      $( "#id_genre1" ).autocomplete({
        source: getGenreList,
      });

      $( "#id_genre2" ).autocomplete({
        source: getGenreList,
      });

      $( "#id_genre3" ).autocomplete({
        source: getGenreList,
      });

      $( "#id_genre4" ).autocomplete({
        source: getGenreList,
      });

      $( "#id_genre5" ).autocomplete({
        source: getGenreList,
      });

      $( "#id_response1" ).autocomplete({
        source: getSongList,
        select: saveResponseOnClick1,
        change: selectOnly,
      });

       $( "#id_response2" ).autocomplete({
        source: getSongList,
        select: saveResponseOnClick2,
        change: selectOnly,
      });

       $( "#id_response3" ).autocomplete({
        source: getSongList,
        select: saveResponseOnClick3,
        change: selectOnly,
      });
       $( "#id_response4" ).autocomplete({
        source: getSongList,
        select: saveResponseOnClick4,
        change: selectOnly,
      });
       $( "#id_response5" ).autocomplete({
        source: getSongList,
        select: saveResponseOnClick5,
        change: selectOnly,
      });

      accessToken = auths;
      function selectOnly(event, ui) { if (!ui.item) { $(this).val(''); } };
      function getSongList(request, response) {
        var songSearch = request.term;
        var songList = [];
        $.ajax({
          url: "https://api.spotify.com/v1/search?q=" + songSearch + "&type=track&limit=25",
          method: "GET",
          dataType: "json",
          headers: {
              "Authorization" : " Bearer " + accessToken
          },
          success: function(data) {
              var artistData;
              var songStr;
              var songID;
              var ary = data.tracks.items;
              for (track in ary) {
                  songStr = ary[track].name + " - ";
                  artistData = ary[track].artists;
                  for (artist in artistData) {
                      songStr = songStr + artistData[artist].name + ", ";
                  }
                  songID = ary[track].id;
                  songList.push({label: songStr.slice(0,-2), value: songID});
              }
              response(songList);
          },
        })
      };
      function saveTrkOnClick1(event, ui) {
          event.preventDefault();
          $("#id_song1_id").val(ui.item.value);
          $("#id_song1_name_artist").val(ui.item.label);
          $("#id_song1_disp").val(ui.item.label);

      };
      function saveTrkOnClick2(event, ui) {
          event.preventDefault();
          $("#id_song2_id").val(ui.item.value);
          $("#id_song2_name_artist").val(ui.item.label);
          $("#id_song2_disp").val(ui.item.label);

      };
      function saveTrkOnClick3(event, ui) {
          event.preventDefault();
          $("#id_song3_id").val(ui.item.value);
          $("#id_song3_name_artist").val(ui.item.label);
          $("#id_song3_disp").val(ui.item.label);

      };
      function saveTrkOnClick4(event, ui) {
          event.preventDefault();
          $("#id_song4_id").val(ui.item.value);
          $("#id_song4_name_artist").val(ui.item.label);
          $("#id_song4_disp").val(ui.item.label);

      };
      function saveTrkOnClick5(event, ui) {
          event.preventDefault();
          $("#id_song5_id").val(ui.item.value);
          $("#id_song5_name_artist").val(ui.item.label);
          $("#id_song5_disp").val(ui.item.label);

      };

      function getAlbumList(request, response) {
        var albumSearch = request.term;
        var albumList = [];
        $.ajax({
          url: "https://api.spotify.com/v1/search?q=" + albumSearch + "&type=album&limit=25",
          method: "GET",
          dataType: "json",
          headers: {
              "Authorization" : " Bearer " + accessToken
          },
          success: function(data) {
              var artistData;
              var albumStr;
              var albumID;
              var ary = data.albums.items;
              for (album in ary) {
                  albumStr = ary[album].name + " - ";
                  artistData = ary[album].artists;
                  for (artist in artistData) {
                      albumStr = albumStr + artistData[artist].name + ", ";
                  }
                  albumID = ary[album].id;
                  albumList.push({label: albumStr.slice(0,-2), value: albumID});
              }
              response(albumList);
          },
        })
      };
      function saveAlbOnClick1(event, ui) {
        event.preventDefault();
        $("#id_album1_id").val(ui.item.value);
        $("#id_album1_name_artist").val(ui.item.label);
        $("#id_album1_disp").val(ui.item.label);

      };
      function saveAlbOnClick2(event, ui) {
        event.preventDefault();
        $("#id_album2_id").val(ui.item.value);
        $("#id_album2_name_artist").val(ui.item.label);
        $("#id_album2_disp").val(ui.item.label);

      };
      function saveAlbOnClick3(event, ui) {
        event.preventDefault();
        $("#id_album3_id").val(ui.item.value);
        $("#id_album3_name_artist").val(ui.item.label);
        $("#id_album3_disp").val(ui.item.label);

      };
      function saveAlbOnClick4(event, ui) {
        event.preventDefault();
        $("#id_album4_id").val(ui.item.value);
        $("#id_album4_name_artist").val(ui.item.label);
        $("#id_album4_disp").val(ui.item.label);

      };
      function saveAlbOnClick5(event, ui) {
        event.preventDefault();
        $("#id_album5_id").val(ui.item.value);
        $("#id_album5_name_artist").val(ui.item.label);
        $("#id_album5_disp").val(ui.item.label);

      };

      function getArtistList(request, response) {
        var artistSearch = request.term;
        var artistList = [];
        $.ajax({
          url: "https://api.spotify.com/v1/search?q=" + artistSearch + "&type=artist&limit=25",
          method: "GET",
          dataType: "json",
          headers: {
              "Authorization" : " Bearer " + accessToken
          },
          success: function(data) {
              var ary = data.artists.items;
              for (artist in ary) {
                  songID = ary[artist].id;
                  artistList.push({label: ary[artist].name, value: ary[artist].id});
              }
              response(artistList);
          },
        })
      };
      function saveArtOnClick1(event, ui) {
        event.preventDefault();
        $("#id_artist1_id").val(ui.item.value);
        $("#id_artist1_name").val(ui.item.label);
        $("#id_artist1_disp").val(ui.item.label);

      };
      function saveArtOnClick2(event, ui) {
        event.preventDefault();
        $("#id_artist2_id").val(ui.item.value);
        $("#id_artist2_name").val(ui.item.label);
        $("#id_artist2_disp").val(ui.item.label);

      };
      function saveArtOnClick3(event, ui) {
        event.preventDefault();
        $("#id_artist3_id").val(ui.item.value);
        $("#id_artist3_name").val(ui.item.label);
        $("#id_artist3_disp").val(ui.item.label);

      };
      function saveArtOnClick4(event, ui) {
        event.preventDefault();
        $("#id_artist4_id").val(ui.item.value);
        $("#id_artist4_name").val(ui.item.label);
        $("#id_artist4_disp").val(ui.item.label);

      };
      function saveArtOnClick5(event, ui) {
        event.preventDefault();
        $("#id_artist5_id").val(ui.item.value);
        $("#id_artist5_name").val(ui.item.label);
        $("#id_artist5_disp").val(ui.item.label);

      };

      function saveResponseOnClick1(event, ui) {
        event.preventDefault();
        $("#id_response1").val(ui.item.label);
        $("#id_response1_id").val(ui.item.value);

      };

      function saveResponseOnClick2(event, ui) {
        event.preventDefault();
        $("#id_response2").val(ui.item.label);
        $("#id_response2_id").val(ui.item.value);

      };
      function saveResponseOnClick3(event, ui) {
        event.preventDefault();
        $("#id_response3").val(ui.item.label);
        $("#id_response3_id").val(ui.item.value);

      };
      function saveResponseOnClick4(event, ui) {
        event.preventDefault();
        $("#id_response4").val(ui.item.label);
        $("#id_response4_id").val(ui.item.value);

      };
      function saveResponseOnClick5(event, ui) {
        event.preventDefault();
        $("#id_response5").val(ui.item.label);
        $("#id_response5_id").val(ui.item.value);
      };

      });