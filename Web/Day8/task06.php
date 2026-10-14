<?php
function sequence(int $n): void
{
    if ($n < 0) {
        return;
    }

    $sequence = "1";

    for ($j = 0; $j < $n; $j++) {
        echo $sequence . PHP_EOL;
        $temp = "";
        $len = strlen($sequence);
        $i = 0;

        while ($i < $len) {
            $digit = $sequence[$i];
            $count = 0;

            while ($i < $len && $sequence[$i] == $digit) {
                $count++;
                $i++;
            }

            $temp = $temp . $count . $digit;
        }

        $sequence = $temp;

    }
    echo $sequence . PHP_EOL;

}
?>