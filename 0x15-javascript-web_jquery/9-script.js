// Queries an API for wind speed in SF and replaces the text of the
// div#sf_wind_speed tag with the speed
/**
 * script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
 * and displays the value of hello from that fetch in the HTML tag DIV#hello
 */
$(document).ready(() => {
    $.ajax({
        url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
        success: result => {
            $('DIV#hello').text(result.hello);
        }
    });
});
