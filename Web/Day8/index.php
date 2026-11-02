<?php
    require("task01.php");
    discover_type(21, "Maria", 3.53, true);
    echo("\n");
    require("task02.php");
    dog_bark(1);
    dog_bark(-42);
    dog_bark(3);
    echo("\n");
    require("task03.php");
    var_dump(get_shortest(array("Time", "flowing", "like", "a", "river")));
    var_dump(get_shortest(array("chou", "be", "do")));
    echo("\n");
    require("task04.php");
    var_dump(calc("*", 7, 6));
    var_dump(calc("/", 4, 3));
    var_dump(calc("+/", 4, 2));
    var_dump(calc("/", 4, 0));
    echo("\n");
    require("task05.php");
    var_dump(calc_average(array(1, 4, 28, 12, 3, 4, 4, 27)));
    echo("\n");
    require("task06.php");
    echo "Sequence 0:" . PHP_EOL;
        sequence(0);
    echo "Sequence 3:" . PHP_EOL;
        sequence(10);

?>