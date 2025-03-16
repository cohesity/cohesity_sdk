# ElastifileObjectProtectionParams

Specifies the parameters which are specific to Elastifile object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.elastifile_object_protection_params import ElastifileObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ElastifileObjectProtectionParams from a JSON string
elastifile_object_protection_params_instance = ElastifileObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(ElastifileObjectProtectionParams.to_json())

# convert the object into a dict
elastifile_object_protection_params_dict = elastifile_object_protection_params_instance.to_dict()
# create an instance of ElastifileObjectProtectionParams from a dict
elastifile_object_protection_params_from_dict = ElastifileObjectProtectionParams.from_dict(elastifile_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


