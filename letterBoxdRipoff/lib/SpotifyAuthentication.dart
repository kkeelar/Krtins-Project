import 'package:flutter/material.dart';
import 'package:flutter_facebook_auth/flutter_facebook_auth.dart';
import 'package:spotify_sdk/spotify_sdk.dart';

void main() {
  runApp(SpotifyAuthApp());
}

class SpotifyAuthApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Spotify Authentication Example',
      theme: ThemeData(
        primarySwatch: Colors.purple,
        backgroundColor: Colors.black,
        textTheme: TextTheme(
          headline6: TextStyle(
            color: Colors.white,
            fontSize: 24.0,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
      home: LoginScreen(),
    );
  }
}

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ElevatedButton(
          child: Text(
            'Connect to Spotify',
            style: Theme.of(context).textTheme.headline6,
          ),
          style: ElevatedButton.styleFrom(
            primary: Colors.purple,
          ),
          onPressed: () async {
            // Initialize the Spotify SDK with your client ID and redirect URI
            await SpotifySdk.connectToSpotifyRemote(
              clientId: '8363379319de4c7ab267c09ef7e6f416',
              redirectUrl: 'http://192.168.1.210:8080',
              print("Helloswpe");
            );

            // Authenticate the user
            //   final result = await SpotifySdk.getAccessToken(
            //       clientId: '8363379319de4c7ab267c09ef7e6f416',
            //       redirectUrl: 'http://192.168.1.210:8080');

            //   if (result.isSuccess) {
            //     print('Successfully authenticated with Spotify');
            //   } else {
            //     print('Error authenticating with Spotify: ${result.error}');
            //   }
          },
        ),
      ),
    );
  }
}
