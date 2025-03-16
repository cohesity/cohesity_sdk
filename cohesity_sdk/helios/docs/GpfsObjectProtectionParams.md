# GpfsObjectProtectionParams

Specifies the parameters which are specific to Gpfs object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.gpfs_object_protection_params import GpfsObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of GpfsObjectProtectionParams from a JSON string
gpfs_object_protection_params_instance = GpfsObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(GpfsObjectProtectionParams.to_json())

# convert the object into a dict
gpfs_object_protection_params_dict = gpfs_object_protection_params_instance.to_dict()
# create an instance of GpfsObjectProtectionParams from a dict
gpfs_object_protection_params_from_dict = GpfsObjectProtectionParams.from_dict(gpfs_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


