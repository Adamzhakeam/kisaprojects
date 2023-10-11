<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "plot";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM cordinates";
$result = $conn->query($sql);
$pointsGreen = [];
$pointsBlue = [];
$pointsRed = [];

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $x = $row['x'];
        $y = $row['y'];
        $color = $row['color'];
        if ($color === 'green') {
            $pointsGreen[] = ['x' => $x, 'y' => $y, 'color' => $color];
        } elseif ($color === 'blue') {
            $pointsBlue[] = ['x' => $x, 'y' => $y, 'color' => $color];
        } elseif($color === 'red'){
            $pointsRed[] = ['x' => $x, 'y' => $y, 'color' =>  $color];
        }
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $x = $_POST['x'];
    $y = $_POST['y'];

    $stmt = $conn->prepare("INSERT INTO cordinates (x, y, color) VALUES (?, ?, 'green')");
    $stmt->bind_param("ii", $x, $y);
    $stmt->execute();

    $pointsGreen[] = ['x' => $x, 'y' => $y, 'color' => 'green'];
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['plot'])) {
    // Delete points with colors 'red' and 'blue' from the database
    $stmtDeleteRed = $conn->prepare("DELETE FROM cordinates WHERE color = 'red'");
    $stmtDeleteRed->execute();

    $stmtDeleteBlue = $conn->prepare("DELETE FROM cordinates WHERE color = 'blue'");
    $stmtDeleteBlue->execute();

    $xBlue = $_POST['w'];
    $yBlue = $_POST['z'];

    $stmt = $conn->prepare("INSERT INTO cordinates (x, y, color) VALUES (?, ?, 'blue')");
    $stmt->bind_param("ii", $xBlue, $yBlue);
    $stmt->execute();

    $pointsBlue[] = ['x' => $xBlue, 'y' => $yBlue, 'color' => 'blue'];
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['toggle'])) {
    $xBlue = $_POST['w'];
    $yBlue = $_POST['z'];

    $pointsGreen = []; // Clear the previous green points to fetch fresh data from the database
    $pointsBlue = []; // Clear the previous blue points to fetch fresh data from the database
    $pointsGreenX = [];
    $pointsGreenY = [];

    // Retrieve the green points from the database
    $sqlGreen = "SELECT * FROM cordinates WHERE color = 'green'";
    $resultGreen = $conn->query($sqlGreen);

    if ($resultGreen->num_rows > 0) {
        $idxq = 0;
        while ($row = $resultGreen->fetch_assoc()) {
            
            $x = $row['x'];
            $y = $row['y'];
            $color = $row['color'];
            $pointsGreen[] = ['x' => $x, 'y' => $y, 'color' => $color];
            $pointsGreenX[] = ['x', $x, 'color' => $color];
            $pointsGreenY[] = ['y', $y, 'color' => $color];
            

            $gt = $pointsGreen[$idxq]['x'];
           $xtg = $pointsGreen[$idxq]['y'];
           echo 'GREEN<br>(',$gt,',',$xtg,')';
           $idxq++;
        }
        $fg = count($pointsGreenX);
        echo $fg;
    }

    // Retrieve the blue points from the database
    $sqlBlue = "SELECT * FROM cordinates WHERE color = 'blue'";
    $resultBlue = $conn->query($sqlBlue);
    if ($resultBlue->num_rows > 0) {
        $idx = 0;
        while ($rows = $resultBlue->fetch_assoc()) {
            
            $xb = $rows['x'];
            $yb = $rows['y'];
            $color = $rows['color'];
            $pointsBlue[] = ['x' => $x, 'y' => $y, 'color' => $color];
           $xt = $pointsBlue[$idx]['x'];
           $xtx = $pointsBlue[$idx]['y'];
           echo '<br>blue(',$xb,',',$yb,')';
           $idx++;
        }
        
    }

    $lowestMagnitude = PHP_INT_MAX;
    $indexToChange = -1;

    foreach ($pointsGreen as $index => $pointGreen) {
        $i = 0;
        $magnitude = sqrt(pow($xb - $pointGreen['x'],2) + pow($yb - $pointGreen['y'],2));
        if ($magnitude < $lowestMagnitude) {
            $lowestMagnitude = $magnitude;
            $indexToChange = $index;
           echo $pointGreen['x'], ',', $pointGreen['y'] ,',',$magnitude ,'<br>';
        
        }
    }

    if ($indexToChange !== -1) {
        $xGreen = $pointsGreen[$indexToChange]['x'];
        $yGreen = $pointsGreen[$indexToChange]['y'];

        $stmt = $conn->prepare("UPDATE cordinates SET color = 'red' WHERE x = ? AND y = ? AND color = 'green'");
        $stmt->bind_param("ii", $xGreen, $yGreen);
        $stmt->execute();

        $pointsGreen[$indexToChange]['color'] = 'red';
    }
}


function displayPoints($points, $color) {
    foreach ($points as $point) {
        if ($point['color'] === $color) {
            echo "({$point['x']}, {$point['y']}) ";
        }
    }
}

$graphSize = 10;
$maxX = $graphSize;
$maxY = $graphSize;

echo '<table>';
for ($row = $maxY; $row >= 0; $row--) {
    echo '<tr>';
    for ($col = 0; $col <= $maxX; $col++) {
        $cellplot = '';
        $isGreen = false;
        $isBlue = false;

        $isRed = false;

        foreach ($pointsGreen as $pointGreen) {
            if ($pointGreen['x'] == $col && $pointGreen['y'] == $row) {
                $cellplot = 'point';
                $isGreen = true;
                break;
            }
        }

        if (!$isGreen) {
            foreach ($pointsBlue as $pointBlue) {
                if ($pointBlue['x'] == $col && $pointBlue['y'] == $row) {
                    $cellplot = 'pointx';
                    $isBlue = true;
                    break;
                }
            }
        }

        if (!$isBlue) {
            foreach ($pointsRed as $pointRed) {
                if ($pointRed['x'] == $col && $pointRed['y'] == $row) {
                    $cellplot = 'pointr';
                    $isRed = true;
                    break;
                }
            }
        }


        if ($col == 0 && $row == 0) {
            $cellplot = 'axis';
            echo "<td class='$cellplot'>($col, $row)</td>";
        } elseif ($col == 0) {
            $cellplot = 'axis-y';
            echo "<td class='$cellplot'>$row</td>";
        } elseif ($row == 0) {
            $cellplot = 'axis-x';
            echo "<td class='$cellplot'>$col</td>";
        } else {
            echo "<td class='$cellplot'></td>";
        }
    }
    echo '</tr>';
}
echo '</table>';

echo 'Plotted Points (Green): ';
displayPoints($pointsGreen, 'green');

echo '<br>';

echo 'Plotted Points (Blue): ';
displayPoints($pointsBlue, 'blue');

$conn->close();
?>
