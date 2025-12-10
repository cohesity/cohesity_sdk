# SapHanaParams

Specifies the recovery options specific to SAP HANA environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_sap_hana_params** | [**RecoverSapHanaParams**](RecoverSapHanaParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.sap_hana_params import SapHanaParams

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaParams from a JSON string
sap_hana_params_instance = SapHanaParams.from_json(json)
# print the JSON string representation of the object
print(SapHanaParams.to_json())

# convert the object into a dict
sap_hana_params_dict = sap_hana_params_instance.to_dict()
# create an instance of SapHanaParams from a dict
sap_hana_params_from_dict = SapHanaParams.from_dict(sap_hana_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


