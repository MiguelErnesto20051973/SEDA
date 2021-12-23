<?php

require_once "vendor/econea/nusoap/src/nusoap.php";

login();

$namespace = "miSuperSoap2020.alv";
$server = new soap_server();
$server->configureWSDL("PinchesSOAP",$namespace);
$server->wsdl->schemaTargetNamespace = $namespace;


$server->wsdl->addComplexType(
    'articulo',
    'complexType',
    'struct',
    'all',
    '',
    array(
        'Nombre' => array('name' => 'Nombre', 'type' => 'xsd:string'),
        'Cantidad' => array('name' => 'Cantidad', 'type' => 'xsd:int'),
        'Precio' => array('name' => 'Precio', 'type' => 'xsd:decimal')
    )
);

$server->wsdl->addComplexType(
    'listaArticulos',
    'complexType',
    'array',
    '',
    'SOAP-ENC:Array',
    array(),
    array(
        array('ref' => 'SOAP-ENC:arrayType', 'wsdl:arrayType' => 'tns:articulo[]')
    )
);


$server->wsdl->addComplexType(
    'ordenDeCompra',
    'complexType',
    'struct',
    'all',
    '',
    array(
        'NumeroOrden' => array('name' => 'NumeroOrden', 'type'=>'xsd:string'),
        'Ordenante' => array('name' => 'Ordenante', 'type'=>'xsd:string'),
        'Moneda' => array('name' => 'Moneda', 'type'=>'xsd:string'),
        'TipoCambio' => array('name' => 'TipoCambio', 'type'=>'xsd:decimal'),
        'Articulos' => array('name' => 'Articulos', 'type' => 'tns:listaArticulos')
    )
);

$server->wsdl->addComplexType(
    'response',
    'complexType',
    'struct',
    'all',
    '',
    array(
        'NumeroDeAutorizacion' => array('name'=>'NumeroDeAutorizacion', 'type'=>'xsd:string'),
        'Articulo' => array('name' => 'Articulo', 'type' => 'xsd:string'),
        'Resultado' => array('name' => 'Resultado', 'type' => 'xsd:boolean')
    )
);

$server->register(
    'guardarOrdenDeCompra',
    array('name' => 'tns:ordenDeCompra'),
    array('name' => 'tns:response'),
    $namespace,
    false,
    'rpc',
    'encoded',
    'Recibe una orden de compra y regresa un numero de autorizacion'
);

function guardarOrdenDeCompra($request){
    //print_r($request);

    return array(
        "NumeroDeAutorizacion" => "La orden de compra ".$request["NumeroOrden"]." ha sido autorizada con el numero ". rand(10000, 100000),
        "Articulo" => "Sin articulos",
        "Resultado" => true
    );
}

function login(){
    if(!isset($_SERVER['PHP_AUTH_USER'])){
        header('WWW-Authenticate: Basic reaml="MiSoap"');
        header('HTTP/1.0 401 Unauthorized');
        exit;
    }

    if($_SERVER['PHP_AUTH_USER'] = 'lucio' && $_SERVER['PHP_AUTH_PW'] = 'lucio'){
        header('Content-Type: application/soap+xml; charset=utf-8');
        return true;
    }
    else{
        header('WWW-Authenticate: Basic reaml="MiSoap"');
        header('HTTP/1.0 401 Unauthorized');
        exit;
    }

}

$POST_DATA = file_get_contents("php://input");
$server->service($POST_DATA);
exit();