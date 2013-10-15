<?php

$dl_rate = 64.0; // KB/s
$request = trim($_SERVER['REQUEST_URI'], '/');
$protoc = isset($_SERVER['SERVER_PROTOCOL']) ? $_SERVER['SERVER_PROTOCOL'] : 'HTTP/1.0';

if(file_exists($request) && is_file($request))
{

	header('Cache-control: private');
	header('Content-Type: application/octet-stream');
	header('Content-Length: ' . filesize($request));
	//header('Content-Disposition: filename=' . $request);

	flush();

        $file = @fopen($request, 'rb');
        if(!$file)
        {
                header($protoc . ' 500');
                die('Error: Could not read ' . $request . '');
        }

	while(!feof($file))
	{
		print(fread($file, round($dl_rate*1024)));
		flush();
		sleep(1);
	}
	fclose($file);
} else
{
	header($protoc . ' 404');
	die('Error: File ' . $request . ' does not exist');
}

?>
