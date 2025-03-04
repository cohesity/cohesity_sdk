# NasQosPolicy

Specifies the QoS policy, which defines the principal and priority of a NAS recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the QoS Policy. | [optional] 

## Example

```python
from cohesity_sdk.models.nas_qos_policy import NasQosPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of NasQosPolicy from a JSON string
nas_qos_policy_instance = NasQosPolicy.from_json(json)
# print the JSON string representation of the object
print(NasQosPolicy.to_json())

# convert the object into a dict
nas_qos_policy_dict = nas_qos_policy_instance.to_dict()
# create an instance of NasQosPolicy from a dict
nas_qos_policy_from_dict = NasQosPolicy.from_dict(nas_qos_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


