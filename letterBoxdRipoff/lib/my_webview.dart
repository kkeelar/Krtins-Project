import 'package:flutter/material.dart';
import 'package:flutter_webview_plugin/flutter_webview_plugin.dart';

class MyWebView extends StatefulWidget {
  @override
  _MyWebViewState createState() => _MyWebViewState();
}

class _MyWebViewState extends State<MyWebView> {
  @override
  Widget build(BuildContext context) {
    return WebviewScaffold(
      url: 'http://192.168.1.210:8080',
      appBar: AppBar(
        title: Text('My HTML Page'),
      ),
      withZoom: true,
      withLocalStorage: true,
      hidden: true,
      initialChild: Container(
        color: Colors.black,
        child: const Center(
          child: Text('Loading...'),
        ),
      ),
    );
  }
}
