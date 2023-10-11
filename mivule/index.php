<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plot</title>
    <style>
        table {
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        th, td {
            width: 30px;
            height: 30px;
            border: 1px solid grey;
        }

        .point {
            background-color: green;
        }
        .pointx {
            background-color: blue;
        }
        .pointr {
            background-color: red;
        }

        .axis {
            font-weight: bold;
            text-align: center;
        }

        .axis-x, .axis-y {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">GRAPH</h1>
    <?php 
    include 'plot.php'; 
    ?>

    <form action="" method="POST">
        <label for="x-coordinate">ENTER X-COORDINATE </label>
        <input type="number" name="x" id="x-coordinate" required>
        <br>
        <label for="y-coordinate">ENTER Y-COORDINATE</label>
        <input type="number" name="y" id="y-coordinate" required>
        <br>
        <button type="submit" name="submit">PLOT</button>
    </form>
    <form action="" method="POST">
        <label for="">CLIENT REQUEST</label>
        <label for="x-coordinate-blue">ENTER X-COORDINATE (Blue)</label>
        <input type="number" name="w" id="x-coordinate-blue" required>
        <br>
        <label for="y-coordinate-blue">ENTER Y-COORDINATE (Blue)</label>
        <input type="number" name="z" id="y-coordinate-blue" required>
        <button type="submit" name="plot">PLOT</button>
    </form>
    <form action="" method="POST">
        <button type="submit" name="toggle">Toggle Calculation</button>
    </form>
</body>
</html>