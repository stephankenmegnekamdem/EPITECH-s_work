<?php

require("task02.php");
function dynamic_body(){
    $html = "<p>Unknown page</p>";
    if (isset($_GET['page'])){
        return render_body($_GET['page']);
    }
    else{
        return $html;
    }
}