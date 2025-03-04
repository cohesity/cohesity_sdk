# RecoveryObjectIdentifier

Specifies the object identifier to perform recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.recovery_object_identifier import RecoveryObjectIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryObjectIdentifier from a JSON string
recovery_object_identifier_instance = RecoveryObjectIdentifier.from_json(json)
# print the JSON string representation of the object
print(RecoveryObjectIdentifier.to_json())

# convert the object into a dict
recovery_object_identifier_dict = recovery_object_identifier_instance.to_dict()
# create an instance of RecoveryObjectIdentifier from a dict
recovery_object_identifier_from_dict = RecoveryObjectIdentifier.from_dict(recovery_object_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


