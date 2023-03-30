// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:flutter/material.dart';

class DashboardScreen extends StatefulWidget {
  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
      width: double.infinity,
      height: double.infinity,
      alignment: Alignment.center,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Padding(
            padding: EdgeInsets.only(top: 50), // adjust the top padding here
            child: Text(
              'My Profile',
              style: TextStyle(
                color: Colors.purple,
                fontSize: 30,
                fontWeight: FontWeight.w600,
                decoration: TextDecoration.underline,
                decorationThickness: 4,
                decorationColor: Colors.purple,
              ),
            ),
          ),
        ],
      ),
    ));
    // Row(
    //     mainAxisAlignment: MainAxisAlignment.start,
    //     crossAxisAlignment: CrossAxisAlignment.center,
    //     children: [
    //   Padding(padding: EdgeInsets.only(top: 25)),
    //   Text(
    //     'My Profile',
    //     style: TextStyle(
    //       color: Colors.black,
    //       fontSize: 25,
    //       fontWeight: FontWeight.w600,
    //       decoration: TextDecoration.underline,
    //       decorationThickness: 4,
    //     ),
    //   ),
    // ]));
  }
}

class MyAppBar extends StatelessWidget implements PreferredSizeWidget {
  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.deepPurple,
      title: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          Text('JukeBox'),
        ],
      ),
      actions: <Widget>[
        Padding(
          padding: const EdgeInsets.only(right: 25.0),
          child: IconButton(
            icon: Icon(Icons.edit),
            onPressed: () {
              // Perform some action
            },
          ),
        ),
      ],
    );
  }

  @override
  Size get preferredSize => Size.fromHeight(75.0);
}
