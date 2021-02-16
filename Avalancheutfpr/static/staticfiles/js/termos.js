(function(){
    'use strict';

    var $btn = document.getElementById('btn_cadastro');
    var $chk = document.getElementById('chk');
    toggleBtn();

    $chk.addEventListener('change', function(){
        toggleBtn();
    });

    function toggleBtn(){
        $btn.disabled = !$chk.checked;
    }
})()