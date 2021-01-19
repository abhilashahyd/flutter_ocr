import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'dart:io';
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
    final pickedFile = await picker.getImage(source: ImageSource.gallery);
    setState(() {
      if (pickedFile != null) {
        file = File(pickedFile.path);
      } else {
        print('No image selected');
      }
    });
    print(file);
  }

// final baseUrl = 'http://flutterocr.walkingtree.tech/';
  final baseUrl = 'http://10.0.2.2:8000';
  var text;
  void getResult(res) {
    setState(() {
      text = res;
      text = jsonDecode(text);
      print(text['result']);
    });
  }

  void _upload() async {
    print(file);
    if (file == null) return;
    try {
      var postUri = Uri.parse('$baseUrl/api/create');
      http.MultipartRequest request =
          new http.MultipartRequest("POSt", postUri);
      http.MultipartFile multipartFile =
          await http.MultipartFile.fromPath("attached_file", file.path);
      request.files.add(multipartFile);
      http.StreamedResponse response = await request.send();
      print(response.statusCode);
      response.stream.bytesToString().then((value) => getResult(value));
    } on Error catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Center(child: Text('Flutter OCR',)),
        ),
        body: Column(
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                RaisedButton(
                  color: Colors.blue,
                  onPressed: _choose,
                  child: Text('Choose Image',style: TextStyle(color: Colors.white),),
                ),
                SizedBox(width: 10.0),
                RaisedButton(
                  color: Colors.blue,
                  onPressed: _upload,
                  child: Text('Upload Image',style: TextStyle(color: Colors.white),),
                ),
              ],
            ),
            file == null
                ? Text('No Image Selected')
                : SizedBox(
                    height: 250,
                    width: 150,
                    child: Image.file(file),
                  ),
            text == null
                ? Container()
                : Container(
                    height: 100,
                    width: 150,
                    child: Column(
                      children: [
                        Text('Extracted text',style: TextStyle(fontWeight: FontWeight.bold),),
                        SizedBox(height: 20,),
                        Text(text['result'],style: TextStyle(fontStyle: FontStyle.italic),),
                      ],
                    ),
                  ),
          ],
        ),
      ),
    );
  }
}
