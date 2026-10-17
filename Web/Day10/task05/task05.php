<?php
header('Content-Type: application/json');

try {
    $pdo = new PDO('sqlite:ajax_products.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Error: database connection failed.']);
    exit;
}

$type   = strtolower(trim($_GET['type'] ?? ''));
$brand  = strtolower(trim($_GET['brand'] ?? ''));
$price  = trim($_GET['price'] ?? '');
$number = trim($_GET['number'] ?? '');

$errors = [];

// ---- Type ----
$stmt = $pdo->prepare('SELECT COUNT(*) FROM products WHERE LOWER(type) = ?');
$stmt->execute([$type]);
if ($stmt->fetchColumn() == 0) {
    $errors['type'] = "Error ($type): this type doesn't exist in our shop.";
}

// ---- Brand ----
$stmt = $pdo->prepare('SELECT COUNT(*) FROM products WHERE LOWER(brand) = ? AND LOWER(type) = ?');
$stmt->execute([$brand, $type]);
if (!isset($errors['type']) && $stmt->fetchColumn() == 0) {
    $errors['brand'] = "Error ($brand): this brand doesn't exist in our database.";
}

// ---- Price: one operator (<, >, =) followed by digits ----
$products = [];
if (!preg_match('/^([<>=])(\d+)$/', $price, $m)) {
    $errors['price'] = "Error ($price): we cannot define a price - string invalid.";
} else {
    $operator = $m[1];
    $value    = (int) $m[2];
    if (!in_array($operator, ['<', '>', '='], true)) {
        $errors['price'] = "Error ($price): we cannot define a price - string invalid.";
    } else {
        // The operator cannot be a placeholder, so it is whitelisted above.
        $stmt = $pdo->prepare("SELECT type, brand, price, stock FROM products WHERE LOWER(type) = ? AND LOWER(brand) = ? AND price $operator ?");
        $stmt->execute([$type, $brand, $value]);
        $products = $stmt->fetchAll(PDO::FETCH_ASSOC);
        if (count($products) === 0) {
            $errors['price'] = "Error ($price): no products found at this price.";
        }
    }
}

// ---- Number: the requested quantity against stock ----
$requested = (int) $number;
$stmt = $pdo->prepare('SELECT stock FROM products WHERE LOWER(type) = ? AND LOWER(brand) = ?');
$stmt->execute([$type, $brand]);
$stock = (int) $stmt->fetchColumn();

if ($requested <= 0) {
    $errors['number'] = "Error ($number): not a positive number.";
} elseif ($requested > $stock) {
    $errors['number'] = "Error ($number): sorry, we don't have enough stock, we only have $stock in stock.";
}

if (count($errors) > 0) {
    echo json_encode(['success' => false, 'errors' => $errors, 'products' => []]);
    exit;
}

// Build the table rows: the requested number replaces the missing column.
$rows = [];
foreach ($products as $p) {
    $rows[] = [
        'type'   => $p['type'],
        'brand'  => $p['brand'],
        'price'  => $p['price'],
        'number' => $requested,
        'stock'  => $p['stock'],
    ];
}

echo json_encode(['success' => true, 'errors' => [], 'products' => $rows]);