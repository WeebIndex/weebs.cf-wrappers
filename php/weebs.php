<?php

class weebs {

  public static function hug() {
    $text = file_get_contents("https://weebs.cf/random/hug");
    return $text;
  }

  public static function punch() {
    $text = file_get_contents("https://weebs.cf/random/punch");
    return $text;
  }

  public static function poke() {
    $text = file_get_contents("https://weebs.cf/random/poke");
    return $text;
  }

  public static function kiss() {
    $text = file_get_contents("https://weebs.cf/random/kiss");
    return $text;
  }

  public static function slap() {
    $text = file_get_contents("https://weebs.cf/random/slap");
    return $text;
  }

  public static function laugh() {
    $text = file_get_contents("https://weebs.cf/random/laugh");
    return $text;
  }
  

}

?>