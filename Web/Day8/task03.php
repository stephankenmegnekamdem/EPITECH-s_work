<?php
function get_shortest(array $arr)
{
    if(count($arr)>=1){
        $min = strlen($arr[0]);
        $str = $arr[0];
        foreach ($arr as $item) {
            if (strlen($item) < $min) {
                $min = strlen($item);
                $str = $item;
            }
        }
        return $str;
    }

}
?>