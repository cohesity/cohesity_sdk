# SapHanaProtectionGroupParams

Specifies parameters related to the SAP HANA Protection job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 8]
**delta** | **str** | Specifies the incremental backup delta (incremental/differential) | 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**source_id** | **int** | Specifies the source Id of the objects to be protected. | 

## Example

```python
from cohesity_sdk.cluster.models.sap_hana_protection_group_params import SapHanaProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaProtectionGroupParams from a JSON string
sap_hana_protection_group_params_instance = SapHanaProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(SapHanaProtectionGroupParams.to_json())

# convert the object into a dict
sap_hana_protection_group_params_dict = sap_hana_protection_group_params_instance.to_dict()
# create an instance of SapHanaProtectionGroupParams from a dict
sap_hana_protection_group_params_from_dict = SapHanaProtectionGroupParams.from_dict(sap_hana_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


