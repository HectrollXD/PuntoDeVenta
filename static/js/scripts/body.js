$(document).ready(main)



function main(){
    $('#id_modal_messages').modal('show');
    $('#id_btn_submit').on('click', function(){
        $('input[required]').addClass('input-required');
    });
    $('#id_profile_image_name').change(function(){
        $('#profile_image_settings').attr('src', window.URL.createObjectURL(this.files[0]))
    })
}