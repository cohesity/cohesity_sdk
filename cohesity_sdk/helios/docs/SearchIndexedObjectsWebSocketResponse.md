# SearchIndexedObjectsWebSocketResponse

The response parameters sent by the MCM Search Sndexed Sbject Websocket.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **int, none_type** | ID of the message, to which the response belongs. This ID is returned as sent by the client. | 
**body** | [**HeliosSearchIndexedObjectsResponseBody**](HeliosSearchIndexedObjectsResponseBody.md) |  | 
**status** | **str, none_type** | Denotes if the search operation is complete, errored or in-progress and if it is safe to close the websocket by the client in case there aren&#39;t any additional search requests to be sent by the client. | [optional] 
**error** | **str, none_type** | Error message, this will be populated if status is Error | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


