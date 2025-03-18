# TieringExternalTargetParams

Specifies the parameters which are specific to Tiering purpose type External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_level** | **str** | Specifies the type of encryption for the Setting. | 
**storage_type** | **str** | Specifies the Storage type of the External Target. | 
**aws_params** | [**TieringAwsExternalTargetParams**](TieringAwsExternalTargetParams.md) |  | [optional] 
**azure_params** | [**TieringAzureExternalTargetParams**](TieringAzureExternalTargetParams.md) |  | [optional] 
**gcp_params** | [**TieringGcpExternalTargetParams**](TieringGcpExternalTargetParams.md) |  | [optional] 
**oracle_params** | [**TieringOracleExternalTargetParams**](TieringOracleExternalTargetParams.md) |  | [optional] 
**s3_comp_params** | [**CommonS3CompExternalTargetParams**](CommonS3CompExternalTargetParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tiering_external_target_params import TieringExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of TieringExternalTargetParams from a JSON string
tiering_external_target_params_instance = TieringExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(TieringExternalTargetParams.to_json())

# convert the object into a dict
tiering_external_target_params_dict = tiering_external_target_params_instance.to_dict()
# create an instance of TieringExternalTargetParams from a dict
tiering_external_target_params_from_dict = TieringExternalTargetParams.from_dict(tiering_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


