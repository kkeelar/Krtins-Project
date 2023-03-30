import 'package:flutter/material.dart';

AppBar header() {
  return AppBar(
    title: const Text(
      "JukeBox",
      style: TextStyle(
        color: Colors.white,
        fontFamily: 'Segoe UI',
        fontSize: 40.0,
      ),
    ),
    centerTitle: true,
    backgroundColor: const Color(0xff0f0c0c),
    toolbarHeight: 100.0,
  );
}
