### Aql-Logging-Api

#### What is it used for?
This api is used for logging events that happen on the AQL network.

#### What is the Aql Network?
The aql network is a group of Docker environments running on 3 raspberry Pis. 
They host a number of services from Bill Schedulers to Repository hygiene tools.

#### How does the logger work?
Ideally you want to use the `RemoteLogger.py` Class in your application. This will
create the logger with a request to send to the API. You can specify the endpoint 
where the logger-api is running. It is super simple to use.

#### Where can I send data and how?
You can create a POST request to the endpoint the logger-api is running.<br>
For example : `http://localhost:5000/log` <br>

In the request body send this json object.

```
{
"service": "<Service Name>",
"event": "<Event name>",
"details": "<Details of the event>",
}
```

#### How can I view the data?
You can view the data via the logger-api's UI which is located @ `http://localhost:5000/`