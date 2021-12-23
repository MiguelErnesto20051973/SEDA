<?php

$location = "http://localhost/soap-php/index.php?wsdl";
$request = "<soapenv:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:mis=\"miSuperSoap2020.alv\" xmlns:soapenc=\"http://schemas.xmlsoap.org/soap/encoding/\">
<soapenv:Header/>
<soapenv:Body>
   <mis:guardarOrdenDeCompra soapenv:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">
      <name xsi:type=\"mis:ordenDeCompra\">
         <!--You may enter the following 5 items in any order-->
         <NumeroOrden xsi:type=\"xsd:string\">1000</NumeroOrden>
         <Ordenante xsi:type=\"xsd:string\">Lucio</Ordenante>
         <Moneda xsi:type=\"xsd:string\">MXN</Moneda>
         <TipoCambio xsi:type=\"xsd:decimal\">1</TipoCambio>
         <Articulos xsi:type=\"mis:listaArticulos\" soapenc:arrayType=\"mis:articulo[]\"/>
      </name>
   </mis:guardarOrdenDeCompra>
</soapenv:Body>
</soapenv:Envelope>";

print("Request: <br>");
print("<pre>".htmlentities($request)."</pre>");


$action = "guardarOrdenDeCompra";
$headers = [
    'Method: POST',
    'Connection: Keep-Alive',
    'User-Agent: PHP-SOAP-CURL',
    'Content-Type: text/xml; charset=utf-8',
    'SOAPAction: "guardarOrdenDeCompra"',
];




$ch = curl_init($location);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $request);
curl_setopt($ch, CURLOPT_HTTP_VERSION, CURL_HTTP_VERSION_1_1);

//tipo de autorización
//curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_NTLM);//NTLM para webservices con dominios de windows
curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);//AUTH BASIC para este caso
curl_setopt($ch, CURLOPT_USERPWD, 'lucio:lucio'); //usuario:contraseña

$response = curl_exec($ch);
$err_status = curl_error($ch);

print("Response: <br>");
print("<pre>".$response."</pre>");