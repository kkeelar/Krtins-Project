import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter_first_demo/progress.dart';

final usersRef = FirebaseFirestore.instance.collection('users');

class ProfilePage extends StatefulWidget {
  @override
  ProfilePageState createState() => ProfilePageState();
}

class ProfilePageState extends State<ProfilePage> {
  List dataList = [];

  @override
  Widget build(context) {
    return Text("progile page");
  }
}
