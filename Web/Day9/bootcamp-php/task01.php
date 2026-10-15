<?php
function display_menu(){
   $pages = ["Home" => "home.php", "Products" => "product.php", "About Us" => "about.php", "Contact" => "contact.php"];
   $html = "<ul>\n";
        foreach($pages as $label => $link){
        $html .= '<li><a href="' . $link . '">' . $label . '</a></li>' . "\n";
        }
        $html .= "</ul>";
    return $html;
}
?>