<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figuras Geométricas con SVG</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #add8e6; /* Celeste */
      color: #333;
      text-align: center;
    }
    h1 {
      color: #2c3e50;
    }
    section {
      margin-bottom: 40px;
      background-color: #ffff99; /* Amarillo claro */
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    svg {
      border: 1px solid #ccc;
      margin: 10px auto;
      background-color: #fff;
      display: block;
    }
    .image-group {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
    }
    .image-with-description {
      display: flex;
      flex-direction: column;
      align-items: center;
      max-width: 150px;
    }
    p {
      max-width: 600px;
      margin: 10px auto;
      text-align: center;
    }
    .figure-name {
      font-weight: bold;
      margin-top: 5px;
    }
  </style>
</head>
<body>
  <h1>Figuras Geométricas usando SVG</h1>

  <section>
    <h2>1. Círculo</h2>
    <svg width="100" height="100">
      <circle cx="50" cy="50" r="40" fill="blue" />
    </svg>
    <p>Este es un círculo con radio 40 y color de relleno azul.</p>
  </section>

  <section>
    <h2>2. Rectángulo</h2>
    <svg width="120" height="100">
      <rect width="100" height="60" x="10" y="20" fill="green" />
    </svg>
    <p>Este es un rectángulo verde de dimensiones 100x60 píxeles, desplazado desde la esquina.</p>
  </section>

  <section>
    <h2>3. Elipse</h2>
    <svg width="150" height="100">
      <ellipse cx="75" cy="50" rx="60" ry="30" fill="orange" />
    </svg>
    <p>Una elipse con radios 60 (horizontal) y 30 (vertical), de color naranja.</p>
  </section>

  <section>
    <h2>4. Polígono (Pentágono)</h2>
    <svg width="150" height="100">
      <polygon points="75,10 120,40 100,90 50,90 30,40" fill="red" />
    </svg>
    <p>Un pentágono rojo formado por 5 puntos con vértices bien definidos.</p>
  </section>

  <section>
    <h2>5. Polígono (Triángulo)</h2>
    <svg width="100" height="100">
      <polygon points="50,10 90,90 10,90" fill="purple" />
    </svg>
    <p>Un triángulo equilátero morado definido por 3 puntos.</p>
  </section>
</body>
</html>
