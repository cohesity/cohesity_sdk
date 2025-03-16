# AddRegionParams

Information about each region that is being added.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_info** | [**KmsKeyBasicInfo**](KmsKeyBasicInfo.md) |  | [optional] 
**region_id** | **str** | ID that identifies a region. | 
**storage_class** | **str** | Specifies the AWS storage class. When the storageClass is not given, set it to the default value, &#39;kAmazonS3StandardIA&#39;. | [optional] 
**vault_name** | **str** | FortKnox vault name. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_region_params import AddRegionParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddRegionParams from a JSON string
add_region_params_instance = AddRegionParams.from_json(json)
# print the JSON string representation of the object
print(AddRegionParams.to_json())

# convert the object into a dict
add_region_params_dict = add_region_params_instance.to_dict()
# create an instance of AddRegionParams from a dict
add_region_params_from_dict = AddRegionParams.from_dict(add_region_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


