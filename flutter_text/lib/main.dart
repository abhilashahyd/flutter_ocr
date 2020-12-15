import 'package:flutter/material.dart';
import 'dart:io';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
void main() {
  runApp(MyHomePage());
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  
  File file;
  final picker = ImagePicker();
  var result;

 void _choose() async {
 final  pickedFile = await picker.getImage(source: ImageSource.gallery);
   setState(() {
        if(pickedFile != null){
          file = File(pickedFile.path);
        }else{
          print('No image selected');
        }
      });
   print(file);
 }
// final baseUrl = 'http://flutterocr.walkingtree.tech/';
  final baseUrl = 'http://10.0.2.2:8000';
 void _upload() async{
   print(file);
   if (file == null) return;
   String base64Image = base64Encode(file.readAsBytesSync());
   // String fileName = file.path.split("/").last;

   try {
     Map data = {'attached_file': base64Image };
     var body = json.encode(data);

     final  response = await http.post('$baseUrl/api/create',
       headers: <String, String>{
         'Content-Type': 'application/json; charset=UTF-8',
       },
       body: body
     );
     print(response.statusCode);
     print(response.body.toString());

 } on Error catch(e) {
     print(e);
   }
 }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
      // appBar: AppBar(),
      body: Column(
        children: <Widget>[
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              RaisedButton(
                onPressed: _choose,
                child: Text('Choose Image'),
              ),
              SizedBox(width: 10.0),
              RaisedButton(
                onPressed: _upload,
                child: Text('Upload Image'),
              ),
              result == null ? Text('Error in Detecting') : Container(
                height: 100,width: 50,
                child: Text(result.toString()),
              )
            ],
          ),
          file == null
            ? Text('No Image Selected')
            : SizedBox(
            height: 130,
            width: 100,
            child: Image.file(file),
          )
        ],
      ),
    ),
    );
  }
}