# CommonOracleExternalTargetParams

Specifies the common parameters which are specific to Oracle related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the access key id of the external target. | 
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**region** | **str** | Specifies the region of the external target. | 
**storage_access_key** | **str** | Specifies the storage access key of the external target. | [optional] 
**tenancy** | **str** | Specifies the tenancy of the external target. | 

## Example

```python
from cohesity_sdk.helios.models.common_oracle_external_target_params import CommonOracleExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonOracleExternalTargetParams from a JSON string
common_oracle_external_target_params_instance = CommonOracleExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonOracleExternalTargetParams.to_json())

# convert the object into a dict
common_oracle_external_target_params_dict = common_oracle_external_target_params_instance.to_dict()
# create an instance of CommonOracleExternalTargetParams from a dict
common_oracle_external_target_params_from_dict = CommonOracleExternalTargetParams.from_dict(common_oracle_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


