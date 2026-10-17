<?php
header('Content-Type: application/json');

try {
    $pdo = new PDO('sqlite:ajax_products.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['success' => false, 'errors' => ['type' => 'Error: database connection failed.']]);
    exit;
}

$type   = strtolower(trim($_GET['type'] ?? ''));
$brand  = strtolower(trim($_GET['brand'] ?? ''));
$price  = trim($_GET['price'] ?? '');
$number = trim($_GET['number'] ?? '');

$errors = [];

// ---- Check 1: all fields filled in ----
if ($type === '')   $errors['type']   = 'Error: no type sent yet!';
if ($brand === '')  $errors['brand']  = 'Error: no brand sent yet!';
if ($price === '')  $errors['price']  = 'Error: no price sent yet!';
if ($number === '') $errors['number'] = 'Error: no number sent yet!';

// ---- Check 2: the same validity rules as the search ----
if (!$errors) {
    if (!preg_match('/^\d+$/', $price)) {
        $errors['price'] = "Error ($price): we cannot define a price - string invalid.";
    }
    if (!preg_match('/^\d+$/', $number) || (int) $number < 0) {
        $errors['number'] = "Error ($number): not a positive number.";
    }
}

if (count($errors) > 0) {
    echo json_encode(['success' => false, 'errors' => $errors]);
    exit;
}

$price  = (int) $price;
$number = (int) $number;

// ---- Check 3: does the product already exist? ----
$stmt = $pdo->prepare('SELECT id FROM products WHERE LOWER(type) = ? AND LOWER(brand) = ?');
$stmt->execute([$type, $brand]);
$existing = $stmt->fetch(PDO::FETCH_ASSOC);

if ($existing) {
    // Update price and stock; both may be 0.
    $stmt = $pdo->prepare('UPDATE products SET price = ?, stock = ? WHERE id = ?');
    $stmt->execute([$price, $number, $existing['id']]);
    $message = 'Product updated.';
} else {
    // Insert a new product; number becomes its stock.
    $stmt = $pdo->prepare('INSERT INTO products (type, brand, price, stock) VALUES (?, ?, ?, ?)');
    $stmt->execute([$type, $brand, $price, $number]);
    $message = 'Product added.';
}

echo json_encode(['success' => true, 'errors' => [], 'message' => $message]);