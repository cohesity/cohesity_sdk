# ModifySourceHierarchyObjectsRequest

Specifies the parameters to add/update objects to/from entity hierarchy. This is a batch API that accepts multiple modification requests. Each request in the batch should specify one object to modify.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modification_requests** | [**[SourceHierarchyModificationRequest]**](SourceHierarchyModificationRequest.md) | List of modification requests to perform on the source. Each request operates on a single leaf object. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


