# SapHanaObjectProtectionParams

Specifies the parameters that are specific to SAP HANA Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams thatwill be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 8]
**delta** | **str** | Specifies the incremental backup delta (incremental/differential) | [optional] [default to 'incremental']
**objects** | [**List[UdaObjectProtectionObjectParams]**](UdaObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 

## Example

```python
from cohesity_sdk.cluster.models.sap_hana_object_protection_params import SapHanaObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaObjectProtectionParams from a JSON string
sap_hana_object_protection_params_instance = SapHanaObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(SapHanaObjectProtectionParams.to_json())

# convert the object into a dict
sap_hana_object_protection_params_dict = sap_hana_object_protection_params_instance.to_dict()
# create an instance of SapHanaObjectProtectionParams from a dict
sap_hana_object_protection_params_from_dict = SapHanaObjectProtectionParams.from_dict(sap_hana_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


