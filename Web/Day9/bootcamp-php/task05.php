<?php
function form_is_submitted() {
    return isset($_POST['submit']);
}

function whoami(){
        $curricula=["pge" => "PGE (Programme Grande Ecole)", "bachelor" => "Bachelor", "msc" => "MSc Pro", "coding" => "Coding Academy", "wac" => "Web@cademie" ];
         if (isset($_POST['curriculum']) && isset($curricula[$_POST['curriculum']])) {
             $curriculum = $curricula[$_POST['curriculum']];
         }
        if (isset($_POST['name'], $_POST['age']) && is_numeric($_POST['age'])) {
        $name = $_POST['name'];
        $age = $_POST['age'];
            if(isset($curriculum)){
                echo("Hi, my name is $name and I'm $age years old. I'm a student of $curriculum \n");
            }
            else{
                echo ("Hi, my name is $name and I'm $age years old.\n");
            }

        }
        else if (isset($_POST['age']) && is_numeric($_POST['age'])) {
           $age = $_POST['age'];
           if(isset($curriculum)){
                 echo("Hi, I have no name and I'm $age years old. I'm a student of $curriculum\n");
            }
           else{
               echo ("Hi, I have no name and I'm $age years old.\n");
           }
        }
        else if (isset($_POST['name'])) {
            $name = $_POST['name'];
            if(isset($curriculum)){
                echo("Hi, my name is $name. I'm a student of $curriculum\n");
            }
            else{
                echo ("Hi, my name is $name.\n");
            }

        }

        else{
            echo  ("Hi, I have no name. \n");
        }


}