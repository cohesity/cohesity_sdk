# FailoverObject

Specifies the details about the objects being failed over.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Specifies the object Id involved in failover operation. | 

## Example

```python
from cohesity_sdk.cluster.models.failover_object import FailoverObject

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverObject from a JSON string
failover_object_instance = FailoverObject.from_json(json)
# print the JSON string representation of the object
print(FailoverObject.to_json())

# convert the object into a dict
failover_object_dict = failover_object_instance.to_dict()
# create an instance of FailoverObject from a dict
failover_object_from_dict = FailoverObject.from_dict(failover_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


