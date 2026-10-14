<?php
function calc_average(array $numbers){
    $average = array_sum($numbers) / count($numbers);
    return round($average, 1);
}
?>