import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite/tflite.dart';

void main() => runApp(FarmerAIApp());

class FarmerAIApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI Assistant for Farmers',
      theme: ThemeData(primarySwatch: Colors.green),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final picker = ImagePicker();
  String _diagnosis = "Take a picture to diagnose plant diseases.";

  @override
  void initState() {
    super.initState();
    loadModel();
  }

  Future<void> loadModel() async {
    await Tflite.loadModel(
      model: "assets/plant_disease_model.tflite",
      labels: "assets/labels.txt",
    );
  }

  Future<void> diagnoseImage(String path) async {
    var recognitions = await Tflite.runModelOnImage(
      path: path,
      numResults: 3,
      threshold: 0.5,
    );

    setState(() {
      if (recognitions != null && recognitions.isNotEmpty) {
        _diagnosis = recognitions[0]['label'];
      } else {
        _diagnosis = "Unable to diagnose the image. Try again.";
      }
    });
  }

  Future<void> pickImage() async {
    final pickedFile = await picker.pickImage(source: ImageSource.camera);

    if (pickedFile != null) {
      diagnoseImage(pickedFile.path);
    } else {
      setState(() {
        _diagnosis = "No image selected.";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("AI Assistant for Farmers")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              _diagnosis,
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: pickImage,
              child: Text("Capture Image"),
            ),
          ],
        ),
      ),
    );
  }
}