# FlashbladeParams

Specifies the information related to Registered Pure Flashblade.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_capacity_bytes** | **int** | Specifies the capacity in bytes assigned on pure flashblade for remote storage usage on cohesity cluster. | [optional] 
**assigned_data_vips** | **List[str]** | Specifies list of data vips that are assigned to cohesity cluster to create nfs share mountpoints. | [optional] 
**available_capacity** | **int** | Available capacity on pure flashblade. | [optional] [readonly] 
**available_data_vips** | **List[Optional[str]]** | Available data vips configured on pure flashblade. | [optional] [readonly] 
**created_file_system_count** | **int** | Number of new file systems created on pure flashblade when assignedCapacityBytes is updated. | [optional] [readonly] 
**is_dedicated_storage** | **bool** | If true, cohesity cluster uses all available capacity on pure flashblade for remote storage. | [optional] 
**name** | **str** | Name of the pure flashblade specified on pure storage. | [optional] [readonly] 
**registration_params** | [**FlashBladeRegistrationInfo**](FlashBladeRegistrationInfo.md) |  | [optional] 
**software_os_version** | **str** | Software OS and version running on pure flashblade | [optional] [readonly] 
**total_capacity** | **int** | Total capacity of pure flashblade. | [optional] [readonly] 
**updated_file_system_count** | **int** | Number of file systems that are updated on pure flashblade when assignedCapacityBytes is updated. | [optional] [readonly] 
**uuid** | **str** | Specifies uuid of the pure flashblade server. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.flashblade_params import FlashbladeParams

# TODO update the JSON string below
json = "{}"
# create an instance of FlashbladeParams from a JSON string
flashblade_params_instance = FlashbladeParams.from_json(json)
# print the JSON string representation of the object
print(FlashbladeParams.to_json())

# convert the object into a dict
flashblade_params_dict = flashblade_params_instance.to_dict()
# create an instance of FlashbladeParams from a dict
flashblade_params_from_dict = FlashbladeParams.from_dict(flashblade_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


