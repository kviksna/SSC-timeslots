<head>
    
</head>
<body bgcolor="black" text="gray">
    <h2>SSC swim timeslots: stunda(aizņemts/kopā)</h2>
    
<?php
function get($d) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://bookla.com/api/v3/timeslots');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, '{"companyId":"042fb9ab-5dd4-4b78-a8ac-d1229322e93d","date":"'.$d.'","slotParams":{"serviceId":"09b3b303-fb77-45d9-bcf2-1434b672f679","spots":1,"tickets":[{"ticketId":"ecbf6d32-f517-40b1-abc6-3e263ffb2d86","spots":1}]}}');
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json', 'SpendoDeviceID: e20d129b-e209-4b4a-9aae-1703eb14c224',
        'SpendoSig: bf8358a8feeb0ec0124df0506975a3a12636cd29a13de917300e010af4a7f6fe', 'SpendoApp: Web/Widget'
    ));
    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        echo 'Error: ' . curl_error($ch);
    } else {
        return $response;
    }

    curl_close($ch);
}//EO get("2023-05-03T00:00:00.000Z")

//echo get("2023-05-03T00:00:00.000Z");

function decode($strData) {
  if (strlen($strData) < 150) {
    echo date('Y.m.d') . " => EOD<br>\n";
    return 0;
  }

  $jData = json_decode($strData, true);
  $date = substr($jData["calendars"][0]["timeslots"][0]["startTime"],0,10);
  $hour = substr($jData["calendars"][0]["timeslots"][0]["startTime"],11,2);
  //echo "$date: ".$date; echo "<br>\n";
  //echo "$hour: ".$hour; echo "<br>\n";

  $i = 0;
  foreach ($jData["calendars"][0]["timeslots"] as $elem) {
    //echo "elem[startTime]: ".$elem["startTime"]; echo "<br>\n";
    $day = substr($elem["startTime"],0,10);
    $hour = intval(substr($elem["startTime"],11,2))+3;
    //echo "$date: ".$date; echo "<br>\n";
    //echo "$hour: ".$hour; echo "<br>\n";
    
    if ($i == 0) { echo $day . ' '; }
    echo "{$hour}({$elem["spotsTaken"]}/{$elem["spotsTotal"]}) ";
    $i += 1;
  }
  echo "<br>\n";
}//EO decode($strData)

//decode(get("2023-05-03T00:00:00.000Z"));
decode(get(gmdate('Y-m-d\T00:00:00.000\Z',strtotime('+0 day'))));
decode(get(gmdate('Y-m-d\T00:00:00.000\Z',strtotime('+1 day'))));
decode(get(gmdate('Y-m-d\T00:00:00.000\Z',strtotime('+2 day'))));
?>
</body>

<!--
<?="Hello from PHP version():".phpversion()?>
Was: 8.0.7
-->
