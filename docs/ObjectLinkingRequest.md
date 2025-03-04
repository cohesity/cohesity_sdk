# ObjectLinkingRequest

Request for linking replicated objects to failover objects on replication cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_map** | [**List[ReplicaFailoverObject]**](ReplicaFailoverObject.md) | Specifies the objectMap that will be used to create linking between given replicated source entity and newly restored entity on erplication cluster. | [optional] 

## Example

```python
from cohesity_sdk.models.object_linking_request import ObjectLinkingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectLinkingRequest from a JSON string
object_linking_request_instance = ObjectLinkingRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectLinkingRequest.to_json())

# convert the object into a dict
object_linking_request_dict = object_linking_request_instance.to_dict()
# create an instance of ObjectLinkingRequest from a dict
object_linking_request_from_dict = ObjectLinkingRequest.from_dict(object_linking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


