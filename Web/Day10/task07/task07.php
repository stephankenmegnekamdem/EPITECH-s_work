<?php
header('Content-Type: application/json');

try {
    $pdo = new PDO('sqlite:ajax_products.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Database connection failed.']);
    exit;
}

// Create the table on first use. IF NOT EXISTS makes this safe to run every time.
$pdo->exec('CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Save a new message.
    $name    = trim($_POST['name'] ?? '');
    $message = trim($_POST['message'] ?? '');

    if ($name === '' || $message === '') {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Name and message are required.']);
        exit;
    }

    $stmt = $pdo->prepare('INSERT INTO messages (name, message) VALUES (?, ?)');
    $stmt->execute([$name, $message]);
    echo json_encode(['success' => true]);
    exit;
}

// GET: return all messages, oldest first.
$stmt = $pdo->query('SELECT name, message, created_at FROM messages ORDER BY id ASC');
echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));