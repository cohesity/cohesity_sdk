# HiveAdditionalParams

Additional params for Hive protection source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authentication type. | [optional] [readonly] 
**metastore_address** | **str** | The MetastoreAddress for this Hive. | [optional] [readonly] 
**metastore_port** | **int** | The MetastorePort for this Hive. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.hive_additional_params import HiveAdditionalParams

# TODO update the JSON string below
json = "{}"
# create an instance of HiveAdditionalParams from a JSON string
hive_additional_params_instance = HiveAdditionalParams.from_json(json)
# print the JSON string representation of the object
print(HiveAdditionalParams.to_json())

# convert the object into a dict
hive_additional_params_dict = hive_additional_params_instance.to_dict()
# create an instance of HiveAdditionalParams from a dict
hive_additional_params_from_dict = HiveAdditionalParams.from_dict(hive_additional_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


