<?php
function dog_bark(int $woof_nb){
    if ($woof_nb >= 1){
        for($i = 1; $i <= $woof_nb; $i++){
            echo("woof ");
        }
    }
    echo("\n");
}
?>