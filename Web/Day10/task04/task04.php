<?php
header('Content-Type: application/json');

try {
    $pdo = new PDO('sqlite:ajax_products.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode([
        'type' => 'Database connection failed.',
        'typeValid' => false,
        'brand' => '',
        'brandValid' => false
    ]);
    exit;
}

$type  = strtolower(trim($_GET['type'] ?? ''));
$brand = strtolower(trim($_GET['brand'] ?? ''));

// Does the type exist?
$stmt = $pdo->prepare('SELECT COUNT(*) FROM products WHERE LOWER(type) = ?');
$stmt->execute([$type]);
$typeExists = $stmt->fetchColumn() > 0;

if ($typeExists) {
    $typeMessage = 'type: this type exists in databases.';
} else {
    $typeMessage = "type: this type doesn't exist in our shop.";
}

// Does the brand already exist?
$stmt = $pdo->prepare('SELECT COUNT(*) FROM products WHERE LOWER(brand) = ?');
$stmt->execute([$brand]);
$brandExists = $stmt->fetchColumn() > 0;

$brandValid = false;
if ($brandExists) {
    $brandMessage = 'brand: this brand already exists in databases.';
} elseif ($typeExists) {
    $brandMessage = "brand: this brand is valid for the type $type.";
    $brandValid = true;
} else {
    // Type is unknown, so the brand cannot be valid for it.
    $brandMessage = '';
}

echo json_encode([
    'type' => $typeMessage,
    'typeValid' => $typeExists,
    'brand' => $brandMessage,
    'brandValid' => $brandValid
]);