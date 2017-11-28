# FruitFul Backend

This is the Flask based backend for our Fruitful Android Application


## Main EndPoint

```
http://162.243.165.201:3000/
```

### Authentication (Subject to Change)

For now authentication works by trying to access the main endpoint with the users credentials.

For Example: (in Android)

```
http://162.243.165.201:3000/
auth(user_name, password)
```  

## POST a user


```
String reply = null;
String resJson=""; //capture acknowledgement from server, if any

//Construct an HTTP POST
HttpClient httpclient = new DefaultHttpClient();
HttpPost storeVal = new HttpPost("http://162.243.165.201:3000/api/user");

// Values to be sent from android app to server
ArrayList<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();

// "tag" is the name of the text form on the webserver
// "value" is the value that the client is submitting to the server
// These two are specified by the server. The cilent side program must respect.
nameValuePairs.add(new BasicNameValuePair("name", "admin"));
nameValuePairs.add(new BasicNameValuePair("password", "password"));


try {
    UrlEncodedFormEntity httpEntity = new UrlEncodedFormEntity(nameValuePairs);
    storeVal.setEntity(httpEntity);

    //Execute HTTP POST
    HttpResponse response = httpclient.execute(storeVal);
    //Capture acknowledgement from server
    // In this demo app, the server returns "Update" if the tag already exists;
    // Otherwise, the server returns "New"
    resJson = EntityUtils.toString(response.getEntity());
    }
```


## GET a User
```
"http://162.243.165.201:3000/api/user/<USER_ID>"
```

```
String reply = null;
String resJson=""; //capture acknowledgement from server, if any

//Construct an HTTP GET
HttpClient httpclient = new DefaultHttpClient();
HttpGet storeVal = new HttpGet("http://162.243.165.201:3000/api/user/<USER_ID>");

try {
    //Execute HTTP GET
    HttpResponse response = httpclient.execute(storeVal);

    resJson = EntityUtils.toString(response.getEntity());
    }
```

As of now this is what you can except in a response here:
```
{
    'name': ,// USERNAME
    'fruit_count': , // TOTAL COUNT OF FRUIT
    'created_date': , // UTC TIME WHICH THE USER WAS CREATED
    'fruits': , // NAME OF ALL FRUITS WHICH THE USER HAS LOGGED
}
```
Let me know what other attributes you would like me to add.

## PUT

```
String reply = null;
String resJson=""; //capture acknowledgement from server, if any

//Construct an HTTP PUT
HttpClient httpclient = new DefaultHttpClient();
HttpPut storeVal = new HttpPut("http://162.243.165.201:3000/api/user/<USER_ID>");

// Values to be sent from android app to server
ArrayList<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();

// "tag" is the name of the text form on the webserver
// "value" is the value that the client is submitting to the server
// These two are specified by the server. The cilent side program must respect.
nameValuePairs.add(new BasicNameValuePair("fruit", "apple"));


try {
    UrlEncodedFormEntity httpEntity = new UrlEncodedFormEntity(nameValuePairs);
    storeVal.setEntity(httpEntity);

    
    //Execute HTTP PUT
    HttpResponse response = httpclient.execute(storeVal);
    //Capture acknowledgement from server
    // In this demo app, the server returns "Update" if the tag already exists;
    // Otherwise, the server returns "New"
    resJson = EntityUtils.toString(response.getEntity());
    }
```





## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

