# GcpProtectionGroupParams

Specifies the parameters which are specific to GCP related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_protection_type_params** | [**GcpNativeProtectionGroupParams**](GcpNativeProtectionGroupParams.md) |  | [optional] 
**protection_type** | **str** | Specifies the GCP Protection Group type. | 

## Example

```python
from cohesity_sdk.models.gcp_protection_group_params import GcpProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpProtectionGroupParams from a JSON string
gcp_protection_group_params_instance = GcpProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GcpProtectionGroupParams.to_json())

# convert the object into a dict
gcp_protection_group_params_dict = gcp_protection_group_params_instance.to_dict()
# create an instance of GcpProtectionGroupParams from a dict
gcp_protection_group_params_from_dict = GcpProtectionGroupParams.from_dict(gcp_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


