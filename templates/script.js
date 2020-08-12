NUM_COLORS = 8;
NUM_ROUNDS = 2;

window.onload = () => {
    round = 1;
    $('.block').click( function() {
        console.log($(this).attr('num'));
        $(this).addClass('hide');
        $('#result')[0].value += $(this).attr('num');
        if ($(`.color_set[num=${round}] .block.hide`).length == NUM_COLORS) {
            change();
        }
    } );
}

function change() {
    if (round >= NUM_ROUNDS) {
        end();
    }
    else {
        $(`.color_set[num=${round}]`).addClass('hide');
        round += 1;
        $(`.color_set[num=${round}]`).removeClass('hide');
        $('#result')[0].value += '\r\n';
    }
}

function end() {
    $('#result').removeClass('hide');
}

//TODO: Site may lay down. So... We need to think about it.