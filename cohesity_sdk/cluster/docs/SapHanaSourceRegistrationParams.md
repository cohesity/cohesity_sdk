# SapHanaSourceRegistrationParams

Specifies parameters to register a SAP HANA source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backint_protocol_version** | **str** | Backint protocol version to be used during backup/restore. | [optional] [default to '1.0']
**hosts** | **List[str]** | Specifies the IPs/hostnames for the nodes forming the SAP HANA source cluster. | 
**script_dir** | **str** | Specifies the absolute path of scripts used to interact with the SAP HANA source. | 
**source_name** | **str** | Specifies user friendly name for the source. | 

## Example

```python
from cohesity_sdk.cluster.models.sap_hana_source_registration_params import SapHanaSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaSourceRegistrationParams from a JSON string
sap_hana_source_registration_params_instance = SapHanaSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(SapHanaSourceRegistrationParams.to_json())

# convert the object into a dict
sap_hana_source_registration_params_dict = sap_hana_source_registration_params_instance.to_dict()
# create an instance of SapHanaSourceRegistrationParams from a dict
sap_hana_source_registration_params_from_dict = SapHanaSourceRegistrationParams.from_dict(sap_hana_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


